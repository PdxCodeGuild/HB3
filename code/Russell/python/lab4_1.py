player_cards = []

value_dict = {
            'A' : 1,
            'J' : 10,
            'Q' : 10,
            'K' : 10
        }

player_cards.append(input("What is your first card? ").upper())
player_cards.append(input("What is your second card? ").upper())
player_cards.append(input("What is your third card? ").upper())

card_value = 0
import string

for card in player_cards:
    if card in string.digits and int(card) in range(1, 10):
        card_value += int(card)
        
    else:
        card_value += value_dict[card]
        
# print(f"Your cards - {player_cards}")
# print(f"Total value of cards - {card_value}")

if card_value < 17:
    print(f"{card_value} - Hit")

elif card_value >= 17 and card_value < 21:
    print(f"{card_value} - Stay")

elif card_value == 21:
    print(f"{card_value} - Blackjack!")

else:
    print(f"{card_value} - Busted!")