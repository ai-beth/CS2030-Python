#Description: Grid Demo 2.0 / with image

#Import tkinter
from tkinter import *

#Create window / root
root = Tk()
root.title("Student Info")
root.geometry("500x300")
root.maxsize(500,300) #Height and width
root.config(bg="lightgrey")

#Profile picute
image = PhotoImage(file="michaelMinzey.png")
img = Label(root, image=image)
img.grid(row=0,column=0,rowspan=6,padx=5,pady=5)

#Enter specific information fo your profile
enter_info = Label(root, text="Please enter your information: ", bg="lightgrey")
enter_info.grid(row=0, column=1, columnspan=5,padx=5,pady=5)

#Name label and entry widgets
Label(root, text="Name", bg="lightgrey").grid(row=1,column=1,
                                              padx=5,pady=5,sticky=E)

name = Entry(root, bd=4)
name.grid(row=1,column=2,padx=5,pady=5)

#Gender label and dropdown widgets
gender = Menubutton(root, text="Gender")
gender.grid(row=2,column=2,padx=5,pady=5,sticky=W)
gender.menu = Menu(gender, tearoff=0)
gender["menu"] = gender.menu

#Choices in the dropdown
gender.menu.add_cascade(label="Male")
gender.menu.add_cascade(label="Female")
gender.menu.add_cascade(label="Other")

#Major label and dropdown widgets
major = Menubutton(root, text="Majors")
major.grid(row=3,column=2,padx=5,pady=5,sticky=W)
major.menu = Menu(major, tearoff=0)
major["menu"] = major.menu

#Major Choices
major.menu.add_cascade(label = "Computer Science")
major.menu.add_cascade(label = "Cybersecurity")
major.menu.add_cascade(label = "Data Science")
major.menu.add_cascade(label = "Software Engineering")

#Start the event listener
root.mainloop()



































