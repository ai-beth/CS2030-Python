#CS2030
#Create the Rectangle Class according to the UML Diagram

#Rectangle Class
class Rectangle():
    

    #Initializer with default values
    def __init__(self, width = 1, height = 2):
        self.width = width
        self.height = height

    #Method to get the area
    def getArea(self):
        return self.width * self.height

    #Method to get the perimeter
    def getPerimeter(self):
        return 2 * (self.width + self.height)

    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
        

    
