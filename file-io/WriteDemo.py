
#import the os and sys modules
import os.path, sys

#Create a main
def main():

    #If file exists it will be destroyed/overwritten with the new text
    #Always good to check if the file exists before opening for writing
    if os.path.isfile("data/Presidents.txt"):
        #Prompt the user that the file exists
        print("data/Presidents.txt exists")

        #Prompt the user if they wan tot contine
        answer = input("File will be overwritten! Contue? (Y/N): ").upper()

        #Check the response
        if answer == 'N':
            sys.exit()

    #Open a file for output
    outputFile = open("data/Presidents.txt","w")

    #Write data to the file
    #Note: Unlike the print(str) funtion going to the next line
    #Write does not have this feature
    #You will need to use the new line character
    outputFile.write("George Washington\n")
    outputFile.write("Abe Lincoln\n")
    outputFile.write("John Adams\n")

    #Close the output file/ save the content
    outputFile.close()

#invoke the main
main()

            
    
