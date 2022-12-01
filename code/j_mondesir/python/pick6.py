# import random module to generate random numbers
import random

# generate 6 numbers ticket that user bought and print to screen
ticket = []
for i in range(0,6):
    user = random.randint(1,99) 
    ticket.append(user)
print(ticket)

# Define function to generate the winning numbers that user playing against and print to screen
def pick():
    lotteryNumbers = []
    for i in range(0,6):
        num = random.randint(1,99)
        lotteryNumbers.append(num)
    return lotteryNumbers
winning = pick()
print(pick())

# Define function to compare user ticket with winning numbers
def num_matches(winning,ticket):
    counter = 0
    for x in ticket:
        if x in winning:
           counter +=1
        return counter
match_result = num_matches(winning,ticket) 
   



        
    
    
        