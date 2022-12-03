class ATM:
    def __init__(self, balance = 0, interest_rate = 0.001):
        self.balance = balance
        self.interest_rate = interest_rate

    def check_balance(self): #returns the account balance
        self.balance = balance
        return balance
    
    def deposit(amount, balance): #deposits the given amount in the account
        balance += amount
        return balance

    def check_withdrawal(amount, balance): #returns true if the withdrawn amount won't put the account in the negative
        if balance - amount >= 0:
            return True

    def withdraw(amount, balance): #withdraws the amount from the account and returns it
        balance -= amount
        return balance

    def calc_interest(balance, interest): #returns the amount of interest calculated on the account
        interest = balance * 0.001
        return interest
    


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