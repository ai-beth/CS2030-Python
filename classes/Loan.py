#Create Class
class Loan:

    #Initialize the object
    def __init__(self,annulInterestRate = 2.5,
                 numberOfYears = 1, loanAmount = 1000, borrower = " "):
        #Private Attributes
        self.__annualInterestRate = annualInterestRate
        self.__numberOfYears = numberOfYears
        self.__loanAmount = loanAmount
        self.__borrower = borrower

    #Getter Methods
    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def getNumberOfYears(self):
        return self.__numberOfYears

    def getLoanAmount(self):
        return self.__loanAmount

    def getBorrower(self):
        return self.__borrower

    #Setter Methods
    def setAnnualInterestRate(self,annualInterestRate):
        self.__annualInterestRate = annualInterestRate

    def setNumberOfYears(self,numberOfYears):
        self.__numberOfYears = numberOfYears

    def setLoanAmount(self,loanAmount):
        self.__loanAmount = loanAmount

    def setBorrower(self,borrower):
        self.__borrower = borrower

    #Computing the monthly payment method
    def getMonthlyPayment(self):
        monthlyInterestRate = self.__annualInterestRate / 1200

        monthlyPayment = self.__loanAmount * monthlyInterestRate / \
                         (1 - (1 / (1 + monthlyInterestRate) ** \
                               (self.__numberOfYears * 12)))

        #Return the results back to the caller
        return monthlyPayment

    #Computing the total payment method













        











    




    
