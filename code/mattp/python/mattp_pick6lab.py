print('\n\tPick 6 Lab')

import random

ticket_price = 2

winning_ticket = [0, 9, 4, 1, 2, 6]

ticketo = random.sample(range(0, 9), 5)

print(ticketo)

def pick6():
    ticket_guess = []
    for space in range(0, 5):
        n = random.randint(0, 9)
    
        