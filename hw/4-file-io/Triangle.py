#CS2030
#Problem 13.12
#Description: The Triangle Error Class
#Create a custom exception class for handling invalid triangles
#Create the Triangle Class that extends geometric object

import math
from GeometricObject import GeometricObject 

#Custom exception class for invalid triangles
class TriangleError(RuntimeError):
    def __init__(self, side1, side2, side3):
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
        super().__init__(f"Invalid triangle sides: {side1}, {side2}, {side3}")

#Triangle class with methods for area, perimeter, and validation
class Triangle(GeometricObject):
    def __init__(self, side1=1.0, side2=1.0, side3=1.0, color="Green", filled=True):
        GeometricObject.__init__(self, color, filled)  #Initialize parent class
        
        #Validate if sides can form a triangle
        if not self.__isValidTriangle(side1, side2, side3):
            raise TriangleError(side1, side2, side3)
        
        #Initialize private side fields
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    #Private method to validate if sides form a valid triangle
    def __isValidTriangle(self, side1, side2, side3):
        return (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1)

    #Getter methods for each side
    def getSide1(self):
        return self.__side1

    def getSide2(self):
        return self.__side2

    def getSide3(self):
        return self.__side3

    #MEthod to calculate the area of the triangle
    def getArea(self):
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        return math.sqrt(s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3))

    #Method to calculate the perimeter of the triangle
    def getPerimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    #Override __str__ method to include color, filled status, and triangle side details
    def __str__(self):
        return (f"Triangle: side1 = {self.__side1}, side2 = {self.__side2}, side3 = {self.__side3}, {super().__str__()}")

#Create a main 
def main():

    #Try statement for our exception
    try:
        triangle = Triangle(3, 4, 5)  #Valid triangle
        print(triangle)  #Print valid triangle

        #This will raise an exception
        invalidTriangle = Triangle(1, 2, 3)  #Invalid triangle
        print(invalidTriangle)

    #Print the exception message  
    except TriangleError as e:
        print(e)  

#Call the main
main()
