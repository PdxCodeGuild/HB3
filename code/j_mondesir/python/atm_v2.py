class ATM:
    def __init__(self,):
        self.balance = 0
        self.interest = 0.1
        self.transactions = []
    def check_balance(self):
        balance = self.balance 
        return balance
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        self.transactions.append(f'user deposited ${amount}')
        return amount
    def check_withdrawal(self,amount):
        if self.balance - amount >= 0:
            return True
        else:
            return False
    def withdraw(self,amount):
        self.balance = self.balance - amount
        self.transactions.append(f'user withdrew ${amount}')
        return amount
    def calc_interest(self):
        interest = self.balance * (self.interest/100)
        return interest
    def print_transaction(self):
        return self.transactions
        
                   
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
        #atm.print_transaction.append(f'user deposit ${amount}')
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            #atm.print_transaction.append(f'user withdrew ${amount}')
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'transaction':
        trans_money = atm.print_transaction()
        print('\n'.join(trans_money)) 
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - in and out money')
        print('exit     - exit the program')    
    elif command == 'exit':
        break
    else:
        print('Command not recognized')