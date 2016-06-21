from sqlalchemy import Table, Column, Integer, String, DateTime, Enum, Text, UniqueConstraint, MetaData
from sqlalchemy import create_engine
from sqlalchemy.exc import NoSuchTableError
from sqlalchemy.orm import sessionmaker

import Monstr.Core.Config as Config

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DBHandler():
    __metaclass__ = Singleton

    engine = None
    session = None

    def __init__(self):
        db_conf = Config.get_section('Database')
        user, password, host, name = db_conf['user'], db_conf['password'], db_conf['host'], db_conf['name']
        connection_string = 'postgresql://' + user + ':' + password + '@' + host + '/' + name

        self.engine = create_engine(connection_string, echo=False)
        self.session = sessionmaker(bind=self.engine)()
        self.metadata = MetaData(self.engine)

    def makeTable(self, name, schema):
        table = Table(name, self.metadata, *schema)
        table.create(checkfirst=True)
        return table

    def getOrCreateTable(self, name, schema):
        metadata = self.metadata
        table = None
        try:
            table = Table(name, metadata, autoload=True)
            print 'Table exist'
        except NoSuchTableError:
            self.makeTable(name, schema)
            table = Table(name, metadata, autoload=True)
        return table

    def initialize(self, schemas, prefix):
        tables = {}
        for schema in schemas:
            table_name = prefix + '_' + schema
            table = self.getOrCreateTable(table_name, schemas[schema])
            tables[schema] = table
        return tables

    def clear(self, params):
        pass

    def bulk_insert(self, table, insert_list):
        if len(insert_list) > 0:
            self.engine.execute(table.insert(), insert_list)

    def get_new_metadata(self):
        return MetaData(self.engine)

    def get_session(self):
        return self.session

    def get_engine(self):
        return self.engine
