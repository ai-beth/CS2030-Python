#CS2030
#Problem 13.2(Count characters, words, and lines in a file)
#Description: Write a program that will count the number of characters,
#words, and lines in a file.
#Words are separated by whitespace characters.


#Create teh main
def main():
    
    #Prompt the user to enter a filename
    fileName = input("Enter a filename: ")

    #Open the file and read its contents
    file = open(fileName, "r")
    contents = file.read()
    file.close()

    #Count the number of characters
    numChars = len(contents)

    #Count the number of words
    words = contents.split()
    numWords = len(words)

    #Count the number of lines
    lines = contents.splitlines()
    numLines = len(lines)

    #Display the results
    print(f"{numChars} characters")
    print(f"{numWords} words")
    print(f"{numLines} lines")

#Call the main function
main()
