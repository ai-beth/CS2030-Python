#Description: Handling the event listener

#Import tkinter module
from tkinter import *

#Callback function (Handlers) for clicking ok
#A function that is invoke when a binding event occurs
def processOK():
    print("OK button is clicked")

#Callback function (Handlers) for click cancel
def processCancel():
    print("Cancel button is clicked")

#Callback function (Handlers) for printing a messages
def printSelected():
    #Change the label text to which one we select
    if (var1.get() == 1) and (var2.get() == 0):
        label.config(text = "PYTHON IS BETTER!")

    elif (var1.get() == 0) and (var2.get() == 1):
        label.config(text = "JAVA IS BETTER!")

    elif (var1.get() == 0) and (var2.get() == 0):
        label.config(text = "I don't like either")

    else:
        label.config(text = "Both are great!")

#Create a root window
window = Tk()

#SEt the title for the window
window.title("The Title Area")

#Create a Label
label = Label(window, text = "empty")
label.pack()
label["font"] = "Arial 22 bold underline"

#Checkbox widget
var1 = IntVar() #set() and get() methods are used to set and retrieve values
var2 = IntVar()
button1 = Checkbutton(window, text = "Python",
                      variable = var1,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10,
                      command = printSelected)

button2 = Checkbutton(window, text = "Java",
                      variable = var2,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10,
                      command = printSelected)

#Display both checkbuttons
button1.pack()
button2.pack()

#Invoke processOK when OK button is clicked
#The fg option specifies the buttons foreground color
#fg default color is black
#The bg option specifiies the buttons background color
#bg default color is grey
btOK = Button(window, text = "OK", fg = "white", bg = "red",
              command = processOK)
btOK["font"] = "Arial 15 bold"
btOK["bg"] = "blue"
btOK["fg"] = "#66FFFF"
btOK["curso"] = "circle"
btOK["justify"] = "left"

#Invoke the processCancel when the cancel button is clicked
btCancel = Button(window, text = "Cancel", fg = "yellow", bg = "purple",
                  command = processCancel)
btCancel["font"] = "Arial 15 bold"

#Display the OK and Cancel buttons
btOK.pack()
btCancel.pack()

#Create a text box
text = Text(window)
text.pack()
text.insert(END, "Tip\nThe best way to learn Tkinter is to read")
text.insert(END, " these examples will help create your applications")

#Create an event loop
window.mainloop()











































































