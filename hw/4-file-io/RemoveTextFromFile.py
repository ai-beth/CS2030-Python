#CS2030
#Problem 13.1 (Remove text)
#Description: Write a program that removes all the occurences of a specified
#string from a text file. Prompt the user for fileName and string to be removed. 


#Create a main function
def main():


    #Prompt the user for the text file
    fileName = input("Enter a filename: ")

    #Prompt for the search value
    removeTxt = input("Enter the string to be removed: ")

    #Open the file and read its contents
    file = open(fileName, "r")

    #Create an object to store the contents of the file
    contents = file.read()
    
    #close the file
    file.close()

    #Replace all occurences of the specified string with an empty string
    newContents = contents.replace(removeTxt, "")

    #open the file to be written with the updated data
    file = open(fileName, "w")

    #Write the new contents to the file
    file.write(newContents)

    #Close the file
    file.close()

    #Display tha the process is done
    print("Done")


#Call the main
main()
