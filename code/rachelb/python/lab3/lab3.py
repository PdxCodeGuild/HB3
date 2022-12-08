#make list
card_num = [4,5,5,6,7,3,7,5,8,6,8,9,9,8,5,5] #----- 4556737586899855

# new_card = (card_num[0:15])    #step 2: slicing

# new_card.reverse()             #step 3: reverse


def cardvalidation():
    num = []
    user_input = input('Enter card number: ')
    for number in user_input:
        num.append(number)
    card_num = (num[0:15])    #--------splice Q & A
    card_num.reverse() 
    for x in range(len(card_num)):
        if x % 2 == 0:
            card_num[x]*2
    print(card_num)
 # Subtract nine from numbers over nine.
    for x in range(len(card_num)):
            if int(card_num[x]) > 9:
                int(card_num[x]) - 9 
    # return card_num
    total = sum(int(card_num))
    print(total)
    remainder = total % 10 
    if total == remainder():
        return True
    else:
        return False

cardvalidation()            
# total = sum(card_num)
# print(total)

# remainder = total % 10 
# print(remainder)

# if total == remainder():
#     return True
# else:
#     return False

# Subtract
# def num(x):
#     if x in (10, 18, 16, 14,):
#         return x - 9
#     else:
#         return x


    

# multiply = [1 * num for num in card_num]  #step 4: multiply each item in the list by 2

# subtraction = [n - 9 for n in multiply if multiply <= 9]


        
# print(new_card)
# subtraction = [n - 9 for n in card_num if card_num <= 9]
# print(subtraction)


