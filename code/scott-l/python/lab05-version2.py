'''
 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
      Project: HB3 - Lab 05 Pick6 - Version 2
      Author: Scott Lefgren
      Email: scojlefg@gmail.com
      Date: November 30, 2022
___________________          _-_
\==============_=_/ ____.---'---`---.____
            \_ \    \----._________.----/
              \ \   /  /    `-_-'
          __,--`.`-'..'-_
         /____          ||
              `--.____,-'

 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
'''

# Version 2

# The ROI (return on investment) is defined as 
# (earnings - expenses)/expenses. Calculate your ROI, 
# print it out along with your earnings and expenses.

import random

# pick6(): Generate a list of 6 random numbers, which can then be used 
# for both the winning numbers and tickets. Return the list
def pick6():
     num_list_random = []
     # loop 6 times
     for n in range(6):
          # generate a random number
          number_rand = random.randint(1,99)
          num_list_random.append(number_rand)
     # end for
     return num_list_random
# end function pick6

# num_matches(winning, ticket): Return the number of matches between the 
# winning numbers and the ticket.
def num_matches(winning, ticket):
     # initialize counter
     match_count = 0
     # Compare all six digits of the ticket number to the winning number
     # Find how many numbers match
     for check_num in range(len(ticket)):
          if ticket[check_num] == winning[check_num]:
               match_count += 1
          else:
               continue
          # end if
     # end for

     # Return the number of matches between the winning numbers and the ticket.
     return match_count
# end function num_matches

#-----------------------------------------------------------------
# BEGIN

winning_amounts = {
     1: 4,   # if 1 number matches, you win $4
     2: 7,   # if 2 numbers match, you win $7
     3: 100,  # if 3 numbers match, you win $100
     4: 50000,  # if 4 numbers match, you win $50,000
     5: 1000000, # if 5 numbers match, you win $1,000,000
     6: 25000000 # if 6 numbers match, you win $25,000,000
}

winning_stats = {
     0: 0,
     1: 0,
     2: 0,
     3: 0,
     4: 0,
     5: 0,
     6: 0
}

# STEP 1
# Generate a list of 6 random numbers representing the winning tickets
winning_num = pick6()
# print(f'Winning Number {winning_num}')  # DEBUG print

# initialize for loop counters
amount_wins = 0
winnings = 0

# STEP 2   -Start your balance at 0
net_winnings_balance = 0
num_attempts = 100000
ticket_cost = 2

# STEP3 - Loop 100,000 times, for each loop:
for num in range(num_attempts):
# STEP 4 Generate a list of 6 random numbers representing the ticket
     ticket_num=pick6()
# STEP 5 Subtract 2 from your balance (you bought a ticket)
     net_winnings_balance -= ticket_cost
     # print(f'Ticket Number {ticket_num}')  # DEBUG CODE
     match_count = 0  # re-initialize match count
     
# STEP 6 Find how many numbers match
     # Compare all six digits of the ticket number to the winning number
     match_count = num_matches(winning_num, ticket_num)
     
# STEP 7 Add to your balance the winnings from your matches
     if match_count == 0:
          winning_stats[match_count] += 1  
     # if 1 number matches, you win $4
     if match_count == 1:
          net_winnings_balance += winning_amounts[match_count]
          winnings = winnings + winning_amounts[match_count]
          winning_stats[match_count] += 1 
     # if 2 numbers match, you win $7
     elif match_count == 2:
          net_winnings_balance += winning_amounts[match_count]
          winnings = winnings + winning_amounts[match_count]
          winning_stats[match_count] += 1 
     # if 3 numbers match, you win $100
     elif match_count == 3:
          net_winnings_balance += winning_amounts[match_count]
          winnings = winnings + winning_amounts[match_count]
          winning_stats[match_count] += 1 
     # if 4 numbers match, you win $50,000
     elif match_count == 4:
          net_winnings_balance += winning_amounts[match_count]
          winnings = winnings + winning_amounts[match_count]
          winning_stats[match_count] += 1 
     # if 5 numbers match, you win $1,000,000
     elif match_count == 5:
          net_winnings_balance += winning_amounts[match_count]
          winnings = winnings + winning_amounts[match_count]
          winning_stats[match_count] += 1 
     # if 6 numbers match, you win $25,000,000
     elif match_count == 6:
          net_winnings_balance += winning_amounts[match_count]
          winnings = winnings + winning_amounts[match_count]
          winning_stats[match_count] += 1 
     # end if

     amount_wins = match_count + amount_wins
# end for

# STEP 8 After the loop, print the final balance

# The ROI (return on investment) is defined as 
# (earnings - expenses)/expenses. Calculate your ROI, 
# print it out along with your earnings and expenses.

earnings = winnings
expenses = num_attempts*(ticket_cost)

roi_calc = (earnings - expenses)/(expenses)

print(f'Return on Investment {round(roi_calc*100,2)}%\n')

print(f'Number of Attempts {num_attempts}, Expenses: ${expenses}')
print(f'Number of Wins: {amount_wins}, Amount of Wins ${earnings}')
print(f'Winning amount ${winnings}')
print(f'Net Winning Amount ${net_winnings_balance}\n')

print(f'''Winning Stats: 
0 numbers match = {winning_stats[0]}, ${winning_stats[0]*(-2)}
1 number match = {winning_stats[1]}, ${winning_stats[1]*winning_amounts[1]}
2 number match = {winning_stats[2]}, ${winning_stats[2]*winning_amounts[2]}
3 number match = {winning_stats[3]}, ${winning_stats[3]*winning_amounts[3]}
4 number match = {winning_stats[4]}, ${winning_stats[4]*winning_amounts[4]}
5 number match = {winning_stats[5]}, ${winning_stats[5]*winning_amounts[5]}
6 number match = {winning_stats[6]}, ${winning_stats[6]*winning_amounts[6]}''')



# END

#        .-""""-.        .-""""-.
#       /        \      /        \
#      /_        _\    /_        _\
#     // \      / \\  // \      / \\
#     |\__\    /__/|  |\__\    /__/|
#      \    ||    /    \    ||    /
#       \        /      \        /
#        \  __  /        \  __  / 
#         '.__.'          '.__.'
#          |  |            |  |
#          |  |            |  |