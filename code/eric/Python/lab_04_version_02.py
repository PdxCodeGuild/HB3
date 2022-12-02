# LAB 4 - Blackjack advice

import random
cards = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}
card_keys = list(cards.keys())
card_1 = random.choice(card_keys)
card_2 = random.choice(card_keys)
card_3 = random.choice(card_keys)

print("What's your first card? ", card_1)
print("What's your second card? ", card_2)
print("What's your third card? ", card_3)


sum = cards[card_1] + cards[card_2] + cards[card_3]

if sum < 21 and (card_1 or card_2 or card_3) == 'A':
    first_two = (cards[card_1] + cards[card_2])
    second_two = (cards[card_2] + cards[card_3])
    if first_two <= 10 and card_3 == 'A':
        sum = first_two + 11
    if card_1 == 'A' and second_two <= 10:
        sum = second_two + 11

if sum < 17:
    print(sum, 'Hit')
elif sum >= 17 and sum < 21:
    print(sum, 'Stay')
elif sum == 21:
    print(sum, 'Blackjack!')
else:
    print(sum, 'Already Busted')
