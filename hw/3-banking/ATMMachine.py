#CS2030
#Description: ATM Game
#Use the Account class to simulate an ATM Machine

#import Account
from Problem9_3 import Account

#Create the main for the ATM 
def main():

    #Create a list of 10 accounts with id in range 0-9
    #with a balance of 100 (defaulted in our class)
    accounts = [Account(id) for id in range(10)]

    #Main loop to continuously prompt the user for an account ID
    while True:

        #Prompt the user for an account id in range(0-9)
        accountId = int(input("Please enter an account id: "))

        #Ensure the account ID is valid
        if 0 <= accountId <= 9:

            #Get the account object for the entered accountId
            account = accounts[accountId]
            
            #Menu loop until the user chooses to exit
            choice = 0
            while choice != 4:

                #Display the menu
                print("\nMain menu")
                print("1: check balance")
                print("2: withdraw")
                print("3: deposit")
                print("4: exit")

                #Prompt the user to enter a choice
                choice = int(input("Enter a choice: "))
                
                #The menu choices
                if choice == 1:
                    #Check balance
                    print(f"The balance is ${account.getBalance():,.2f}")

                elif choice == 2:
                    #Withdraw money
                    amount = float(input("Enter an amount to withdraw: "))
                    account.withdraw(amount)
                    print(f"The balance is ${account.getBalance():,.2f}")

                elif choice == 3:
                    #Deposit money
                    amount = float(input("Enter an amount to deposit: "))
                    account.deposit(amount)
                    print(f"The balance is ${account.getBalance():,.2f}")
                    
        else:
            #Return an error message for incorrect account ID
            print("Invalid Input. Please enter a number between 0 and 9.")


#Call the main
main()
     
    
    
