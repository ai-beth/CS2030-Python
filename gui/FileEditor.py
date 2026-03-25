#Description: Create a file editor to open and save files

#Import tkinter and tkinter filediaglog
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

#Create the File Editor class
class FileEditor:

    #Initializer method
    def __init__(self):

        #Create the window
        window = Tk()
        window.title("Text Editor")

        #Create a menu bar
        menubar = Menu(window)
        window.config(menu = menubar) #Display the bar

        #Create a pulldown menu
        operationMenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "File", menu = operationMenu)
        operationMenu.add_command(label = "Open", command = self.openFile)
        operationMenu.add_command(label = "Save As", command = self.saveFile)
        operationMenu.add_separator()
        operationMenu.add_command(label = "Exit", command = window.destroy)

        #Create a pulldown menu
        edit = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "Edit", menu = edit)
        edit.add_command(label = "Edit")

        #Add a tool bar frame
        frame0 = Frame(window)
        frame0.grid(row = 1, column = 1, sticky = W)

        #Add images to the frame
        openImage = PhotoImage(file = "open.gif")
        saveImage = PhotoImage(file = "save.gif")

        #Create the folder and the save drive image button
        Button(frame0, image = openImage, command = self.openFile
               ).grid(row = 1, column = 1, sticky = W)
        Button(frame0, image = saveImage, command = self.saveFile
               ).grid(row = 1, column = 2)

        #Create a frame
        frame1 = Frame(window)
        frame1.grid(row = 2, column = 1)

        #Add a scrollbar to the frame
        scrollbar = Scrollbar(frame1)
        scrollbar.pack(side = RIGHT, fill = Y)

        #Adding the textbox
        self.text = Text(frame1, width = 40, height = 20,
                         wrap = WORD, yscrollcommand = scrollbar.set)
        self.text.pack()
        scrollbar.config(command = self.text.yview)

        #Create the event listener
        window.mainloop()

    #Create the method for opening a file
    def openFile(self):
        filenameforReading = askopenfilename()
        inputFile = open(filenameforReading, "r")
        self.text.insert(END, inputFile.read())
        inputFile.close()

    #Create the method for saveing a file
    def saveFile(self):
        filenameforWriting = asksaveasfilename()
        outputFile = open(filenameforWriting, "w")
        outputFile.write(self.text.get(1.0,END))
        outputFile.close()

#Create the FileEditor GUI
FileEditor()





        






        













        










        
