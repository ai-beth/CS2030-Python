#Import Tkinter
from tkinter import *

#Create a class for processing the button clicks
class ProcessButtonEvent:

    #Create a Initializer method
    def __init__(self):
        #Create the window
        window = Tk()

        #Create the button
        btOK = Button(window, text = "OK", fg = "red",
                      command = self.processOK)

        btCancel = Button(window, text = "Cancel", bg = "yellow",
                          command = self.processCancel)

        #Display the buttons
        btOK.pack()
        btCancel.pack()

        #Create an event loop
        window.mainloop()

    #Methods for pressing OK and Cancel
    def processOK(self):
        print("OK button is clicked")

    def processCancel(self):
        print("Cancel button is clicked")

#Create an object
ProcessButtonEvent()








        
