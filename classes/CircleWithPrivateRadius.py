#Radius property will not be directly accessed
#We still can display it with getter method

#Import the math module
import math

#Create Class
class Circle:
    #Initialize our object
    def __init__(self,radius = 1):
        self.setRadius(radius)

    #Getter methods
    def getRadius(self):
        return self.__radius

    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    def getArea(self):
        return self.__radius * self.__radius * math.pi

    #Setter method
    def setRadius(self,radius):
        self.__radius = radius if radius >= 0 else 0











    
