print('\n\tPick 6 Lab')

import random

def pick6():
    number_list = []   ### i had parenthesis here instead of brackets, causing issues later in the code
    for num in range(6):
       numbers = random.randint(1, 99) 
       number_list.append(numbers)
    return number_list   #### initially screwed this up because i had it apply to the winning ticket only


def num_matches(winning, ticket):
    match = 0
    for num in range(6):
        if winning[num] == ticket[num]:
            match = match + 1

    ###### this will account for all the matching possibilities        
            
    if match == 0:
        return 0
    
    elif match == 1:
        return 4
    
    elif match == 2:
        return 7
    
    elif match == 3:
        return 100
    
    elif match == 4:
        return 50000
    
    elif match == 5:
        return 1000000
    
    elif match == 6:
        return 25000000

account_balance = 0

winning = pick6()

for num in range(100000):
    
    ticket = pick6()
    
    account_balance -= 2

    winnings = num_matches(winning, ticket)   #####this was giving me an error because i didnt put brackeus at the top
    
    account_balance = account_balance + winnings

print(f'\n\tCongrats! you have won: {account_balance} dollars')
    