#Description: Using Tkinter to reverse a string

#Import Tkinter
from tkinter import *

#Create a class to reverse the text
class TextReverser:

    #Create Initializer method
    def __init__(self):

        #Establish a window
        window = Tk()
        window.title("Reverse")

        #Create widgets for the window
        self.visibleMessage = StringVar() #Object Type
        #We call set to give the string an initial value
        self.visibleMessage.set("Hello...Its me!")
        #Create a label widget through the textvariable parameter
        #we are connecting our message to the label
        #The first parmeter is the window variable. This assigns the
        #window as the parent
        #Note: This does not assign where they are displayed
        textLabel = Label(window, textvariable = self.visibleMessage,
                          font=("Arial",32))

        #Reverse text checkbox widget
        #IntVar Object to track the state that it is in
        self.reverseState = IntVar()
        #Create a checkbutton widget
        reverseButton =  Checkbutton(window, text = "Reverse Text",
                                     font=("Arial",24),
                                     variable = self.reverseState,
                                     command = self.updateText)

        #Add controls in order to the window
        textLabel.pack()
        reverseButton.pack()

        #Create an event loop
        window.mainloop()

    #Method for updating the text
    def updateText(self):
        if (self.reverseState.get() == 1):
            self.visibleMessage.set("!em stI...olleH")
        else:
            self.visibleMessage.set("Hello...Its me!")

#Create GUI by calling constructor
TextReverser()










        













        











        
