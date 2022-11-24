# user input
# card_num = input('Enter card to validate: ')
# define a function to validate credit card
def validate_card(num):
    card_list = []
    card_list[:0] = num[:-1:]
    card_list.reverse()
    card_list = [int(x) for x in card_list]
    card_list[::2] = [x*2 for x in card_list[::2]]
    #card_list[::] = [x-9 for x  in card_list[::]]
    return card_list

card_num = input('Enter card to validate: ')    
# cards = validate_card(card_num)
print(validate_card(card_num))
   