#Import the superclass
from GeometricObject import GeometricObject

#Rectangle is a subclass of GeometricObject
class Rectangle(GeometricObject):

    #Initializer constructor
    def __init__(self, width = 1, height = 1):
        super().__init__() #Invoke superclass init method
        self.__width = width
        self.__height = height

    #Method to get the width
    def getWidth(self):
        return self.__width

    #Method the set the width
    def setWidth(self, width):
        self.__width = width

    #Method to get the height
    def getHeight(self):
        return self.__height

    #Method to set the height
    def setHeight(self, height):
        self.__height = height

    #Method to get the area
    def getArea(self):
        return self.__width * self.__height

    #Method to get teh perimeter
    def getPerimeter(self):
        return 2 * (self.__width + self.__height)

    #Method to ooveride the __str__ method
    def __str__(self):
        return f"{super().__str__()} width: {self.__width} \
height: {self.__height}"


