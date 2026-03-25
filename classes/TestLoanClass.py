#Import the loan class
from Loan import Loan

#Create a main function
def main():

    #Enter yearly interest Rate
    annualInterestRate = float(input(
        "Enter yearly interest rate, example, 7.25: "))

    #Enter number of years
    numberOfYears = int(input(
        "Enter number of years as an integer: "))

    #Enter loan amount
    loanAmount = float(input(
        "Enter loan amount, example, 120000.95: "))

    #Enter a borrower
    borrower =  input("Enter a borrower's name: ")

    #Create a loan object
    loan = Loan(annualInterestRate,numberOfYears,
                loanAmount,borrower)

    #Display loan name, mothly payment and total payment
    print(f"The loan is for {loan.getBorrower()")
    print(f"The monthly payment is ${loan.getMonthlyPayment():.2f}")
    print(f"The total payment is ${loan.getTotalPayment():.2f}")

#Invoke the main function
main()









    
