# define a function to validate credit card
def validate_card(num):
    card_list = []
    card_list[:0] = num
    card_list = [int(x) for x in card_list]
    card_list2 = card_list[:-1]
    card_list2.reverse()
    card_list2[::2] = [x*2 for x in card_list2[::2]]
    card_list2[::] = [x - 9 if (x > 9) else x for x in card_list2[::]]
    card_list2 = sum(card_list2)
    card_list2 = [int(x) for x in str(card_list2)]

    if card_list[-1] == card_list2[-1]:
        return 'Valid!'
    else:
        return 'Invalid Card!'

card_num = input('Enter card to validate: ')    
# cards = validate_card(card_num)
print(validate_card(card_num))
   