#CS2030
#HW1 Problem 8.11
#Game: Nine Heads and Tails

'''
1. The user inputs a number between 0 and 511.
2. Convert this number to its 9-bit binary form.
3. Map the 0s to 'H' and 1s to 'T'.
4. Format the binary result as a 3x3 matrix and print it.
'''

#Function to convert a number to a 3x3 matrix of H(heads) and T(tails)
def displayMatrix(number):

    #Convert the number to a binary string of 9
    bString = format(number, '09b')
    
    #Initialize an empty matrix
    matrix = []
    
    #Map each binary digit to H or T and add to the matrix
    #Loop through the binary string in steps of 3
    for i in range(0, 9, 3):  
        
        #Initialize an empty row
        row = []  

        #Loop through each group of 3 bits
        for bit in bString[i:i+3]: 

            #If the bit is 0, it's heads(H)
            if bit == '0':  
                row.append('H')

            #Otherwise, it's tails(T)
            else:  
                row.append('T')

        #Add the row to the matrix
        matrix.append(row)  

    #Display the matrix
    for row in matrix:
        print(' '.join(row))

#Main function to prompt user input
def main():
    #Prompt the user for a number between 0 and 511
    number = int(input("Enter a number between 0 and 511: "))
    displayMatrix(number)

#Call the main
main()
