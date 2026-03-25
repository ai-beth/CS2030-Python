#Import sqlAlchemy
from sqlalchemy import *

#The create_engine() function takes the database as one argument.
#If the database is not defined anywhere it will get created.
#returns an Engine Object
engine = create_engine('sqlite:///college.db',echo = True)

#The echo flag is a shortcut to set up SQLAlchemy logging

#Methods from the Engine Class
#connect() = returns connection object
#execute() = Executes a Sql statement construct
#begin() = Returns a context manager deliviering a Connection
#dispose() = Disposes of the connection pool used by the engine
#driver() = Driver name of the Dialect in use by the engine
#table_names() = Returns a list of all table names available in the db

#SQLAlchemy Column object represents a column in a db table which is in turn
#represented by a Table Object.

#Metadata contains definitions of tables and associated objects such as
#index, view, triggers, etc.

#Matadata is a collection of Table Object as well as an optional binding to an
#engine or Connection

meta = MetaData()
#Constructor of MetaData class can have bind and schema parameters which
#are by default None

#Column object represents a column in a database table. Constructor takes
#name, type, and other parameters such as primary_key, autoincrement, and
#other constraints

#SQLAchemy matches Python data to the best possible generic column data types
#BigInteger, Boolean, Date, DateTime, Float, Integer, Numeric, String, etc.

students = Table(
    'students', meta,
    Column('id',Integer,primary_key = True),
    Column('name',String),
    Column('lastname',String))

#The create_all() function uses the engine object to create all the defined
#table objects and stores the information in metadata
meta.create_all(engine)

#We now have a Sqlite database name college.db with a student table in it
#echo attribute of create_engine is set to True, the console will display the
#actual SQL query for the table creation (Pretty Cool)

#Insert statement is created by executing insert() method
#returns a insert object that can be verified by using str() function
ins = students.insert()
print(str(ins))

#It is possible to insert value in a specific field by values() method
#to insert object
ins = students.insert().values(name = 'Tom')
print(str(ins))
#Echoed on Python console doesn't show the actual value Tom
#Instead Sqlalchemy generates a bind parameter which is visible in complied form
#of the statement

print(ins.compile().params)
print()
#In order to execute the SQL Expression, we have to obtain a connection object
#representing an actively checked out DBAPI connection resource and then
#feed the expression object
conn = engine.connect()

#The insert() object can be used for execute() method
ins = students.insert().values(name = 'Mike', lastname = 'Ross')
result = conn.execute(ins)
conn.commit()
print()
#To issue many inserts using DBAPI'S execute many() method
#we can send in a list of dictionaries each containing a distinct set
#of parameters to be inserted
conn.execute(students.insert(),[
    {'name':'Stan','lastname':'Smith'},
    {'name':'Steve','lastname':'Smith'},
    {'name':'Roger','lastname':'Smith'},
    {'name':'Haily','lastname':'Smith'}])
conn.commit()
print()
#The select() method of table object enables us to construct SELECT Expression
s = students.select()
print(s)

#We can use this select object as a paraeter to execute() method
#of connection object
result = conn.execute(s)
print(result)

#Fetch records using the fetchone() method
row = result.fetchone()
print()
print(row)

#Display each row
for row in result:
    print(row)
print()





