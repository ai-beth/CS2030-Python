#Description: Counting each letter in a file

#Create a main function
def main():

    while True:
        #Try Block to test the code
        try:

            #Prompt the user to input a filename
            filename = input("Enter a filename: ").strip()

            #Open the file to read
            inputFile = open(filename, "r")

            #Break the loop
            break

        except IOError:
            print(f"File {filename} does not exist. Try again!")

    #Create a list of 26 indices intilizing all index to 0
    counts = 26 * [0]

    #Read each line from the file as a string
    for line in inputFile:
        #Convert the letters to lowercase and pass them
        #to invoke countLetters function
        countLetters(line.lower(), counts)

    #Display the results
    for i in range(len(counts)):
        if counts[i] != 0:
            print(chr(ord('a') + i) + " appears " + str(counts[i]) +
                  (" time" if counts[i] == 1 else " times"))

    #Close the file
    inputFile.close()


#Build the countLetter function
def countLetters(line, counts):
    for ch in line:
        #Test if the character is a letter
        if ch.isalpha():
            #Increment the letter count
            counts[ord(ch) - ord('a')] += 1

#Invoke the main function
main()



















            
