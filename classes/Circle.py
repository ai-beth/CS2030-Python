#Description: Circle Class to define what a circle object is

#Import the math module
import math

#Create a Class called Circle
class Circle:

    #Create / initial our object
    def __init__(self, radius = 1):
        self.radius = radius

    #Method to get the perimeter
    def getPerimeter(self):
        return 2 * self.radius * math.pi

    #Method to get the area
    def getArea(self):
        return self.radius * self.radius * math.pi

    #Method to set the radius
    def setRadius(self,radius):
        self.radius = radius











    
