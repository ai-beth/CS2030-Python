#CS2030
#Create the Stock Class according to the UML Diagram

# Stock Class
class Stock:

    #Initializer with default values
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.__symbol = symbol  #private data field for stock symbol
        self.__name = name  #private data field for stock name
        self.__previousClosingPrice = previousClosingPrice  #private data field for previous price
        self.__currentPrice = currentPrice  #private data field for current price

    #Getter method for stock name
    def getName(self):
        return self.__name
    
    #Getter method for stock symbol
    def getSymbol(self):
        return self.__symbol

    #Getter and setter methods for previous price
    def getPreviousClosingPrice(self):
        return self.__previousClosingPrice
    
    def setPreviousClosingPrice(self, price):
        self.__previousClosingPrice = price

    #Getter and setter methods for current price
    def getCurrentPrice(self):
        return self.__currentPrice
    
    def setCurrentPrice(self, price):
        self.__currentPrice = price

    #Method to calculate the percentage change from previousClosingPrice to currentPrice
    def getChangePercent(self):
        return ((self.__currentPrice - self.__previousClosingPrice) / self.__previousClosingPrice) * 100 
