#---------------------------------
# PDX Code Guild: HB3
# Lab04: Blackjack
# Author: Daniel Smith
# Date: 2022.11.23
#---------------------------------

def blackjack(hand):
    # A program that gives basic blackjack playing advice during a game depending on the user's hand of 3 cards.

    # Point values of each card.
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

    # Sum the total value of the hand (consider Aces 1 point ea).
    hand_value = card_value[hand[0]] + card_value[hand[1]] + card_value[hand[2]]

    # Explicitly handle Aces:
    if 'A' in hand and hand_value <= 11:
        hand_value += 10

    # Print out the total hand value and the advice.
    # Less than 17, advise to "Hit"
    if hand_value < 17:
        print(f'{hand_value} Hit')
        return
    # Greater than or equal to 17, but less than 21, advise to "Stay"
    elif 17 <= hand_value < 21:
        print(f'{hand_value} Stay')
        return
    # Exactly 21, advise "Blackjack!"
    elif hand_value == 21:
        print(f'{hand_value} Blackjack!')
        return
    # Over 21, advise "Already Busted"
    else:
        print(f'{hand_value} Already Busted')
        return


# Ask the user for three playing cards, and pass the cards to the blackjack function.
print('Card choices: 2, 3, 4, 5, 6, 7, 8, 9, J, Q, K, A')
hand = ['','','']
hand[0] = input('What\'s your first card? ').upper()
hand[1] = input('What\'s your second card? ').upper()
hand[2] = input('What\'s your third card? ').upper()
blackjack(hand)