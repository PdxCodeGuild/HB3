print('PCO Practice Lab')

####### Version 1 #######

class ATM: 

    def __init__(self, balance = 0, interest_rate = .1, transactions = []): ###initializer
        self.balance = balance  
        self.interest_rate = interest_rate
        self.transaction_list = [] ###### ^^^^ "transactions" is a version 2 addition

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.transaction_list.append(f'The user deposited ${amount}') #### version 2 addition
        return amount

    def check_withdrawal(self, amount):
        while True: # i dont think this is necessary, but the lab specifically says to return True
            if amount <= self.balance:
                return self.balance
            else:
                return print('ERROR!')

    def withdraw(self, amount):
        self.balance = self.balance - amount
        self.transaction_list.append(f'The user withdrew ${amount}') #### version 2 addition
        return amount

    def calc_interest(self):
        amount = (self.balance * self.interest_rate) + self.balance
        return amount
    
    ########### This is a version 2 addition ##########
    def print_transaction(self): 
         return self.transaction_list
##############################################################

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
    #######version 2 addition    
    elif command == 'transaction':
        receipt = atm.print_transaction()
        '''for i in range(len(receipt)):
            for x in receipt:             ##### trying to make my transaction list print vertically
                print(x[1], end=' ')'''
        print(receipt)
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - print list of transactions') ##### version 2 addition
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
        

