#Description: Randomly show 4 cards

#Import tkinter and random module
from tkinter import *
import random

#Create a class
class DeckOfCardsGUI:
    #Create the initializer method
    def __init__(self):
        #Create the window
        window = Tk()
        window.title("Pick Four Cards Randomly")

        #Store images for cards
        self.imageList = []

        #Append the image to imageList
        for i in range(1,55):
            self.imageList.append(PhotoImage(file="card/" + str(i) + ".gif"))

        #Create a frame to hold four labels
        frame = Frame(window)
        frame.pack()

        #A list of four labels
        self.labelList = []
        for i in range(4):
            self.labelList.append(Label(frame, image = self.imageList[i]))
            self.labelList[i].pack(side = LEFT)

        Button(window, text = "Shuffle", command = self.shuffle).pack()

        #Create a event loop listener
        window.mainloop()

    #Choose four random cards
    def shuffle(self):
        random.shuffle(self.imageList)
        for i in range(4):
            self.labelList[i]["image"] = self.imageList[i]

#Create GUI
DeckOfCardsGUI()








        











            
