'''
 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
      Project: Lab 8 - ATM
      Author: Scott Lefgren
      Email: scojlefg@gmail.com
      Date: December 6, 2022
___________________          _-_
\==============_=_/ ____.---'---`---.____
            \_ \    \----._________.----/
              \ \   /  /    `-_-'
          __,--`.`-'..'-_
         /____          ||
              `--.____,-'

 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
'''

'''
Let's represent an ATM with a class containing two attributes: 
a balance and an interest rate. A newly created account will 
default to a balance of 0 and an interest rate of 0.1%. 
implement the initializer, as well as the following functions:

    -check_balance() returns the account balance
    -deposit(amount) deposits the given amount in the account
    -check_withdrawal(amount) returns true if the withdrawn amount won't 
      put the account in the negative
    -withdraw(amount) withdraws the amount from the account and returns it
    -calc_interest() returns the amount of interest calculated on the account


'''
import math

class ATM:
    def __init__(self):  # this is the initializer
        self.balance = 0
        self.interest_rate = 0.1
    # end function __init__

    # returns the account balance
    def check_balance(self):  
       
       print("CLASS -Check Balance") # Test code
       return self.balance

    # end function check_balance
    
    # deposits the given amount in the account
    def deposit(self,amount):  
        print("CLASS-Deposit")  # test code

        previous_balance = self.balance
        self.balance = self.balance + amount
        print(f'Previous Balance: ${previous_balance}')
        print(f'New balance: ${self.balance}')

    # end function deposit

    #  returns true if the withdrawn amount won't 
    # put the account in the negative
    def check_withdrawal(self,amount): 

        print("CLASS-check withdrawal")  # test code
        if self.balance - amount > 0:
            return True
        elif self.balance - amount < 0:
            print("Unable to withdraw this amount check balance and try again")
            return False

    # end function check_withdrawal

    # withdraws the amount from the account and returns it
    def withdraw(self,amount):  
        
       print("CLASS-withdraw") # test code

       if self.balance - amount > 0:
            previous_balance = self.balance
            self.balance = self.balance - amount
            print(f'Previous Balance: ${previous_balance}')
            print(f'New balance: ${self.balance}')
            return True

       elif self.balance - amount < 0:
            print("Unable to withdraw this amount check balance and try again")
            return False
    
    #end function withdraw

    # returns the amount of interest calculated on the account
    def calc_interest(self): 

        print("CLASS-calc_interest") # test code
    
    # end function 



# BEGIN CODE Provided

atm = ATM() # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance() # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')



# END