# Lab 5v1 -> Pick 6 (Have the computer play pick6 many times and determine net balance)
#   a ticket costs $2
#   if 1 number matches, you win $4
#   if 2 numbers match, you win $7
#   if 3 numbers match, you win $100
#   if 4 numbers match, you win $50,000
#   if 5 numbers match, you win $1,000,000
#   if 6 numbers match, you win $25,000,000

print('************* WELCOME TO PICK 6 *****************')
import random

# Generate a list of 6 random numbers representing the winning tickets
def pick6():
    numbers = []
    for i in range(6):
        random_number = (random.randrange(1,99))
        numbers.append(random_number)
    return numbers

ticket = pick6()
print('Your ticket numbers are:', ticket) 

# return the number of matches between the winning numbers and the ticket 
def num_matches(winning, ticket):
    bool_list = list(map(lambda x, y: x == y, winning, ticket))
    count = bool_list.count(True)
    return count

# start your balance at 0
balance = 0
expenses = 0
earnings = 0

# loop 100,000 times
i = 1
while i != 100001:
    balance = balance - 2
    expenses = expenses - 2
    winning = pick6()
    if num_matches(ticket, winning) == 1:
        balance = balance + 4
        earnings = earnings + 4
    elif num_matches(ticket, winning) == 2:
        balance = balance + 7
        earnings = earnings + 7
    elif num_matches(ticket, winning) == 3:
        balance = balance + 100
        earnings = earnings + 100
    elif num_matches(ticket, winning) == 4:
        balance = balance + 50000
        earnings = earnings + 50000
    elif num_matches(ticket, winning) == 5:
        balance = balance + 1000000
        earnings = earnings + 1000000
    elif num_matches(ticket, winning) == 6:
        balance = balance + 25000000
        earnings = earnings + 25000000
    i = i + 1

roi = (earnings - abs(expenses))/abs(expenses)  
# print the balance 
print('Your balance is:', balance)
print('Your earnings are:', earnings)
print('Your expenses are:', expenses)
print('Your ROI is:', '{percent:.2%}'.format(percent=roi))
