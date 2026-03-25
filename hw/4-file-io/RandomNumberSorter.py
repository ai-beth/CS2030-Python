#CS2030
#Problem 13.4

#import the random module
import random

#import os to check for the file existence
import os  


#Create the main
def main():

    #Prompt the user for the fileName
    filename = input("Enter a filename: ")

    #Check if the file already exists and exit the function if the file exists
    if os.path.exists(filename):
        print("Error: The file already exists.")
        return  

    #Generate 100 random integers
    numbers = [random.randint(1, 1000) for i in range(100)]

    #Write numbers to the file, separated by spaces
    file = open(filename, "w")
    file.write(" ".join(map(str, numbers)))
    file.close()

    #Read the file content back and convert it to a list of integers
    file = open(filename, "r")
    data = file.read().strip().split()
    numbers = list(map(int, data))
    file.close()

    #Sort the numbers and display them
    numbers.sort()
    print("Sorted numbers:", " ".join(map(str, numbers)))

#call the main
main()
