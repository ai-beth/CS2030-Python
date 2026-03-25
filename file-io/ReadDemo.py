#Invoking readline or read returns an empty string at the end of the file

#Create a main
def main():

    #Open a file for input
    inputFile = open("data/Presidents.txt","r")

    #Display read() method which reads all characters from the file
    #and returns them as a string
    print(f"1. Using read(): \n{inputFile.read()}")

    #Close the input file
    inputFile.close()
    #########################################################################

    inputFile = open("data/Presidents.txt","r")

    #Display read and give it a number to read the specified number of characters
    print("\n2. Using read(number): ")

    #read fofur characters
    s1 = inputFile.read(4)
    print(s1)

    #read 15 characters
    s2 =inputFile.read(15)
    print(s2)

    #The repr funtion returns a raw string for s2
    #Which causes the escape sequence to be siplayed as liters
    print(repr(s2))

    #close the input file
    inputFile.close()


     #########################################################################

    #readline() which reads a line that ends with a newline
    #open a file for input
    inputFile = open("data/Presidents.txt","r")

    print("\n3. Using readline(): ")
    line1 = inputFile.readline()
    line2 = inputFile.readline()
    line3 = inputFile.readline()
    line4 = inputFile.readline()

    print(line1)
    print(line2)
    print(line3)
    print(line4)

    print(repr(line1))
    print(repr(line2))
    print(repr(line3))
    print(repr(line4))

    #Close the inputfile
    inputFile.close()


     #########################################################################
    #readlines() reads all lines and returns a list of strings
    #open file for input
    inputFile = open("data/Presidents.txt","r")
    print("\n4. Using readlines(): ")
    #print(inputFile.readlines())
    print()

    lines = inputFile.readlines()
    lines = [line.rstrip('\n') for line in lines]
    print(lines)

    #close the input file
    inputFile.close()


#Invoke the main()
main()




