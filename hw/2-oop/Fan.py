#CS2030
#Create the Fan Class according to the UML Diagram

#Fan Class
class Fan:

    #Constants for the fan speeds
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    #Initializer with default properties
    def __init__(self, speed=SLOW, radius=5.0, color="blue", on=False):
        self.__speed = speed  # private data field for fan speed
        self.__on = on  # private data field for fan status (on/off)
        self.__radius = radius  # private data field for fan radius
        self.__color = color  # private data field for fan color

    #Get the fan speed
    def getSpeed(self):
        return self.__speed

    #Set the fan speed
    def setSpeed(self, speed):
        self.__speed = speed

    #Check if the fan is on
    def isOn(self):
        return self.__on

    #Turn the fan off and on
    def power(self, on):
        self.__on = on

    #Get the fan radius
    def getRadius(self):
        return self.__radius

    #Set the fan radius
    def setRadius(self, radius):
        self.__radius = radius

    #Get the fan color
    def getColor(self):
        return self.__color

    #Set the fan color
    def setColor(self, color):
        self.__color = color

