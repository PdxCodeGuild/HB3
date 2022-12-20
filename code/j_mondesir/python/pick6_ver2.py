# import random module to generate random numbers
import random

# Winning prizes
winning_prize = {1 : 4,
                 2 : 7,
                 3 : 100,
                 4 : 50000,
                 5 : 1000000,
                 6 : 25000000,
                 0 : 0
}
#Define function to generate the winning numbers 
def pick6():
    lotterpick = []
    for i in range(0,6):
        num = random.randint(1,100)
        lotterpick.append(num)
    return lotterpick
winning = pick6()

balance = 0
def num_matches(winning, ticket):
    counter = 0        
    if winning[0] == ticket[0]:
       counter +=1
    if winning[1] == ticket[1]:
       counter +=1
    if winning[2] == ticket[2]:
       counter +=1
    if winning[3] == ticket[3]:
       counter += 1
    if winning[4] == ticket[4]:
       counter += 1
    if winning[5] == ticket[5]:
       counter += 1
    return counter
         
for i in range(100000):
    tickets = pick6()
    balance -= 2
    match_result = num_matches(winning,tickets) 
    balance += winning_prize[match_result]
print(f'You have a balance of ${float(balance)}')

# for i in range(100):
#     ticket = pick()
#     balance -= 2
#     match_result = num_matches(winning,ticket)
#     balance += match_result
# print(f'You have a balance of ${float(balance)}')

earnings =  abs(-200000 - balance)
ROI = (earnings - 200000)/200000
print(f'You earned ${earnings} and your ROI is {ROI}')