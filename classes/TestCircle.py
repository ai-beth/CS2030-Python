#Import Circle class
from Circle import Circle

#Create main function
def main():

    #Create a circle with radius 1
    circle1 = Circle()
    print(f"The area of the circle of radius {circle1.radius} is \
{circle1.getArea():.2f}\n")

    #Create a circle with radius 25
    circle2 = Circle(25)
    print(f"The area of the circle of radius {circle2.radius} is \
{circle2.getArea():.3f}\n")

    #Create a circle with radius 125
    circle3 = Circle(125)
    print(f"The perimeter is {circle3.getPerimeter():.3f}")
    print(f"The area is {circle3.getArea():.3f}")

    #You can create an object without explicitly assigning it to a variable
    print(f"Area is {Circle(5).getArea()}")
   
    

#Invoke the main function
main()
