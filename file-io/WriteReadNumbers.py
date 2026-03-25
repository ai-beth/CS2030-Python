#To write numbers to a file you must first convert them into a string
#and use the write methos to write them to the file

#import random module
from random import randint

#Create the main
def main():

    #open a file for writing data
    outputFile = open("data/Numbers.txt","w")

    #create a for loop to iterate 10 times
    for i in range(10):
        #write a random number 1 - 50 with each iteration
        #separate the numbers with whitespace
        outputFile.write(str(randint(0,50)) + " ")

    #Close the file to save th data to it
    outputFile.close()
                     


    #open the file for reading
    inputFile = open("data/Numbers.txt","r")

    #read all data to a string
    s = inputFile.read()

    #combine list comprehension with the splitmethod()(Str)
    numbers = [int(x) for x in s.split()]

    #Display each element in the list
    for number in numbers:
        print(number,end=' ')

    #Close the file
    inputFile.close()

                         

#invoke the main
main()
