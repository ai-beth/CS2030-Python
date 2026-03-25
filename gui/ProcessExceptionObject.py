'''
Processing Exceptions using exception Objects

You can access an exception object in the except class

To throw an exception:
First you create an exception object.
Second you use the raise keyword to throw it.
'''
#Try Block
try:
    #Prompt the user to input a floating point value
    number = float(input("Enter a number: "))

    #Display the results
    print(f"The number entered is {number}")

except ValueError as ex:
    #ValueError is the object that we assigned to ex
    #The __str__() method in ex is invoked to return a string
    #that describes the exception
    print("Exception:", ex)
