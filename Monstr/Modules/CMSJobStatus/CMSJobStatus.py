#!/bin/python

import Monstr.Core.Utils as Utils
import Monstr.Core.DB as DB
import Monstr.Core.BaseModule as BaseModule

from datetime import timedelta
import json
import pytz
from pprint import pprint as pp

from Monstr.Core.DB import Column, Integer, String, DateTime, UniqueConstraint
from sqlalchemy.sql import func

class CMSJobStatus(BaseModule.BaseModule):
    name = 'CMSJobStatus'
    table_schemas = {'main': (Column('id', Integer, primary_key=True),
                              Column('time', DateTime(True)),
                              Column('site_name', String(60)),
                              Column('aborted', Integer),
                              Column('app_succeeded', Integer),
                              Column('applic_failed', Integer),
                              Column('application_failed', Integer),
                              Column('cancelled', Integer),
                              Column('pending', Integer),
                              Column('running', Integer),
                              Column('site_failed', Integer),
                              UniqueConstraint("time", "site_name"),)
                    }
    # tables = None

    def __init__(self):
        super(CMSJobStatus, self).__init__()
        self.db_handler = DB.DBHandler()

    def isInteresting(self, site_name):
        if site_name.startswith('T1'):
            return True
        if site_name.startswith('T0'):
            return True
        if site_name == 'T2_CH_CERN':
            return True
        return False

    def PrepareRetrieve(self):
        current_time = Utils.get_UTC_now().replace(minute=0, second=0, microsecond=0)
        last_time = None
        last_row = self.db_handler.get_session().query(func.max(self.tables['main'].c.time).label("max_time")).one()
        if last_row[0]:
            last_time = last_row[0].replace(tzinfo=pytz.utc)
            if current_time - last_row[0] > timedelta(days=7):
                last_time = current_time - timedelta(days=7)
        else:
            last_time = current_time - timedelta(days=7)
        return {'last_time': last_time,
                'current_time': current_time}

    def Retrieve(self, params):
        last_time = params['last_time']
        current_time = params['current_time']
        insert_list = []
        
        while last_time < current_time:
            begin = last_time
            end = last_time + timedelta(hours=1)
            time1 = '+' + str(begin.hour) + "%3A00"
            time2 = '+' + str(end.hour) + "%3A00"
            date1 = str(begin).split(' ')[0] + time1
            date2 = str(end).split(' ')[0] + time2
            url = "http://dashb-cms-job.cern.ch/dashboard/request.py/jobsummary-plot-or-table2?user=&submissiontool=&application=&activity=&status=&check=terminated&tier=&sortby=site&ce=&rb=&grid=&jobtype=&submissionui=&dataset=&submissiontype=&task=&subtoolver=&genactivity=&outputse=&appexitcode=&accesstype=&inputse=&cores=&date1=" + date1 + "&date2=" + date2 + "&prettyprint"
            
            json_raw = Utils.get_page(url)
            json_obj = json.loads(json_raw)['summaries']

            for obj in json_obj:
                site_name = str(obj['name'])
                if self.isInteresting(site_name):
                    current_status = {'site_name': site_name,
                                        'time': last_time,
                                        'applic_failed': int(obj['applic-failed']),
                                        'app_succeeded': int(obj['app-succeeded']),
                                        'pending': int(obj['pending']),
                                        'running': int(obj['running']),
                                        'aborted': int(obj['aborted']),
                                        'application_failed': int(obj['application-failed']),
                                        'site_failed': int(obj['site-failed']),
                                        'cancelled': int(obj['cancelled'])}

                    insert_list.append(current_status)
            last_time = last_time + timedelta(hours=1)
        return {'main': insert_list}

def InsertToDB():
    X = CMSJobStatus()
    X.ExecuteCheck()

if __name__=='__main__':
    InsertToDB()