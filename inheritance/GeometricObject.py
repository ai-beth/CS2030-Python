class GeometricObject:

    #Initializer Constructor
    def __init__(self, color = "Green", filled = True):
        self.__color = color
        self.__filled = filled

    #Method to get the color
    def getColor(self):
        return self.__color

    #Method to set the color
    def setColor(self,color):
        self.__color = color

    #Method to see if object has color
    def isFIlled(self):
        return self.__filled

    #Method to set the fill status
    def setFilled(self,filled):
        self.__filled = filled

    #str method
    def __str__(self):
        return f"Color: {self.__color} and filled: {self.__filled}"








