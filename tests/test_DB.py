import Monstr.Core.DB as DB

from Monstr.Core.DB import Column, Integer, String, DateTime, UniqueConstraint

schema1 = (Column('id', Integer, primary_key=True),
                              Column('time', DateTime(True)),
                              Column('user_name', String(30)),
                              Column('password', String(30)),
                              UniqueConstraint("user_name"),)

schema2 = (Column('id', Integer, primary_key=True),
                              Column('user_name', String(30)),
                              Column('password', String(30)),
                              UniqueConstraint("user_name"),)

schema3 = (Column('id', Integer, primary_key=True),
                              Column('date', DateTime(True)),
                              Column('user_name', String(30)),
                              Column('password', String(30)),
                              UniqueConstraint("user_name"),)

db_handler = DB.DBHandler()

def test_CreateTableIfAbsent():
    db_handler.getOrCreateTable('test', schema1)
    db_handler.getOrCreateTable('test', schema2)
    db_handler.getOrCreateTable('test', schema3)