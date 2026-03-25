#CS2030
#Problem 13.3 (Process scores in a text file)
#Write a program that prompts the user to enter the filename 
#and reads the scores from the file.
#The program displays the total and average of the scores.
#Scores are separated by blanks.

#Create the main
def main():

    #Prompt the user to enter a filename
    file_name = input("Enter a filename: ")

    #Open the file and read its contents
    file = open(file_name, "r")
    contents = file.read()
    file.close()

    #Convert the scores from strings to integers
    scores = list(map(int, contents.split()))

    #Calculate the total and average
    total = sum(scores)
    count = len(scores)
    average = total / count if count > 0 else 0

    #Display the results
    print(f"There are {count} scores")
    print(f"The total is {total}")
    print(f"The average is {average:.2f}")

#Call the main
main()
