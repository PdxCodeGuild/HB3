# user input
card_num = input('Enter card to validate: ')
# define a function to validate credit card
def validate_card(num):
    card_list = []
    card_list[:0] = num
    slice_num = num[:-1:]
    return slice_num
     
cards = validate_card(card_num)
print(cards)
    