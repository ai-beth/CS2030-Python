#Grid manager places our widgets into the cells of an invisible grid
#in a container
#You can place a widget in a specified row and column

#Import Tkinter
from tkinter import *

#Create the window
window = Tk()
window.title("Practice with grid")
window.geometry("210x180") #sets the strating size of the window

#Create a label
label = Label(window, text="Which colors do you like below?")
label.grid(row = 0)

#Create variables and check buttons for diff colors
red_var = IntVar()
Checkbutton(window, width = 10, text="red",variable=red_var, bg="red"
            ).grid(row=1)

yellow_var = IntVar()
Checkbutton(window, width = 10, text="yellow",variable=yellow_var, bg="yellow"
            ).grid(row=2)

green_var = IntVar()
Checkbutton(window, width = 10, text="green",variable=green_var, bg="green"
            ).grid(row=3)

blue_var = IntVar()
Checkbutton(window, width = 10, text="blue",variable=blue_var, bg="blue"
            ).grid(row=4)


def display_checked():
    #If the check buttons have been toggled, and we display
    #The value 1, if not checked we display 0
    red = red_var.get()
    yellow = yellow_var.get()
    green = green_var.get()
    blue = blue_var.get()

    print(f"red: {red}\nyellow: {yellow}\ngreen: {green}\nblue: {blue}")


#create a button to check and another to close
Button(window, text="Tally", command=display_checked).grid(row=5)
Button(window, text="End", command=dwindow.quit).grid(row=6)

window.mainloop()




          
