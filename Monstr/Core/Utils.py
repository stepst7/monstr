import datetime
import pytz
import urllib
import ssl

def get_page(url):
    """Return html code from cmsweb.cern.ch of the page with the given url"""
    print "HTTP access: ", url
    try:
        socket_obj = urllib.urlopen(url)
    except Exception, e:
        print e
        context = ssl._create_unverified_context()
        socket_obj = urllib.urlopen(url, context=context)
    page = socket_obj.read()
    socket_obj.close()
    return page

def epoch_to_datetime(seconds):
    new_time = datetime.datetime.utcfromtimestamp(float(seconds)).replace(tzinfo=pytz.utc)
    return new_time

def get_UTC_now():
    return datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
