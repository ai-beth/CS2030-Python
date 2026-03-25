#Create our own exception class
class InvalidRadiusException(RuntimeError):
    #Initializer method
    def __init__(self,radius):
        super().__init__()
        self.__radius = radius

    #Getter method
    def getRadius(self):
        return self.__radius
