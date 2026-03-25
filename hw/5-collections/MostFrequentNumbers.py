#CS2030
#Problem 14.2(Count occurences of numbers)
#Description: Write a program that reads integers and finds the one
#or ones with the most occurences and display them/it.


#function to help sort the pairs
def sortByCount(pair):
    return pair[1]

#main
def main():
    
    #Prompt the User to enter the numbers
    numbers = input("Enter the numbers: ").split()

    #Convert the input to int
    numbers = [int(num) for num in numbers]

    #Create an empty dictionary to count occurences
    numCounts = {}

    #increment through the numbers to get their count
    for number in numbers:
        
        if number in numCounts:
            #If true: Increment count by 1 (+= 1).
            numCounts[number] += 1

        else:
            #If false: Add the number to the dictionary
            #with an initial count of 1
            numCounts[number] = 1

    #Get pairs from the dictionary
    #numCounts.items() returns the dictionary’s key-value pairs as tuples
    #list( ) converts this into a list of tuples
    pairs = list(numCounts.items())
    #print(pairs)

    

    #Sort pairs by the second value using
    #the helper function to get the second value(count)
    pairs.sort(key = sortByCount, reverse = True)
    print(pairs)

    #Get the maximum count
    #Since the list is sorted, the first tuple has the highest count.
    #Accesses the count value (second element) of the first tuple
    maxCount = pairs[0][1]

    #find all numbers with the maximum occurence compared to the first one
    mostFreq = [num for num, count in pairs if count == maxCount]

    #print the results
    print("The numbers with the most occurrence are", " ".join(str(num) for num in mostFreq))

#call the main
main()
