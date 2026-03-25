#imports
from tkinter import Toplevel, messagebox, ttk
import tkinter as tk
from UserManager import UserManager
from BookManager import BookManager
import sqlite3
import re

#UI Manager
class UIManager:

    #Initializer
    #initilizes the ui manager with the given root window and database
    #Sets up the login screen
    def __init__(self, root, db):
        #Main app window
        self.root = root
        #database connection
        self.db = db
        #window title
        self.root.title("The Library")

        #initilaize the UserManager and BookManager using hte database
        self.user_manager = UserManager(db)
        self.book_manager = BookManager(db)

        #Track if the user is loggin in and store their username
        self.user_logged_in = False
        self.username = ""
        #Display the login screen when the app starts
        self.login_screen()

    #Load Text
    #Load and display .txt file instructions in a messagebox
    def load_txt(self, filepath):
        # Try to open the specified text file and read its contents
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
                #Display the content of the file in a messagebox
                messagebox.showinfo("Instructions", content)
        #If the file is not found or there is a decoding issue
        #show an error message
        except FileNotFoundError:
            messagebox.showerror("Error", f"File '{filepath}' not found.")
        except UnicodeDecodeError:
            messagebox.showerror("Error", "There was an issue with reading the file. Please check the encoding.")


    #Login Screen
    #Creates the login screen with fields for username and password
    #allows new account creation 
    def login_screen(self):
        #frame to hold login UI elements
        login_frame = ttk.Frame(self.root, padding=20)
        #pack the frame to the window
        login_frame.pack()
        #Title Label
        ttk.Label(login_frame, text="Login to The Library", font=("Arial", 20)).pack(pady=10)
        #username label and input field
        ttk.Label(login_frame, text="Username:").pack(pady=2)
        #username entry widget
        self.username_entry = ttk.Entry(login_frame, width=30)
        self.username_entry.pack(pady=2)
        #Password label and input field (masked)
        ttk.Label(login_frame, text="Password:").pack(pady=2)
        #password entry widget 
        self.password_entry = ttk.Entry(login_frame, show="*", width=30)
        self.password_entry.pack(pady=2)

        #Attempt Login
        #Attemps to log in using the entered username and password
        #If valid, transitions to the main menu, Otherwise show an error. 
        def attempt_login():
            #Get username 
            username = self.username_entry.get().strip()
            #Get password
            password = self.password_entry.get().strip()
            #validate user credentials
            if self.user_manager.validate_user(username, password):
                #mark user as logged in
                self.user_logged_in = True
                #store the username of the logged in user
                self.username = username
                #destroy the login frame to transition to the main menu
                login_frame.destroy()
                #Set up the main menu screen
                self.setup_main_menu()
            else:
                #or show an error
                messagebox.showerror("Error", "Invalid username or password.")
        #Login button
        ttk.Button(login_frame, text="Login", command=attempt_login).pack(pady=10)


        #Create User Window
        #Opens the user creation screen when clicked
        def create_user_window():
            #destroy the login screen
            login_frame.destroy()
            #set up screen to create a new user
            self.setup_create_user_screen()
        #'Create new user' button
        ttk.Button(login_frame, text="Create New User", command=create_user_window).pack(pady=10)

    #Setup 'create user' screen
    #Sets up the screen for creating a new user account
    #validates the password and username and attempts to add the user to the database
    def setup_create_user_screen(self):
        #Frame for user creation
        create_user_frame = ttk.Frame(self.root, padding=20)
        create_user_frame.pack()
        #Title label
        ttk.Label(create_user_frame, text="Create a New User", font=("Arial", 20)).pack(pady=10)
        # USername label and entry field for creating new user
        ttk.Label(create_user_frame, text="Username:").pack(pady=2)
        #entry widget for username input
        self.create_username_entry = ttk.Entry(create_user_frame, width=30)
        self.create_username_entry.pack(pady=2)
        #Password label for creating a new user (masked****)
        ttk.Label(create_user_frame, text="Password:").pack(pady=2)
        #entry widget for password input
        self.create_password_entry = ttk.Entry(create_user_frame, show="*", width=30)
        self.create_password_entry.pack(pady=2)

        #Save User
        #Saves new user to the database after validating the username and password
        #Displays an error if there is a validation issue
        def save_user():
            #Get the username and password from the input fields
            username = self.create_username_entry.get().strip()
            password = self.create_password_entry.get().strip()
            # Validate password 
            if self.user_manager.validate_password(password):
                try:
                    # adding the new user to the database
                    self.user_manager.add_user(username, password)
                    # Destroy the user creation screen
                    create_user_frame.destroy()
                    # Return to the login screen
                    self.login_screen()
                #Show an error message if the user creation fails
                except ValueError as e:
                    messagebox.showerror("Error", str(e))
            else:#Show an error if the password or username are invalid
                messagebox.showerror(
                    "Error",
                    "Password must start with a special character (!@#$%^&*), "
                    "include at least one digit, one lowercase letter, one uppercase letter, "
                    "and be between 6 and 12 characters long,"
                    "Username Must start with a capital letter,"
                    "and be 3 - 6 characters.",
                    
                )
        #Button to save the new user
        ttk.Button(create_user_frame, text="Create User", command=save_user).pack(pady=10)
        #button to view the rules
        ttk.Button(create_user_frame, text="View Rules", command=lambda: self.load_txt("rules.txt")).pack(pady=10)

    #Setup Main Menu
    #Sets up the main menu screen after a user logs in
    #provides options for the user to manage books and log out
    def setup_main_menu(self):
        #Frame for the main menu UI
        main_frame = ttk.Frame(self.root, padding=60)
        main_frame.pack()
        #"Welcome, User" message
        ttk.Label(main_frame, text=f"Welcome, {self.username}", font=("Arial", 20)).pack(pady=10)
        #List of buttons for book management and logging out
        buttons = [
            ("Add Book", self.add_book_window),
            ("Modify Book", self.modify_books_window),
            ("Query Books", self.query_books_window),
            ("View All Books", self.view_all_books_window),
            ("Delete Book", self.delete_book_window),
            ("Log Out", self.logout),
        ]
        #Create a button for each action in the list
        for text, command in buttons:
            ttk.Button(main_frame, text=text, command=command, width=25).pack(pady=5)

    #Add Book window
    #Creates a window for adding a new book with teh fields for book details
    def add_book_window(self):
        #Create a new TopLevel window for adding a book 
        add_window = Toplevel(self.root)
        #Set the window title
        add_window.title("Add a Book")

        #Create a frame for organizing the fields in a grid layout
        form_frame = ttk.Frame(add_window)
        form_frame.pack(padx=20, pady=20)

        #ISBN
        ttk.Label(form_frame, text="Enter ISBN:").grid(row=6, column=0, sticky="w", pady=5)
        #ISBN entry widget
        isbn_entry = ttk.Entry(form_frame, width=40)
        isbn_entry.grid(row=6, column=1, pady=5)

        #Title
        ttk.Label(form_frame, text="Enter Book Title:").grid(row=0, column=0, sticky="w", pady=5)
        #Title Entry widget
        title_entry = ttk.Entry(form_frame, width=40)
        title_entry.grid(row=0, column=1, pady=5)

        #Author
        ttk.Label(form_frame, text="Enter Book Author:").grid(row=1, column=0, sticky="w", pady=5)
        author_entry = ttk.Entry(form_frame, width=40)
        author_entry.grid(row=1, column=1, pady=5)

        #Genre
        ttk.Label(form_frame, text="Enter Genre:").grid(row=2, column=0, sticky="w", pady=5)
        genre_entry = ttk.Entry(form_frame, width=40)
        genre_entry.grid(row=2, column=1, pady=5)

        #Year
        ttk.Label(form_frame, text="Enter Year:").grid(row=3, column=0, sticky="w", pady=5)
        year_entry = ttk.Entry(form_frame, width=40)
        year_entry.grid(row=3, column=1, pady=5)

        #Pages
        ttk.Label(form_frame, text="Enter Pages:").grid(row=4, column=0, sticky="w", pady=5)
        pages_entry = ttk.Entry(form_frame, width=40)
        pages_entry.grid(row=4, column=1, pady=5)

        #Status(Dropdown Menu)
        ttk.Label(form_frame, text="Select Status:").grid(row=5, column=0, sticky="w", pady=5)
        #Available statuses
        status_options = ["Reading", "Finished", "Want To Read", "Abandoned"]
        #Combobox for status selection
        status_combobox = ttk.Combobox(form_frame, values=status_options, width=38)
        status_combobox.grid(row=5, column=1, pady=5)
        status_combobox.set(status_options[0])#default value
        
        #Notes
        ttk.Label(form_frame, text="Enter Notes:").grid(row=7, column=0, sticky="w", pady=5)
        notes_entry = ttk.Entry(form_frame, width=40)
        notes_entry.grid(row=7, column=1, pady=5)


        #Save Book
        #Gathers user inputs and saves the book 
        def save_book():
            #Retrieve and clean input values from the relating entry fields
            isbn = isbn_entry.get().strip()
            title = title_entry.get().strip().title()
            author = author_entry.get().strip().title()
            genre = genre_entry.get().strip().upper()
            year = year_entry.get().strip()
            pages = pages_entry.get().strip()
            #Get selected status from combobox
            status = status_combobox.get().strip().upper()  
            notes = notes_entry.get().strip()
            try:#Attempt to add the new book using input data
                self.book_manager.add_book(isbn, title, author, genre, int(year), int(pages), status, notes)
                #Show success message
                messagebox.showinfo("Success", "Book added successfully!")
                #Destroy the add book window
                add_window.destroy()
            except ValueError as e:
                #Show error message if there is a ValueError(invalid data etc)
                messagebox.showerror("Error", str(e))
        #Add Book button
        ttk.Button(add_window, text="Add Book", command=save_book).pack(pady=10)

    #Modify Books Window
    #handles the window where a user can modify an existing book 
    def modify_books_window(self):
        #Create new TopLevel window for modification 
        modify_window = Toplevel(self.root)
        #window title
        modify_window.title("Modify Book")

        #Label to prompt the user for ISBN of book to modify
        ttk.Label(modify_window, text="Enter ISBN of Book to Modify:").pack(pady=10)
        isbn_entry = ttk.Entry(modify_window, width=30)
        isbn_entry.pack(pady=5)


        #Load Book Details
        def load_book_details():
            #retireve isbn entered by user
            isbn = isbn_entry.get().strip()
            #Query databse for the book with the provided ISBN
            book = self.book_manager.query_books(isbn)
            if book:#IF found, get the details and call display_modify_Form
                book_details = book[0] if isinstance(book, list) else book#might not need, but oh well
                display_modify_form(book_details)
            else:#or show error message if no book found. 
                messagebox.showerror("Error", "No book found with the given ISBN.")

        #Display 'Modify' Form
        def display_modify_form(book_details):
            #Destroy previous widgets to refresh the form
            for widget in modify_window.winfo_children():
                widget.destroy()
            #Create the form layout for modifying book details
            form_frame = ttk.Frame(modify_window)
            form_frame.pack(padx=20, pady=20)

            #Define fields to modify and prepopulate them
            fields = {
                "Title": book_details['title'],
                "Author": book_details['author'],
                "Genre": book_details['genre'],
                "Year": book_details['year'],
                "Pages": book_details['pages'],
                "Status": book_details['status'],
                "Notes": book_details['notes'],
            }
            entries = {}
            for i, (field, value) in enumerate(fields.items()):
                #for each field, create a label and an entry box
                ttk.Label(form_frame, text=f"{field}:").grid(row=i, column=0, sticky="w", pady=5)
                entry = ttk.Entry(form_frame, width=40)
                #Insert the current value of the book detail into the entry box
                entry.insert(0, value)
                entry.grid(row=i, column=1, pady=5)
                #Store reference to the entry box for later use
                entries[field] = entry
            #Status (Dropdown)
            ttk.Label(form_frame, text="Select Status:").grid(row=len(fields), column=0, sticky="w", pady=5)
            #Status options
            status_options = ["Reading", "Finished", "Want To Read", "Abandoned"]
            status_combobox = ttk.Combobox(form_frame, values=status_options, width=38)
            #Set the surrent status in the combobox
            status_combobox.set(book_details['status'])
            status_combobox.grid(row=len(fields), column=1, pady=5)

            #Save Changes
            def save_changes():
                #Collect updated values from the fields
                updated_values = {field: entry.get().strip() for field, entry in entries.items()}
                #Get the selected status
                updated_values["status"] = status_combobox.get().strip()
                try:#Update the book details for each field
                    for field, value in updated_values.items():
                        self.book_manager.update_book(book_details['isbn'], field.lower(), value)
                    #Show success message
                    messagebox.showinfo("Success", "Book updated successfully!")
                    #Close the modify window
                    modify_window.destroy()
                except ValueError as e:#Error message for ValueError
                    messagebox.showerror("Error", str(e))
            #Save changes button
            #Triggers save_changes
            ttk.Button(modify_window, text="Save Changes", command=save_changes).pack(pady=10)
        #Load Book Button
        #triggers load_book_details when clicked
        ttk.Button(modify_window, text="Load Book", command=load_book_details).pack(pady=10)

    #Query Books Window
    #Handles search functionality to query books
    def query_books_window(self):
        #Create new Toplevel window for the query
        query_window = Toplevel(self.root)
        #Window Title
        query_window.title("Query Books")

        #Label prompting the user to enter a search term
        ttk.Label(query_window, text="Enter Search Term:").pack(pady=10)
        query_entry = ttk.Entry(query_window, width=30)
        query_entry.pack(pady=5)

        #Search Books
        #Not worked on very much
        def search_books():
            #Retrieve user search query
            #Accessing query_entry to get the text entered
            search_query = query_entry.get().strip()  

            #Fetch all books from the database as dictionaries using view_all_books
            books = self.book_manager.view_all_books()

            #Open the result window
            result_window = Toplevel(self.root)
            result_window.title("Search Results")

            #Iterate through each book in the list of books (which is now a list of dictionaries)
            for book in books:
                #Check if any of the fields contain the search query (case insensitive)
                if any(search_query.lower() in str(value).lower() for value in book.values()):
                    #Display the matching book details
                    ttk.Label(result_window, text=f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Notes: {book['notes']}").pack(pady=5)

        ttk.Button(query_window, text="Search", command=search_books).pack(pady=10)

    
    #View All Books
    #Retireves all books from the database as a list of dictionaries.
    def view_all_books(self):
        with self.db.connect() as conn:
            cursor = conn.cursor()
            #Fetch all rows from the Books table
            cursor.execute("SELECT * FROM Books")
            
            #Get column names
            columns = [description[0] for description in cursor.description]
            
            #Convert each row into a dictionary using the column names
            books = [dict(zip(columns, row)) for row in cursor.fetchall()]
        #return books   
        return books

    #View All Books window
    #Creates a new window to display all the books in a tree view
    def view_all_books_window(self):
        view_window = Toplevel()
        view_window.title("All Books")
        
        #Define columns for the treeview
        columns = ('Title', 'Author', 'Pages', 'Genre', 'Year', 'ISBN', 'Status')
        
        #Create the treeview
        tree = ttk.Treeview(view_window, columns=columns, show='headings')
        
        #Define the headings for each column
        for col in columns:
            tree.heading(col, text=col, command=lambda c=col: self.sort_treeview(tree, c))
            tree.column(col, width=150, anchor="center")
        
        #Add style to make it look better
        style = ttk.Style(view_window)
        style.configure("Treeview", font=("Arial", 12), rowheight=25)
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"), foreground="pink")
        
        #Fetch the books and populate the treeview
        books = self.view_all_books()  
        for book in books:
            tree.insert('', 'end', values=(book['title'], book['author'], book['pages'],
                                          book['genre'], book['year'], book['isbn'], book['status']))
        tree.pack(pady=20, padx=20, fill="both", expand=True)
        
        #Add a scrollbar to the treeview
        scrollbar = ttk.Scrollbar(view_window, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        #Add a button to close the window
        close_button = ttk.Button(view_window, text="Close", command=view_window.destroy)
        close_button.pack(pady=10)



    #Delete Book window
    def delete_book_window(self):
        #New Toplevel(popup) window for deleting a book
        delete_window = Toplevel(self.root)
        #Window Title
        delete_window.title("Delete Book")
        #Label that prpmts the user for ISBN to delete
        ttk.Label(delete_window, text="Enter ISBN to Delete:").pack(pady=10)
        isbn_entry = ttk.Entry(delete_window, width=30)
        isbn_entry.pack(pady=5)

        #Delete Book will be triggered when user presses the 'Delete Book' button
        def delete_book():
            #Retrieve ISBN entered by user and strip.
            isbn = isbn_entry.get().strip()
            #Try to delete the book using ISBN enetered
            if self.book_manager.delete_book(isbn):
                #print success message if and close window
                messagebox.showinfo("Success", "Book deleted successfully!")
                delete_window.destroy()
            else:#Display error and close window
                messagebox.showerror("Error", "Book not found.")
                delete_window.destroy()
                
        #Button for user to initiate the book deltion process, calls delete_book
        ttk.Button(delete_window, text="Delete Book", command=delete_book).pack(pady=10)

    #Logout
    def logout(self):
        #Clear all existing widgets from the root window
        #iterate through all child widgets and detroy
        for widget in self.root.winfo_children():
            widget.destroy()

        #Call the login_screen method to display the login screen
        self.login_screen()
