#---------------------------------
# PDX Code Guild: HB3
# Lab04: Blackjack
# Author: Daniel Smith
# Date: 2022.11.23
#---------------------------------

def blackjack(hand):
    # This function gives basic blackjack playing advice during a game based on the user's 3-card hand.

    # Point values of every card (consider Aces as 1 point ea).
    card_value = {
        'A':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        'J':10,
        'Q':10,
        'K':10,
        }

    # Total value of the hand (consider Aces as 1 point ea).
    hand_value = card_value[hand[0]] + card_value[hand[1]] + card_value[hand[2]]

    # Explicitly handle Aces:
    if 'A' in hand and hand_value <= 11:
        hand_value += 10

    # Print out the hand value and the advice.
    # Less than 17, advise to "Hit"
    if hand_value < 17:
        return f'{hand_value} Hit'
    # Greater than or equal to 17, but less than 21, advise to "Stay"
    elif 17 <= hand_value < 21:
        return f'{hand_value} Stay'
    # Exactly 21, advise "Blackjack!"
    elif hand_value == 21:
        return f'{hand_value} Blackjack!'
    # Over 21, advise "Already Busted"
    else:
        return f'{hand_value} Already Busted'


# Ask the user for three playing cards, then
# pass the cards to the blackjack function, then
# return the result & pass it to the terminal.
hand = ['','','']
print('\nCard Choices: A, 2, 3, 4, 5, 6, 7, 8, 9, J, Q, K')
hand[0] = input('What\'s your first card? ').upper()
hand[1] = input('What\'s your second card? ').upper()
hand[2] = input('What\'s your third card? ').upper()
print(blackjack(hand))

# Note: should probably handle everything inside the function. Is it odd the function calls for a specific list of 3 values?
