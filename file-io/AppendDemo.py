#We can use "a" mode to open a file for appending data

#Create a main
def main():

    #open a file fo rappending data
    outputFile = open("data/Info.txt","a")

    outputFile.write("Hello, World!")
    outputFile.close()

#Invoke the main
main()
