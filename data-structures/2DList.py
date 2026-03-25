#Examples os using a 2d list
#a two dimenstional list is a list that contains other lists as its elements

#import rand int
from random import *
'''
#create an empty list
matrix = []

#prompt the user for the row index and column index
num_rows = int(input("Enter the number of rows: "))
num_columns = int(input("Enter the number of columns we want: "))


#create a for loop to initialize user input
for row in range(num_rows):
    matrix.append([]) #appending an empty new list

    for column in range(num_columns):
        #grab user input for the values in the columns
        #value = float(input("Enter an element, and press enter: "))
        #append the value to the row
        #matrix[row].append(value)

        #Instead of user input we can randomly input the values
        matrix[row].append(randint(1,90))

#display the results
print(matrix)
print()
'''
###############################################################################################


#Printing a 2D list

#create a 2d list
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]


#Nested for loop to display the list
for row in range(len(matrix1)):
    for column in range(len(matrix1[row])):
        print(matrix1[row][column], end='')
    print()
print()

#or

for row in matrix1:
    for value in row:
        print(value, end='')
    print()
print()


#or if you want to track the iteration if rows or colums
#as the value
#we can use enumerate
for i, row in enumerate(matrix1):
    for j, column in enumerate(row):
        print(f"matrix1[{i}][{j}] = {column} ", end='')
    print()
print()

#we can enumerate()with both a list and a string
list1 = ["eat","sleep","repeat"]
string1 = "Goku"

#creating enumerate objects
obj1 = enumerate(list1)
obj2 = enumerate(string1)

#display the return type and results
print("Return type:", type(obj1), type(obj2))
print(list(enumerate(list1)))
print(list(enumerate(string1,2)))

print()



######################################################################################################

##Summing all elements
#create a variable to track our total
total = 0

#nested for loop to add the element to the total
for row in matrix1:
    for value in row:
        total += value

#display the result
print(f"The total is {total}")


#finding the row with the largest sum
maxRow = sum(matrix1[0]) #gets sum of first row
index = 0

#nested for loop to find the index of the max row
for row in range(1, len(matrix1)):
    if sum(matrix1[row]) > maxRow:
        maxRow = sum(matrix1[row])
        index = row


#display the results
print(f"Row Index = {index} has the max sum of {maxRow}")

#########################################################################################################

#randomly shuffling

for row in range(len(matrix1)):
    for column in range(len(matrix1[row])):
        i = randint(0, len(matrix1) - 1)
        j = randint(0, len(matrix1[row]) - 1)

                    #swap our matrix row index and column in dex
                    ##using simultaneous assignment
        matrix1[row][column], matrix1[i][j] = matrix1[i][j], matrix1[row][column]
#display the results
print(matrix1)
print()
    
