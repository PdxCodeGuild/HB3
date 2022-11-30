#---------------------------------
# PDX Code Guild: HB3
# Lab05: Pick6
# Author: Daniel Smith
# Date: 2022.11.28
#---------------------------------

# Program will pick 6 random numbers as the 'golden ticket',
# then try 100,000 times to match the golden ticket,
# then print the balance, earnings, expenses, and ROI.

from random import randint
def randticket(): 
    return [randint(1, 99) for _ in range(6)] ### Are duplicate numbers permitted? This code assumes so.

# Generate a list of 6 random numbers representing the winning ticket.
golden_ticket = randticket()

# Start the balance at 0.
earnings = 0
expenses = 0

# Loop 100,000 times.
for _ in range(100000):

    # Generate a list of 6 random numbers representing the ticket.
    ticket = randticket()

    # Add 2 to expenses (cost of a ticket).
    expenses += 2

    # Find the matches between the winning numbers and the ticket.
    matches = [
        value for pos, value in enumerate(ticket)
        if ticket[pos] == golden_ticket[pos]
        ]

    # if 1 number matches, you win $4
    # if 2 numbers match, you win $7
    # if 3 numbers match, you win $100
    # if 4 numbers match, you win $50,000
    # if 5 numbers match, you win $1,000,000
    # if 6 numbers match, you win $25,000,000
    winnings_ref = {
        0 : 0,
        1 : 4,
        2 : 7,
        3 : 100,
        4 : 50000,
        5 : 1000000,
        6 : 25000000
        }

    # Add winnings to earnings.
    earnings += winnings_ref[len(matches)]

# Print the final balance, earnings, expenses, and ROI.
print(f'\nGolden Ticket: {golden_ticket}')
print(f'Final Balance: ${earnings - expenses}')
print(f'Earnings: ${earnings}')
print(f'Expenses: ${expenses}')
print(f'ROI: {(earnings - expenses) / expenses:.1%}\n')

# f"{1/3.0:.1%}"