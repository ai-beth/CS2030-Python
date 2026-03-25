#tkinter module contains the classes for creating GUI'S
#The TK class creates a window for holding GUI Widgets

#Import the tkinter module
from tkinter import *

#Create a root window
window = Tk() #Instance of a window

#Create a label
#Label is part of the widget class for creating a label
label = Label(window, text = "Welcome to Python")

#Create a button
#Button is part of the widget class for creating a button
button = Button(window, text = "Click Me")

#Display the Label in the window
#pack manager packs the widget in the window row by row
label.pack()

#Display the button in the window
button.pack()

#Tkinter GUI program listens and processes events in a
#continuous loop. (Mouse Clicks / Key Presses)
#Stops when you close the main window
window.mainloop()











