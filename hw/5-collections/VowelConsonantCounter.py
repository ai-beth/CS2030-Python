#CS2030
#Problem 14.11 (Count consonants and vowels)
#Description: Write a program that prompts the user to enter a text filename
#and displays the number of vowels and consonants in the file
#Use a set to store the vowels A,E,I,O,U


def countVowelsConsonants(filename):
    #Define the set of vowels
    vowels = {'A', 'E', 'I', 'O', 'U'}

    #initialize counts to 0
    vowelCount = 0
    consonantCount = 0

    #try block to catch file not found error
    try:
        with open(filename, 'r') as file:
            #Read the file content
            text = file.read()

            #Iterate through each character in the text
            for char in text:
                #Check if the character is alphabetic
                if char.isalpha():
                    #Convert character to uppercase for case insensitivity
                    char = char.upper()

                    #Count vowels and consonants
                    if char in vowels:
                        vowelCount += 1
                    else:
                        consonantCount += 1

        #Return the counts
        return vowelCount, consonantCount
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None

    
#Create the main
def main():
    
    #Prompt the user to enter the filename
    filename = input("Enter a text filename: ")

    result = countVowelsConsonants(filename)

    if result is None:
        vowels, consonants = 'no', 'no' 
    else:
        vowels, consonants = result

    
    print(f"There are {vowels} vowels, and {consonants} consonants.")

#call the main
main()
