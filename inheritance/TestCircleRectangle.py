#Import Circle and Rectangle Subclasses
from CircleSub import Circle
from RectangleSub import Rectangle

#Create a main function
def main():

    #Create a Circle with radius 1.5
    circle = Circle(1.5)
    #Display the circle Objects information
    print(f"A circle {circle}") #Invoke the __str__() method
    print(f"The radius is {circle.getRadius()}")
    print(f"The area is {circle.getArea()}")
    print(f"The diameter is {circle.getDiameter()}")
    print(f"{circle.printCircle()}")
    print(f"{circle.__str__()}")

    #Create a rectangle with a width of 2 and height of 4
    rectangle = Rectangle(2,4)
    print(f"A rectangle {rectangle}")
    print(f"{rectangle.__str__()}")
    print(f"The area is {rectangle.getArea()}")
    print(f"The perimeter is {rectangle.getPerimeter()}")

#Invoke the main function
main()
