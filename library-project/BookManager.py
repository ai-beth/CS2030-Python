#Book Manager
#Needs a lot more work
#Imports
from tkinter import Toplevel, messagebox, ttk
import tkinter as tk
import sqlite3

#Book Manager Class
class BookManager:

    #Initializer
    #Initializes the BookManager with a database connection object.
    def __init__(self, db):
        self.db = db

    #Add Book
    #Adds a new book to the database.
    def add_book(self, isbn, title, author, genre, year, pages, status, notes):
        try:
            #Establish connection to the database
            with self.db.connect() as conn:
                cursor = conn.cursor() 
                #Insert the new book into the database
                cursor.execute(
                    """
                    INSERT INTO Books (isbn, title, author, genre, year, pages, status, notes)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (isbn, title, author, genre, year, pages, status, notes)
                )
                conn.commit()
        except sqlite3.IntegrityError as e:
            #Handle general SQLite integrity errors
            raise ValueError("An error occurred while adding the book: " + str(e))

    #Query Books
    #Searches for books matching the query in any field of the Books table.
    def query_books(self, query):
        with self.db.connect() as conn:
            cursor = conn.cursor()
            query = f"%{query}%"  #Prepare query for partial matching
            #Execute SQL to search all fields in the Books table
            cursor.execute(
                """
                SELECT * FROM Books WHERE
                isbn LIKE ? OR
                title LIKE ? OR
                author LIKE ? OR
                genre LIKE ? OR
                year LIKE ? OR
                pages LIKE ? OR
                status LIKE ? OR
                notes LIKE ?
                """,
                (query, query, query, query, query, query, query, query)
            )  
            #Get column names
            columns = [description[0] for description in cursor.description] 
            #Convert each row into a dictionary using the column names
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        #Return results  
        return results

    #Delete Book
    #Deletes a book from the database based on its ISBN
    def delete_book(self, isbn):
        with self.db.connect() as conn:
            cursor = conn.cursor()
            #Execute SQL to delete the book by ISBN
            cursor.execute("DELETE FROM Books WHERE isbn = ?", (isbn,))
            conn.commit()

    #Update Book
    #Updates a specific field of a book in the database.
    def update_book(self, isbn, field, value):
        with self.db.connect() as conn:
            cursor = conn.cursor()
            #Execute SQL to update the specified field for the book
            cursor.execute(f"UPDATE Books SET {field} = ? WHERE isbn = ?", (value, isbn))
            conn.commit()#Commit to save

    #View All Books
    #Retrieves all books from the database
    def view_all_books(self):
        with self.db.connect() as conn:
            cursor = conn.cursor()
            #Execute SQL to fetch all rows from the Books table
            cursor.execute("SELECT * FROM Books")
            #Get column names
            columns = [description[0] for description in cursor.description]
            #Convert each row into a dictionary using the column names
            books = [dict(zip(columns, row)) for row in cursor.fetchall()]
        #return a list of all books(dictionaries)(Confusing!) in the database 
        return books



