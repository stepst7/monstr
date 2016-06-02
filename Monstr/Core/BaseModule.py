import logging
from abc import ABCMeta, abstractmethod
import Monstr.Core.DB as DB



# ,----------------------.
# |BaseNodule            |
# |----------------------|
# |+string name          |
# |+obj table_schemas    |
# |----------------------|
# |+void Initialize()    |
# |+obj PrepareRetrieve()|
# |+obj Retrieve()       |
# |+obj InsertToDB()     |
# |+obj Analyze()        |
# |+obj React()          |
# |+obj Run()            |
# `----------------------'


class BaseModule():
    __metaclass__ = ABCMeta
    
    name = None
    table_schemas = None
    tables = None
    db_handler = None

    def __init__(self):
        self.db_handler = DB.DBHandler()

    def checkClass(self):
        if self.name == None:
            raise "Module require name"
        if self.table_schemas == None:
            raise "Module require schemas list"
        self.tables = {}

        for schema in self.table_schemas:
            table_name = self.name + '_' + schema
            table = self.db_handler.checkSchema(table_name, self.table_schemas[schema])
            self.tables[schema] = table



    def Initialize(self):
        self.checkClass()


    def PrepareRetrieve(self):
        return {}

    @abstractmethod
    def Retrieve(self, params):
        pass

    def InsertToDB(self, data):
        for schema in data:
            table = self.tables[schema]
            self.db_handler.bulk_insert(table, data[schema])        

    def ExecuteCheck(self):
        self.Initialize()
        params = self.PrepareRetrieve()
        data = self.Retrieve(params)
        self.InsertToDB(data)
