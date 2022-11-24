
'''
 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
      Project: HB3 - Lab 04 Blackjack Advice
      Author: Scott Lefgren
      Email: scojlefg@gmail.com
      Date: November 23, 2022
 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
'''

# Let's write a python program to give basic blackjack playing advice during 
# a game by asking the player for cards. First, ask the user for three 
# playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, 
# figure out the point value of each card individually. Number cards 
# are worth their number, all face cards are worth 10. At this point, 
# assume aces are worth 1. Use the following rules to determine the advice:

#     Less than 17, advise to "Hit"
#     Greater than or equal to 17, but less than 21, advise to "Stay"
#     Exactly 21, advise "Blackjack!"
#     Over 21, advise "Already Busted"

# Print out the current total point value and the advice.

# What's your first card? Q
# What's your second card? 2
# What's your third card? 3
# 15 Hit

# What's your first card? K
# What's your second card? 5
# What's your third card? 5
# 20 Stay

# What's your first card? Q
# What's your second card? J
# What's your third card? A
# 21 Blackjack!

# --------------------------------------------------------------------
# BEGIN

# Create a dictionary of playing cards
# playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)
playing_cards = {  # playing card name: points
    'A': 1,   # Ace
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,   # Jack
    'Q': 10,   # Queen
    'K': 10    # King
}

# Ask the player for cards
print(f'''
Welcome to the game of Blackjack
Enter the values of the following playing cards:
(A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)'''
)

first_card = input("What's your first card? ")
second_card = input("What's your second card? ")
third_card = input("What's your third card? ")

# figure out the point value of each card individually
first_card_val = playing_cards[first_card]
second_card_val = playing_cards[second_card]
third_card_val = playing_cards[third_card]
print(f'Cards Chosen {first_card_val}, {second_card_val}, {third_card_val}')

card_sum = first_card_val + second_card_val + third_card_val
print(f'Total Card Sum {card_sum}')

#     Less than 17, advise to "Hit"
#     Greater than or equal to 17, but less than 21, advise to "Stay"
#     Exactly 21, advise "Blackjack!"
#     Over 21, advise "Already Busted"
if card_sum < 17:
    print(f'{card_sum} Hit')
elif card_sum > 17 and card_sum < 21:
    print(f'{card_sum} Stay')
elif card_sum == 21:
    print(f'{card_sum} BlackJack!')
elif card_sum > 21:
    print(f'{card_sum} Already Busted')
# end if


