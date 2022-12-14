import random
import numbers

def pick6():
    winning_ticket = []
    for x in range(0,6):
        n = random.randint(0,99)
        winning_ticket.append(n)
    return winning_ticket                     #-------end?


# Sum_of_expenses 
# Earings ------------Save both for later
 
def num_matches(winning_ticket, ticket):
    matches = 0 
    for i in range(6):
        if winning_ticket[i] == ticket[i]:
            matches += 1
    return matches

winning_ticket = pick6()

wins = 0 
games = 0
expenses = 0 

while games < 100000:
    games += 1
    expenses -=2
    num_match = num_matches(winning_ticket,pick6())
    if num_match == 1:
        wins += 4 
    elif num_match == 2:
        wins += 7
    elif num_match == 3:
        wins += 100
    elif num_match == 4:
        wins += 50000
    elif num_match == 5:
        wins += 1000000
    elif num_match == 6:
        wins += 25000000

print(wins)
print(games)


expenses = abs(expenses)
roi = (wins - expenses)/expenses 
#(earnings - expenses)/expenses
print(roi)