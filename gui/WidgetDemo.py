#Import tkinter
from tkinter import *

#Create a class for the widget demo
class WidgetDemo:

    #Create the initializer method
    def __init__(self):

        window = Tk() #Creates a window
        window.title("Widgets Demo") #Sets the title

        #Add a button, a check button, and a radio button to frame1
        frame1 = Frame(window) #Create and add a frame to window
        frame1.pack()

        self.v1 = IntVar() #Bound with cbtBold
        cbtBold = Checkbutton(frame1, text = "Bold",
                              variable = self.v1, command = self.processCheckbutton)

        self.v2 = IntVar() #Bound with the rbRed
        rbRed = Radiobutton(frame1, text = "Red", bg = "red",
                           variable = self.v2, value = 1,
                           command = self.processRadiobutton)

        rbYellow = Radiobutton(frame1, text = "Yellow", bg = "yellow",
                               variable = self.v2, value = 2,
                               command = self.processRadiobutton)

        #The grid (geometry manager) is used to place the checkbox
        #and radio buttons into frame1
        #THese three widgets are placed in the same row and in
        #different columns
        cbtBold.grid(row = 1, column = 1)
        rbRed.grid(row = 2, column = 1)
        rbYellow.grid(row = 3, column = 1)

        #Add a button, a check button, and a radio button to frame2
        frame2 = Frame(window)
        frame2.pack()

        #Create a label
        label = Label(frame2, text = "Enter your name: ")
        self.name = StringVar()
        entryName = Entry(frame2, textvariable = self.name)

        #Create a button
        btGetName = Button(frame2, text = "Get Name",
                           command = self.processButton)

        #Create a message
        message = Message(frame2, text = "It is a widgets demo")

        #Using the grid manager place the widgets
        label.grid(row = 1, column = 1)
        entryName.grid(row = 1, column = 2)
        btGetName.grid(row = 1, column = 3)
        message.grid(row = 1, column = 4)

        #Add a textbox area
        text = Text(window)
        text.pack()
        text.insert(END,"Tip\nThe best way to learn Tkinter is to read")
        text.insert(END,"These carefully designed examples and use them")
        text.insert(END,"to create your applications.")

        #Create an event loop
        window.mainloop()


    #Method for checking the checkbox
    def processCheckbutton(self):
        print("Check button is " +
              ("checked " if self.v1.get() == 1 else "unchecked"))

    #Method for checking the radio button
    def processRadiobutton(self):
        print(("Red" if self.v2.get() == 1 else "Yellow") +
              " is selected")

    #Method for clicking the button
    def processButton(self):
        print(f"Your name is {self.name.get()}")

#Create the GUI
WidgetDemo()












        













        









                           











        
