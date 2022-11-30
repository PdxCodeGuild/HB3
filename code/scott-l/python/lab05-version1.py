'''
 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
      Project: HB3 - Lab 05 Pick6 - Version 1
      Author: Scott Lefgren
      Email: scojlefg@gmail.com
      Date: November 28, 2022
___________________          _-_
\==============_=_/ ____.---'---`---.____
            \_ \    \----._________.----/
              \ \   /  /    `-_-'
          __,--`.`-'..'-_
         /____          ||
              `--.____,-'

 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
'''

""" 
Have the computer play pick6 many times and determine net balance.

Initially the program will pick 6 random numbers as the 'winner'. 
Then try playing pick6 100,000 times, with the ticket cost and payoff below.

A ticket contains 6 numbers, 1 to 99, and the number of matches between 
the ticket and the winning numbers determines the payoff. Order matters, 
if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you 
have 0 matches. If the winning numbers are [5, 10, 2] and your ticket numbers 
are [10, 5, 2], you have 1 match. Calculate your net winnings (the sum of all 
expenses and earnings).

    a ticket costs $2
    if 1 number matches, you win $4
    if 2 numbers match, you win $7
    if 3 numbers match, you win $100
    if 4 numbers match, you win $50,000
    if 5 numbers match, you win $1,000,000
    if 6 numbers match, you win $25,000,000

Write the following functions and use them in the code:

    pick6(): Generate a list of 6 random numbers, which can then be used 
    for both the winning numbers and tickets. Return the list
    num_matches(winning, ticket): Return the number of matches between the 
    winning numbers and the ticket.

Steps

    Generate a list of 6 random numbers representing the winning tickets
    Start your balance at 0
    Loop 100,000 times, for each loop:
    Generate a list of 6 random numbers representing the ticket
    Subtract 2 from your balance (you bought a ticket)
    Find how many numbers match
    Add to your balance the winnings from your matches
    After the loop, print the final balance

 """

import random
import re

# Generate a list of 6 random numbers representing the winning tickets

def random_six():
     num_list_random = []
     # loop 6 times
     for n in range(6):
          # generate a random number
          number_rand = random.randint(1,99)
          num_list_random.append(number_rand)
     # end for
     return num_list_random
# end function random_six

# winning number to start with
winning_num = random_six()
# print(f'Winning Number {winning_num}')  # DEBUG print


# attempted sort code but order matters so this will 
# temp_num.sort()
# print(f'sort 1 {temp_num}')
# temp_num1.sort()
# print(f'sort 2 {temp_num1}')
# 
# attempted to use set in order to find the answer but discovered sets order doesn't matter
# and therefore will not work
# # print(set(temp_num))
# temp_num = [10,20,30,40,50,60]
# temp_num1 = [10,10,70,70,70,70]
# print(temp_num)
# print(temp_num1)

# ex_set = set(temp_num)
# print(ex_set.isdisjoint(set(temp_num1)))

# Attempted to use match but the random numbers are established in a list
# and not a string making it difficult to match because the list needs to convert to a string
# re.match(pattern, string, flags=0)
# match_obj = re.match(r'/d temp_num[0]', temp_num[1])
# print(match_obj.group())

amount_wins = 0
for num in range(100000):
     # Choose a ticket number
     ticket_num=random_six()
     # print(f'Ticket Number {ticket_num}')  # DEBUG CODE
     count = 0  # initialize count
     # Compare the ticket number to the winning number
     for check_num in range(len(ticket_num)):
          if ticket_num[check_num] == winning_num[check_num]:
               count = count + 1
          else:
               continue
          # end if
     # end for

     if count == 1:

     elif count == 2:

     elif count == 3:
     amount_wins = count + amount_wins
# end for

print(f'Number of wins: {amount_wins}')

