#CS2030
#Test the Account class created for HW3

from Problem9_3 import Account
#main
def main():
        
    #Create an Account object with
    #id = 1122
    #balance = 20000
    #AiR = 4.5
    account = Account(1122,20000,4.5)

    #Use withdraw to wd 2500
    account.withdraw(2500)

    #Use the deposit() to deposit 3000
    account.deposit(3000)

    #Print the id,balance,monthly interest rate, and monthly interest
    print(f"Account ID: {account.getId()}")
    print(f"Account Balance: ${account.getBalance():,.2f}")
    print(f"Monthly Interest Rate: {account.getMonthlyInterestRate():,.2f}%")
    print(f"Monthly Interest Amount: ${account.getMonthlyInterest():,.2f}")
        
#Call the main
main()
