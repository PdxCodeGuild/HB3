import math

class ATM:
    def __init__(self):
        self.balance = 0 
        self.interest_rate = .001
        self.loop = []
        self.transactions = []
    def check_balance(self):
        self.balance == self.balance
        return self.balance 
    def deposit(self, amount):
        self.balance += amount
        return amount
    def check_withdrawl(self, amount):
        if amount > self.balance:
            return True
    def withdraw(self, amount):
        self.balance -= amount 
        self.loop.append(f'user withdrawls {amount}')       # need users input....loop?
        return amount
    def calc_interest(self):
        interest = self.interest_rate * self.balance 
        return interest 
    def print_transactions(self,trans):
        if trans == 'transactions':
            return self.transactions
        else:
            self.transactions.append(trans)



atm = ATM() # create an instance of our class
print('Welcome to the ATM')
transactions = []
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance() # call the check_balance() method
        atm.print_transactions('User check balance')
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        atm.print_transactions(f'Desposited {amount}')
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawl(amount): # call the check_withdrawal(amount) method
            print('Insufficient funds')
        else:
            atm.withdraw(amount) # call the withdraw(amount) method
            atm.print_transactions(f'User withdrew {amount}')
            print(f'Withdrew ${amount}')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        atm.print_transactions(f'User deposited {amount}')
        print(f'Accumulated ${amount} in interest')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
    elif command == 'transactions':
        print(atm.print_transactions(command))
    elif command == 'exit':
        break
    else:
        print('Command not recognized')