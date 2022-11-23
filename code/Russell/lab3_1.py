card_number = '4556737586899855'
#card_number.split()
print(card_number)

number_as_int = [int(x) for x in card_number]
print(number_as_int)

check_digit = number_as_int[15]
print(check_digit)

number_as_int = number_as_int[0:15]
number_as_int.reverse()
print(number_as_int)

