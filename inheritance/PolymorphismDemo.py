#Import the circle and rectangle class
from CircleSub import Circle
from RectangleSub import Rectangle

#Create the main function
def main():

    #Create a circle and rectangle object
    c = Circle(4)
    r = Rectangle(1,3)

    #INvoke the display object function
    print("\nCircle...") #isinstance example
    displayObject(c)

    print("\nRectangle...") #isinstance example
    displayObject(r)

    #Display results / invoke the isSameArea function
    print(f"Are the circle and rectangle the same size? \
{isSameArea(c,r)}")
'''
#Create function to display geometric object properties
def displayObject(g):
    print(g.__str__())

    #Note: You can invoke displayObject with any object since
    #the __str__() method is defind in the Object Class
    #Example of polymorphism
'''

#Isinstance Example
#isinstance is a built-in function
#Determinew whether an object is an instance of a class
#Display the geometric object properties
def displayObject(g):
    print(f"Area is {g.getArea()}")
    print(f"Perimeter is {g.getPerimeter()}")

    #Test if g is an instance of circle
    if isinstance(g,Circle):
        print(f"Diameter is {g.getDiameter()}")

    elif isinstance(g,Rectangle):
        print(f"Width is {g.getWidth()}")
        print(f"Height is {g.getHeight()}")

#Compare the areas of two geometric objects
def isSameArea(g1,g2):
    #Return True if g1 and g2 have the same area
    return g1.getArea().__eq__(g2.getArea())

    #Another example of Polymorphism: You can invoke the isSame
    #Area function with any objects g1 and g2 as long as the
    #object has the getArea method

#invoke main
main()












    
