'''
Write a function that sums all the numbers of the major diagnol
n x n of integers using hte following header

def sumMajorDiagonal(n)

Note: major diagonal is a diagonal that runs from the top left to the bottom right

find the sum of all elements
'''

#create a main
def main():

    #create an empty list
    matrix = []

    #for loop for building and filling the matrix 4x4
    #each iteration creates a list element for matrix
    for i in range(4):
        #Prompt the user to input 4 values
        s = input(f"Enter a 4-by-4 matrix row [i+1]: ")
        items = s.split() #extracts items from the string
        list1 = [float(x) for x in items] #will convert items to numbers
        matrix.append(list1) #appending the list element to our matrix

    #display the results and pass the 2d list to find the sum of majr diag
    print(f"Sum of all elements in the major diagonal is {sumMajorDiagonal(matrix)})")


#create the function for summing our major diagonal
def sumMajorDiagonal(m):
    #track the sum
    sum = 0
    #use a for loop to iterate through each row
    for i in range(len(m)):
        #adding hhe value of the location of m row index[column index}
        #first iteration 0,0 | 1,1
        sum += m[i][i]

    #return the sum back to the caller
    return sum


#invoke the main
main()



