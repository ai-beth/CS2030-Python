from GeometricObject import GeometricObject

#Create the tringle sublass
class Triangle(GeometricObject):

    #Initializer
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        GeometricObject.__init__(self)

    #Get the side1 - side2 - side3
    def getSide1(self):
        return self.side1
    
    def getSide2(self):
        return self.side2
    
    def getSide3(self):
        return self.side3

    #Get method for finding the area of a triangle
    def getArea(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(S * (s - self.side1) * (s - self.side2) * (s - self.side3))

    #get method for finding perimeter
    def getPerimeter(self):
        return self.side1 + self.side2 + self.side3

    #to string method
    def toString(self):
        return f"Triangle: side1 = {self.side1} side2 = {self.side2} side3 = {self.side3}"
