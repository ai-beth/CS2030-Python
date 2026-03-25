#CS2030
#HW1 Problem 8.1
#Sum elements column by column

#Define the function sumColumn that takes a matrix and column index as parameters
def sumColumn(m, columnIndex):
    #Initialize sum to 0
    sum = 0

    #For-loop to iterate through the column and add each value to sum
    for row in range(len(m)):
        sum += m[row][columnIndex]

    #Return the sum total
    return sum


#Main function
def main():
    #Initialize an empty list to store the matrix
    matrix = []

    #Read three rows of input to form the matrix (0, 1, 2)
    for i in range(3):
        #Prompt the user to input 4 values
        s = input(f"Enter a 3-by-4 matrix row {i}: ")
        items = s.split()  #Extract items from the string
        list1 = [float(x) for x in items]  #Convert items to numbers
        matrix.append(list1)  #Append the list element to the matrix

    #Display the sum of the elements in each column
    #For loop to display the sum of each of the 4 columns (0 to 3)
    for column in range(4):
        print(f"Sum of the elements at column {column} is {sumColumn(matrix, column)}")


#Call the main function
main()
