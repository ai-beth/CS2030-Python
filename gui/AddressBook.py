






#Create an address book
#We will use object input/output for storing an viewing an address book

#import pickle, os.path, tkinter
import pickle, os.path, tkinter.messagebox
from tkinter import *


#Define a class named address
class Address:

    #Create initlizer that create address object with a
    #name, stree, city state, and zi
    def __init__(self, name, stree, city, state, zip):
        self.name =name
        self.street=street
        self.city= city
        self.state = state
        self.zip = zip

#Define another class called Address Book
class AddressBook:

    #initilizer method that create the user interface for displaying and
    #processing address

    def __init__(self):
        window = tk() #Creates the window
        window.title("Address Book")

        #Variables to store user input
        self.nameVar = StringVar()
        self.streetVar = StringVar()
        self.cityVar = StringVar()
        self.stateVar = StringVar()
        self.zipVar = StringVar()

        #Create a frame to house the name label and entry
        frame1 = Frame(window)
        frame1.pack() #place into the window
        Label(frame1, text = "Name").grid(row = 1, column = 1, sticky = W)
        Entry(frame1, textvariable = self.nameVar, width = 40).grid(
            row = 1, column = 2)

        #Create a fram to house the street label and entry
        frame2 = Frame(window)
        frame2.pack()
        Label(frame2, text = "Street").grid(row = 1, column = 1, sticky = W)
        Entry(frame2, textvariable = self.streetVar, width = 40).grid(
            row = 1, column = 2)

        #Create a fram e to house the city state and zip labels and sntries
        frame3 = Frame(window)
        frame3.pack()
        Label(frame3, text = "City", width = 5).grid(
            row = 1, column = 1, sticky = W)
        Entry(frame3, textvariable = self.cityvar).grid(row = 1, column = 2)
        
        Label(frame3, text = "State").grid(row = 1, column = 3, sticky = W)
        Entry(frame3, textvariable = self.stateVar, width = 5).grid(
            row = 1, column = 4)

        Label(frame3, text = "Zip").grid(row = 1, column = 5, sticky = W)
        Entry(frame3, textvariable = self.zipVar, width = 5).grid(
            row = 1, column = 6)


        #Create a frame to house our action buttons
        frame4 = Frame(window)
        frame4.pack()

        #Add button
        Button(frame4, text = "Add", command = self.processAdd).grid(
            row = 1, column = 1)

        btFirst = Button(frame4, text = "First", command = self.proccessFirst).grid(row = 1, column = 2)

        btNext = Button(frame4, text = "Next", command = self.processNext).grid(
            row = 1, column = 3)

        btPrevious = Button(frame4, text = "Previous", command = self.processPrevious).grid(
            row = 1, column = 4)

        btLast = Button(frame4, text = "Last", command = self.processLast).grid(
            row = 1, column = 5)


        self.addressList = self.loadAddress()
        self.current = 0

        if len(self.addressList) > 0:
            self.setAddress()

        window.mainloop()

        #Method will write the address list to the file
        #Will also display a message dialogue box to alert he user
        #That a new address has been added
        def saveAddress(self):

            #open/create a file to write to binary
            outputFile = open("address.dat", "wb")

            #Dump the address list ot ehte file
            pickle.dump(self.addressList, outputFile)

            #Display the success message
            tkinter.messagebox.showinfor("Address Saved", "A new address is saved")

            outputFile.close()

            #MEthod tha treads the address list ot he file
            #If the file does not exist, our program returns an empty list
            def loadAddress(self):
                #Check if our file exists
                if not os.path.isfile("address.dat"):
                    return[]


        
