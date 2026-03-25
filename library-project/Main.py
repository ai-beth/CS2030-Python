#Main
#Imports
from tkinter import Tk
from UI import UIManager
from DBManager import Database


#Main
def main():
    
    #Initialize the database
    db = Database()
    db.initialize()

    #Start the Tkinter app
    root = Tk()
    app = UIManager(root, db)
    root.mainloop()
    
#call the main
main()

