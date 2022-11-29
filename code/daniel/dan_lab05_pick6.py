#---------------------------------
# PDX Code Guild: HB3
# Lab05: Pick6
# Author: Daniel Smith
# Date: 2022.11.28
#---------------------------------

# Have the computer play pick6 many times and determine net balance.

# Initially the program will pick 6 random numbers as the 'winner'.
# Then try playing pick6 100,000 times, w/ the ticket cost and payoff below.

# A ticket contains 6 numbers, 1 to 99, and the number of matches
# between the ticket and the winning numbers determines the payoff.
# Order matters, if the winning numbers are [5, 10] and your ticket numbers
# are [10, 5] you have 0 matches. If the winning numbers are [5, 10, 2]
# and your ticket numbers are [10, 5, 2], you have 1 match.
# Calculate your net winnings (the sum of all expenses and earnings).


# Write the following functions and use them in the code:

# pick6(): Generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets.
# Return the list num_matches(winning, ticket):
# Return the number of matches between the winning numbers and the ticket.

# Steps
# Generate a list of 6 random numbers representing the winning tickets
from random import randint
golden_ticket = [randint(1, 9) for x in range(6)]
print(golden_ticket)

######## Do they need to be 6 DIFFERENT random numbers or are duplicates allowed?

# Start your balance at 0
balance = 0

# Loop 100,000 times, for each loop:

# Generate a list of 6 random numbers representing the ticket
player_ticket = [randint(1, 9) for x in range(6)]
print(player_ticket)

# Subtract 2 from your balance (you bought a ticket)
balance -= 2

# Find how many numbers match
matches = [y for x, y in enumerate(player_ticket) if player_ticket[x] == golden_ticket[x]]
print(matches)

# Add to your balance the winnings from your matches
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
balance += winnings_ref[len(matches)]
print(balance)

# After the loop, print the final balance
# Version 2
# The ROI (return on investment) is defined as (earnings - expenses)/expenses.
# Calculate your ROI, print it out along with your earnings and expenses.