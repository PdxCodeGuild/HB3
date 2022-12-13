# create an instance of our class
class ATM:   
   
#function containing two attributes: a balance and an interest rate.
#A newly created account will default to a balance of 0 
# and an interest rate of 0.1% and Implement the initializer.
    def __init__(self, balance = 0, interest = 0.1):
        self.balance      = balance
        self.interest     = interest
        self.transactions = []

# check_balance() returns the account balance
    def check_balance(self):
        return self.balance

# get_receipt() return both transactions and the acct balance
    def get_receipt(self):
        self.check_balance()
        self.print_transactions()
        return self.transactions

# deposit(amount) deposits the given amount in the account
    def deposit(self, amount):
        if amount <= 0:
            return False
        else:
            self.balance += amount
            self.transactions.append(amount)
            return True

# check_withdrawal(amount) returns true if the 
# withdrawn amount won't put the account in the negative
    def check_withdraw (self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(-amount)
            return self.balance

# withdraw(amount) withdraws the amount from the account and returns it
    def withdrawal(self, amount):
        if self.balance < amount:
            return False

# calc_interest() returns the amount of interest calculated on the account   
    def calc_interest(self):
        interest =self.interest * self.balance
        print(f"{self.interest} * ${self.balance}  =  ${interest}")
        return interest

# Version 2 printing all transactions
    def print_transactions(self):
        return self.transactions     
         
atm = ATM()

print(f"\n....................Welcome To The ATM.......................")

options_menu = {
'1': 'Balance',
'2': 'Deposit',
'3': 'Withdraw',
'4': 'Interest',
'5': 'Transactions',
'6': 'Receipt',
'7': 'Exit',
}

while True:
    #===============Asking the user select a command from the options=====================
    print()
    for label, option in options_menu.items():
        print(f'{label}. {option}')
    command = input('\nEnter the number of the option you would like to perform\n>>>')
    command = options_menu.get(command)


    # call the check_balance() method
    if command == 'Balance':
        balance = atm.check_balance() 
        print(f'Your balance is ${balance}')

    # printing out receipt by calling check_balance() &
    # print_transactions() functions to get all transactions
    elif command == 'Receipt':
        balance = atm.check_balance()
        atm.transactions = atm.print_transactions()
        for transaction in atm.transactions:
            if int(transaction) > 0:
                print(f"Deposited amt ${transaction}")
            elif int(transaction) < 0:
                print(f"Withdrawn amt -${-transaction}")
        print(f"Your remaining balance is ${balance}")

        
# ================call the deposit(amount) method=============
    elif command == 'Deposit':
        amount = float(input('How much would you like to deposit?\n>>>$'))
        success = atm.deposit(amount) 
        if not success:
            print("Deposit amount must be a positive number.")
        else:
            print(f'Deposited ${amount}')

        
# tracking all withdraws by calling the check_withdraw(amount) function
    elif command == 'Withdraw':
        amount = float(input('How much would you like to withdraw?\n>>>$'))
        success = atm.check_withdraw(amount)
       
        # checking if the acct bal if is less than the withdrawer amt 
        if not success:
            print('Insufficient funds')
            print(f'Your account balance is ${atm.balance}')
        else:
            atm.withdrawal(amount)
            print(f'Withdrew ${amount}')
            

# call the calc_interest()function to get the interest on deposit
    elif command == 'Interest':
        amount = atm.calc_interest() 
        atm.deposit(amount)
        print(f'Accumulated interest is ${amount}')


# call the print_transactions()function to track all transactions
    elif command == 'Transactions':
        atm.transactions = atm.print_transactions()
        for transaction in atm.transactions:
            if int(transaction) > 0:
                print(f"Deposited amt ${transaction}")
            elif int(transaction) < 0:
                print(f"Withdrawn amt -${-transaction}")


    elif command == 'Exit':
        print("Goodbye and thank for using our atm machine.")
        break
    else:
        print('Command not recognized please select the right command')