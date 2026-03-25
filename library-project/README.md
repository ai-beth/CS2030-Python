# Library Database Management System

A desktop application for managing a personal book library, built as the final project for CS2030 at UCM.

## Features

- **User Authentication** - Create accounts with validated usernames and hashed passwords (SHA-256)
- **Add Books** - Store books with ISBN, title, author, genre, year, page count, reading status, and notes
- **View All Books** - Sortable table view using Tkinter TreeView
- **Search & Query** - Find books by any field
- **Modify Books** - Update any book's details through a dynamic form
- **Delete Books** - Remove books from the library

## Tech Stack

- **Python 3** - Core language
- **Tkinter** - GUI framework
- **SQLite3** - Database (created automatically on first run)

## How to Run

```bash
python Main.py
```

The application will create a `Library.db` file on first launch. No additional dependencies required.

## Project Structure

| File | Purpose |
|------|---------|
| `Main.py` | Entry point - initializes database and launches UI |
| `DBManager.py` | Database connection and table creation (Users, Books) |
| `UI.py` | Full Tkinter interface - login, menus, all book management screens |
| `BookManager.py` | CRUD operations for the Books table |
| `UserManager.py` | User registration, login validation, password hashing |
| `rules.txt` | Username and password validation rules |

## Password Requirements

- Must start with a special character
- Must contain at least one digit, one lowercase letter, and one uppercase letter
- Must be 6-12 characters long

## Username Requirements

- Must start with a capital letter
- Must be 3-6 characters long
