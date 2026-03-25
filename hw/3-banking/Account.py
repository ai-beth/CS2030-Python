#CS2030
#The Account class created in problem 9.3

#Create the Account Class
class Account:

    #Initializer with default values
    #id = 0
    #balance = 100
    #annualInterestRate = 0
    def __init__(self, id = 0, balance = 100, annualInterestRate = 0):
        #private attributes
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    #Getter Methods
    def getId(self):
        return self.__id

    def getBalance(self):
        return self.__balance

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def getMonthlyInterestRate(self):
        return self.__annualInterestRate / 12

    def getMonthlyInterest(self):
        return self.__balance * (self.getMonthlyInterestRate() / 100)

    #Setter Methods
    def setId(self, id):
        self.__id = id

    def setBalance(self, balance):
        self.__balance = balance

    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate

    #Method to withdraw a specified amount
    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient Funds"
        self.__balance -= amount
        
    #Method to deposit a specified amount
    def deposit(self, amount):
        self.__balance += amount
    

    
