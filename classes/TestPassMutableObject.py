#Description: Mutable vs immutable ojects

#Import the Circle
from Circle import Circle

#Create the main function
def main():
    #Create a Circle Object with radius 1
    myCircle = Circle() #Mutable Object

    #Display areas for radius 1 - 5
    n = 5 #Immutable Object

    #Invoke the printArea function
    printAreas(myCircle,n)

    #Display myCircle radius and times
    print(f"\nRadius is {myCircle.radius}")
    print(f"n is {n}")

#Create a function to print a table of areas for the
#given radius
def printAreas(c,times):
    #Display a header
    print(f"{'Radius':10s}{'Area'}")

    #while loop to iterate through the different radius
    while times >= 1:
        #Display object and its area
        print(f"{c.radius:<10d}{c.getArea():<.3f}")

        c.radius += 1 #Increment radius
        times -= 1 #Decrement times

#Invoke the main function
main()


    
















    
