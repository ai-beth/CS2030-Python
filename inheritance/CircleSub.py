#Using super() helps to avoid explicitly referring to the superclass
#by name and ensures that the correct methods are called in the presence
#or multiple inheritance
#Note: When invoke the method super(), don't pass the self arugment

#Import the math module and super class
from GeometricObject import GeometricObject
import math

#Create a subclass of GeomtricObject
class Circle(GeometricObject):

    #Initializer Constructor
    def __init__(self,radius):
        super().__init__() #Invokes the superclasses init method
        self.__radius = radius

    #Method to get the radius
    def getRadius(self):
        return self.__radius

    #Method to set the radius
    def setRadius(self,radius):
        self.__radius = radius

    #Method to get the area
    def getArea(self):
        return self.__radius * self.__radius * math.pi

    #Method to get the diameter
    def getDiameter(self):
        return 2 * self.__radius

    #Method to get the perimeter
    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    #Method to display the circle
    def printCircle(self):
        #Invoke the str method from the superclass
        print(self.__str__() + " radius: " + str(self.__radius))

    #Override the __str__ method in the superclass
    #The method must be defined in the subclass using
    #the same header as in its superclass
    def __str__(self):
        return f"{super().__str__()} radius: {self.__radius}"







    
