#Description: Examples of using a 2D list
#A two dimensional list is a list that contains other
#lists as its elements

#import the random module
from random import *
'''
#Create an empty list
matrix = []

#Prompt the user for the rowIndex and the columnIndex
num_rows = int(input("Enter the number of rows: "))
num_columns = int(input("Enter the number of columns: "))

#For loop initialize the matrix with user input
for row in range(num_rows):
    matrix.append([]) #appending an empty new list

    for column in range(num_columns):
        #Grab user input for the values in the columns
        #value = float(input("Enter an element and press enter: "))
        #append the value to the current row
        #matrix[row].append(value)

        #Instead of user input we can randomly input values
        matrix[row].append(randint(1,99))

#Display the matrix result
print(matrix)
print()
'''
####################################################################
#Printing a 2D List

#Create a 2D List
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]

#Nested for loop to display the 2d list
for row in range(len(matrix1)):
    for column in range(len(matrix1[row])):
        print(matrix1[row][column], end = '')
    print()
print()

#or

for row in matrix1:
    for value in row:
        print(value, end = '')
    print()
print()

#or if you want to track the iteration or rows and columns as well
#as the value
#We can use enumerate(iterable,start = 0)
for i,row in enumerate(matrix1):
    for j,column in enumerate(row):
        print(f"matrix1[{i}][{j}] = {column}", end = ' ')
    print()
print()

#We can use enumerate() with both a list and a string
list1 = ["eat","sleep","repeat"]
string1 = "Goku"

#Creating enumerate objects
obj1 = enumerate(list1)
obj2 = enumerate(string1)

#Display the reutrn type and results
print("Return type:", type(obj1),type(obj2))
print(list(enumerate(list1)))
print(list(enumerate(string1,2)))
print()
####################################################################
#Summing all elements
#Create a total variable
total = 0

#Nested for loop to add the element to the total
for row in matrix1:
    for value in row:
        total += value

#Display the total result
print(f"The total is {total}")
print()

#Finding the row with the largest sum
maxRow = sum(matrix1[0]) #Gets the sum of the first row
index = 0

#Nested for loop to find the index of the max row
for row in range(1, len(matrix1)):
    if sum(matrix1[row]) > maxRow:
        maxRow = sum(matrix1[row])
        index = row

#Display the results
print(f"Row Index = {index} has the max sum of {maxRow}")
print()
####################################################################
#Randomly shuffling

#Nested for loop to shuffle elements
for row in range(len(matrix1)):
    for column in range(len(matrix1[row])):
        i = randint(0,len(matrix1) - 1)
        j = randint(0,len(matrix1[row]) - 1)

        #Swap matrix row index and column S.A
        matrix1[row][column], matrix1[i][j] = \
                              matrix1[i][j],matrix1[row][column]

print(matrix1)
print()
#####################################################################
#Sorting a 2D list
points = [[4,2],[26,4],[7,9],[22,57],[77,32],[11,18],[1,3], [4,3]]

#Sorts the rows on their first element
#For rows with the same first element they are sorted on the second
#element and so on and so fourth
points.sort()

#Display the sorted 2d list
print(points)

























































































































        
        
