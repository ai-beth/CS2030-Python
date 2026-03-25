#User Manager

#Imports
import hashlib
from tkinter import Toplevel, messagebox, ttk
import tkinter as tk
from BookManager import BookManager
import sqlite3
import re


#User Manager
class UserManager:

    #Initializer
    #Initialize the UserManager with a database connection.
    def __init__(self, db):
        self.db = db

    #Hash Password
    #Hash a password using sha256 for secure storage.
    def hash_password(self, password):

        #Return the hashed password
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    #Validate User
    #Validate a user's login credentials by checking the username and password
    #against the database.
    def validate_user(self, username, password):

        #hash the password
        hashed_password = self.hash_password(password)
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM Users WHERE username = ? AND password = ?",
                (username, hashed_password),
            )
            #Returns the user data if the credentials match
            return cursor.fetchone()  

    #Validate Password
    def validate_password(self, password):
        """Criteria:
             - Must begin with a special character (!@#$%^&*)
             - Must contain a lowercase letter
             - Must contain a capital letter
             - Must be between 6 and 12 characters"""
        #copied this from hashLibDemo but I think it needs to be 5 and 11
        #instead of 6 and 12
        pattern = r"^[!@#$%^&].*(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{5,11}$"
        return bool(re.match(pattern, password))

    #Validate Username
    def validate_username(self, username):  
        """Criteria:
            - Must be between 3 and 6 characters.
            - Must start with a capital letter."""
        
        pattern = r"^[A-Z][A-Za-z\d]{2,5}$"
        return bool(re.match(pattern, username))


    #Add User
    #Add a new user to the database after validating the username and password.
    def add_user(self, username, password):

        #Check if the password and username meet validation criteria
        #If it doesn't, raise a ValueError with appropriate message
        if not self.validate_username(username):
            raise ValueError("Invalid username. Must start with a capital letter and be 3-6 characters long.")
        if not self.validate_password(password):
            raise ValueError("Invalid password. Must be 6-12 characters long and start with a special character.")

        #Establish database connection using context manager
        with self.db.connect() as conn:
            cursor = conn.cursor()
            try:
                #Hash the password to store in teh database
                hashed_password = self.hash_password(password)
                
                #Insert the new user data into Users table
                cursor.execute(
                    "INSERT INTO Users (username, password) VALUES (?, ?)",
                    (username, hashed_password),
                )

                #Commit the transaction to save changes to the database
                conn.commit()
                #Display message to the user
                messagebox.showinfo("Success", "User created successfully!")
            #If the username already exists, raise an error   
            except sqlite3.IntegrityError:
                raise ValueError("Username already exists.")
