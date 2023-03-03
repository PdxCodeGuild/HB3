#---------------------------------
# PDX Code Guild: HB3
# Lab08: ATM
# Author: Daniel Smith
# Date: 2022.12.3
#---------------------------------

# Represent an ATM with a class containing two attributes: balance and interest rate.
# Newly created accounts default to a balance of 0 and an interest rate of 0.1%.
class ATM:
    def __init__(self, balance = 0, interest_rate = 0.001): # Implement initializer.
        self.balance = balance # These are attributes, aka member variables.
        self.interest_rate = interest_rate
        self.ledger = [] # Create list to add a record of each transaction to.
    # check_balance() returns the account balance.
    def check_balance(self):
        return self.balance
    # deposit(amount) deposits the amount in the account.
    def deposit(self, amount):
        self.balance += amount
        self.ledger.append(f'Deposited {amount}') # Add str record to the ledger.
    # check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative.
    def check_withdrawal(self, amount):
        if amount <= self.balance:
            return True
        else:
            return False
    # withdraw(amount) withdraws the amount from the account.
    def withdraw(self, amount):
        self.balance -= amount
        self.ledger.append(f'Withdrew {amount}') # Add str record to the ledger.
    # calc_interest() returns the amount of interest calculated on the account.
    def calc_interest(self):
        return self.balance * self.interest_rate
    # print_transactions() prints out the list of transactions aka ledger.
    def print_transactions(self):
        print(*self.ledger, sep = '\n') # Display ledger list formatted as indexes seperated by new lines.

atm = ATM() # Creates an instance of the class.
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance() # Call the check_balance() method.
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # Call the deposit(amount) method.
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like to withdraw? '))
        if atm.check_withdrawal(amount): # Call the check_withdrawal(amount) method.
            atm.withdraw(amount) # Call the withdraw(amount) method.
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds.')
    elif command == 'interest':
        amount = atm.calc_interest() # Call the calc_interest() method.
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'ledger':
        atm.print_transactions() # Call the print_transactions() method.
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('ledger - get transaction history')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized.')