# import random module to generate random numbers
import random

# Define function to generate the winning numbers that user playing against and print to screen
def pick():
    lottery = []
    for i in range(0,6):
        num = random.randint(1,20)
        lottery.append(num)
    return lottery
winning = pick()

# Define function to compare user ticket with winning numbers
def num_matches(x,y):
    counter = 0
    for nums in range(6):
        if x[nums] == y[nums]:
           counter +=1
    if counter == 0:
        return 0
    elif counter == 1:
        return 4 
    elif counter == 2:
        return 7 
    elif counter == 3:
        return 100 
    elif counter == 4:
        return 5000 
    elif counter == 5:
        return 1000000 
    elif counter == 6:
        return 25000000 
    
balance = 0

for i in range(100):
    ticket = pick()
    balance -= 2
    match_result = num_matches(winning,ticket)
    balance += match_result
print(f'You have a balance of ${float(balance)}')

earnings =  abs(-200 - balance)
ROI = (earnings - 200)/200
print(f'You earned ${earnings} and your ROI is {ROI}')