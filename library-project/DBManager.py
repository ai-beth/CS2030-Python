#Database
#imports
import sqlite3

#Database class
class Database:

    #Initializer
    #INitializes the database class witht the specified database name
    def __init__(self, db_name="Library.db"):
        self.db_name = db_name

    #Connect
    #Establishes a connection to the SQLite database
    def connect(self):
        #return a connection to the specified database
        return sqlite3.connect(self.db_name)

    #Initialize
    #Create the necessary tables
    def initialize(self):
        #using with statement to ensure the connection is closed automatically when done
        with self.connect() as conn:
            #Create teh cursor object to exucute SQL commands
            cursor = conn.cursor()
            
            #Create users table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )
            """)
            
            #Create books table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Books (
                isbn TEXT PRIMARY KEY ,
                title TEXT UNIQUE NOT NULL,
                author TEXT NOT NULL,
                genre TEXT NOT NULL,
                year INTEGER NOT NULL,
                pages INTEGER NOT NULL,
                status TEXT NOT NULL,
                notes TEXT
            )
        """)
            #Commit to save
            conn.commit()

    
    
