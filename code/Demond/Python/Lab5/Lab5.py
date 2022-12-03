import random 
import re

def pick6():
    results = []
    for x in range(6):
        results.append(random.randint(1,99))
    return results
# [random.randint(1, 99) for x in range(6)]

Winning_Numbers = [1,2,3,4,5,6,]
Ticket = [1,2,3,4,6,6]

def num_matches(Winning_Numbers, Ticket):
    matches = 0
    if Winning_Numbers[0] == Ticket[0]:
        matches += 1
    if Winning_Numbers[1] == Ticket[1]:
        matches += 1
    if Winning_Numbers[2] == Ticket[2]:
        matches += 1
    if Winning_Numbers[3] == Ticket[3]:
        matches += 1
    if Winning_Numbers[4] == Ticket[4]:
        matches += 1
    if Winning_Numbers[5] == Ticket[5]:
        matches += 1
    return matches
print(num_matches(Winning_Numbers, Ticket))
# print(num_matches(Winning_Numbers, Ticket))

# balance = -2
for x in range(100000):
    x = Winning_Numbers
    y=Ticket
    balance = -2
    if num_matches(x, y) == 1:
        balance + 4
    if num_matches(x, y) == 2:
        balance + 7 
    if num_matches(x, y) == 3:
        balance + 100
    if num_matches(x, y) == 4:
        balance + 50,000
    if num_matches(x, y) == 5:
        balance + 10000000
    if num_matches(x, y) == 6:
        balance + 25000000
print(balance)