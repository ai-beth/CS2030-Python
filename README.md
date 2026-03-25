# CS2030 - Object-Oriented Programming in Python

Coursework and projects from CS2030 at UCM, covering intermediate to advanced Python concepts with an emphasis on object-oriented design.

## Repository Structure

```
├── classes/            Classes, encapsulation, operator overloading
├── inheritance/        Inheritance, polymorphism, dynamic binding
├── data-structures/    2D lists, dictionaries, sets, matrices
├── file-io/            Reading, writing, appending files
├── regex/              Regular expressions and pattern matching
├── gui/                Tkinter widgets, events, GUI applications
├── database/           SQLite3, SQLAlchemy Core and ORM
├── web/                Web crawling, JSON, datetime, hashing
├── hw/                 Five course assignments
└── library-project/    Final project: Library Database Management System
```

## Assignments

| # | Topic | Highlights |
|---|-------|------------|
| 1 | Matrices | TicTacToe, State Capital Quiz, Heads & Tails |
| 2 | OOP | Fan, Rectangle, Stock classes |
| 3 | Banking | Account class, ATM Machine simulation |
| 4 | File I/O | File analyzer, score processor, baby name ranker |
| 5 | Collections | Vowel counter, subtraction quiz, frequency analysis |

## Final Project

A **Library Database Management System** with user authentication, book CRUD operations, and search functionality. Built with Python, Tkinter, and SQLite.

[See project details](library-project/README.md)

## How to Run

Requires **Python 3.10+**. Most examples have no external dependencies.

```bash
# Run any example from its directory
cd classes
python TestCircle.py

# Run the library project
cd library-project
python Main.py
```

For SQLAlchemy demos: `pip install sqlalchemy`
