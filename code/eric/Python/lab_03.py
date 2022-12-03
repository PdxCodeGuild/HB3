# CC validation lab


card_number = list(input("Enter a credit card number: ").replace(" ", ""))
print(' '.join(card_number))

def check(card_number):
# remove the last digit   
    check_digit = card_number.pop()
    print(' '.join(card_number))
# reverse the numbers
    card_number.reverse()
    print(' '.join(card_number))
# double every other digit in the reversed list
    card_number = [int(x) for x in card_number]
    doub_2nd_num = list()
    digits = list(enumerate(card_number, start=1))
    for index, digit in digits:
        if index % 2 != 0:
            doub_2nd_num.append(digit * 2)
        else: 
            doub_2nd_num.append(digit)
    print(*doub_2nd_num)
# subtract nine from numbers over nine
    doub_2nd_num = [x - 9 if (x > 9) else x for x in doub_2nd_num]
    print(*doub_2nd_num)
# sum all the values
    sum_num = sum(doub_2nd_num)
    print(sum_num)
# take the second digit 
    last_digit = sum_num % 10
    print(last_digit)
# check digits
    if bool(last_digit == int(check_digit)):
        print ("Valid!")
    else:
        print("Invalid!")
check(card_number)