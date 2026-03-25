#Testing the Trinagle Class

#import triangle
from TriangleSub import Triangle


#Create a amain
def main():

    #Prompt the user to input the values for 3 side
    side1 = float(input("Enter side1: "))
    side2 = float(input("Enter side2: "))
    side3 = float(input("Enter side3: "))

    #Create the trinalge object
    triangle = Triangle(side1, side2, side3)

    #Promp thte user to input a color for our object
    color = input("Enter color: ")

    #Set the color using the GeometriCObject method setColor()
    triangle.setColor(color)

    #prompt the user to input the filled status
    filled = int(input("Enter 1/0 for fill(1:True, 0:False): "))


    #Check user input
    isFilled = (filled == 1)

    #set the filled status
    triangle.setFill(isFilled)



    #Check to see if our input forms a triangle
    if side1 + side2 <= side3 or side1 + side3 <= side2 or \
       side2 + side3 <= side1:
        print("The input cannot form a triangle")
        return
    #Display infor about our trianlge
    print(f"The area is {triangle.getArea()}")
    print(f"The perimeter is {triangle.getPerimeter()}")
    print(f"The color is {triangle.getColor()}")
    print(f"Filled is {triangle.isFilled()}")

#invoke the main
main()
