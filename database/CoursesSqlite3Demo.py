#Import sqlite3 module
import sqlite3

#Connecting to sqlite database by using connect() method
#if that database does not exist, then it'll be created
conn = sqlite3.connect("Courses.db")

#Returns a database cursor object to excute SQL Statements
cursor = conn.cursor()

#Drop tables if it exists
cursor.execute("DROP TABLE IF EXISTS User")
cursor.execute("DROP TABLE IF EXISTS Course")
cursor.execute("DROP TABLE IF EXISTS Student")

#Create the user table
cursor.execute("create table User ( " +
               "userId integer not null, username varchar(32) not null, " +
               "password varchar(512) not null, " +
               "primary key (userId))")

#Insert user entry
cursor.execute("insert into User (userId, username, password) " +
               "values (1,'stan0001','@cHapter1')")

cursor.execute("insert into User (userId, username, password) " +
               "values (2,'britt0002','password123')")

#Create the Course Table
cursor.execute("create table Course ( " +
               "courseId char(5), subjectId char(4) not null, " +
               "courseNumber integer, title varchar(50) not null, " +
               "numOfCredits integer, primary key (courseId))")

#Insert course entries
cursor.execute("insert into Course (courseId, subjectId, " +
               "courseNumber, title, numOfCredits) " +
               "values ('11111','CS',1030,'Python Programming 1',3)")

cursor.execute("insert into Course (courseId, subjectId, " +
               "courseNumber, title, numOfCredits) " +
               "values ('11112','CS',2030,'Python Programming 2',3)")

#Create the Student Table
cursor.execute("create table Student(studentId integer, name char(30), age integer, " +
               "gender char(1), major char(6), phone varchar(12), userId integer, " +
               "foreign key(userId) references User(userId), primary key (studentId))")

#Insert Student entry
cursor.execute("insert into Student(studentId,name,age,gender,major,phone,userId) " +
               "values (700300001,'Stan Smith',23,'M','CS','816-111-1111',1)")

#Insert Student entry
cursor.execute("insert into Student(studentId,name,age,gender,major,phone,userId) " +
               "values (700300002,'Britt Green',27,'F','SE','816-222-1111',2)")

#Commits any pending changes to the database
conn.commit()
cursor.execute("select * from Course")
rows = cursor.fetchmany(2) #Return a list consisiting of tuples
for i in rows:
    print(i)
print()

#Display Students
cursor.execute("select * from Student")
rows = cursor.fetchone()
print(rows)
print()

#Display User
cursor.execute("select * from User")
rows = cursor.fetchone()
print(rows)
print()

#Update a new user
studentId = 700300003
name = input("Please enter the student name: ")
age = int(input("Please enter the age: "))
gender = input("Gender: ")
major = input("Major: ")
phone = input("Phone Number: ")
userId = 3
cursor.execute("insert into Student(studentId,name,age,gender,major,phone,userId) " +
               f"values ('{studentId}','{name}','{age}','{gender}','{major}','{phone}','{userId}')")



cursor.execute("select * from Student")
rows = cursor.fetchall()
for i in rows:
    print(i)
print()

#Updating
cursor.execute('''update User set password = 'newpassword' where userId == 1;''')
cursor.execute('''update Student set major = 'CYBR' where userId == 2;''')
conn.commit()
conn.close()


            










               
