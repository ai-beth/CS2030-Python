#Import sqlaclachemy modules
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, declarative_base

#Create the base class
Base = declarative_base()

#Create the Engine Object to create the DB if it does not exist
#Echo flag will give use a real time activity log
engine = create_engine('sqlite:///Student.db',echo = False)

#Create the student class with the super class of base
class Student(Base):

    #Create the table student
    __tablename__ = 'Student'
    #Column within student tables
    id = Column(String(9),primary_key = True, unique = True)
    name = Column(String(32), nullable = False)
    age = Column(Integer)
    gender = Column(String(1))
    major = Column(String(32))
    

#Create the user class with the super class of base
class User(Base):

    #Create the table user
    __tablename__ = 'User'
    #Column within user table
    name = Column(String(32),primary_key = True, nullable = False)
    password = Column(String(512))

#Create the Score Class with the sper class of base
class Score(Base):
    #Create the Table score
    __tablename__ = 'Score'
    #Column within the score table
    id = Column(String(9), primary_key = True, unique = True)
    name = Column(String(32), nullable = False)
    CS1030 = Column(Integer)
    CS2030 = Column(Integer)
    CS4600 = Column(Integer)

Base.metadata.create_all(engine)

#Create a session object to initiate query in the db
Session = sessionmaker(bind = engine)
session = Session()
'''
s1 = Student(id = 7001, name = "Bret Star", age = 22, gender = 'F', major = 'CS')
session.add(s1)
session.commit()

session.add_all([
    Student(id = 7002, name = "Jane Star", age = 22, gender = 'F', major = 'CS'),
    Student(id = 7003, name = "Tiff Star", age = 22, gender = 'F', major = 'SE'),
    Student(id = 7004, name = "Tom Star", age = 22, gender = 'M', major = 'DS'),
    Student(id = 7005, name = "John Star", age = 22, gender = 'M', major = 'CYBR')])
session.commit()
'''
#Select name from student
result = session.query(Student.name,Student.major)
print(f"Query 1: {result}")
for i in result:
    print(i.name,'|',i.major)
print()

#COunt how many students are in the database
result = session.query(Student).count()
print(f"Number of students: {result}")

#Delete from student where there major is DS
result = session.query(Student).filter(Student.major == 'DS')\
         .delete(synchronize_session = False)
print(f"Rows deleted: {result}")
session.commit()

#Recount the students in the db
result = session.query(Student).count()
print(f"Number of students: {result}")
print()




    
