print('\n\tLab 04. Blackjack Advice Lab: Version 1')

card_values = {
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
    
print('\n\tThis is a card game.  \n\tYou can select the value of card: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q or K).')

card_1_input = input('\n\tWhat is your first card: ')
card_2_input = input('\n\tWhat is your second card: ')
card_3_input = input('\n\tWhat is your third card: ')

card_1 = card_values[card_1_input]
card_2 = card_values[card_2_input]
card_3 = card_values[card_3_input]

print(card_1, card_2, card_3)

card_count = card_1 + card_2 + card_3

if card_count < 17:
    print(f'\n\t{card_count}, that is low: Hit!')
elif 17 <= card_count < 21:
    print(f'\n\t{card_count} is good: Stay!')
elif card_count == 21:
    print(f'\n\t{card_count} Blackjack!')
else:
    print(f'\n\t{card_count} Already Busted...bummer')
    

    