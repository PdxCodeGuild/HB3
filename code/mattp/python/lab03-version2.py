print('\t\n Number to Phrase Lab: Version 2')

ones = {
    0: ' ',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}

tens = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
}

hundreds = {
    1: 'a hundred',
    2: 'two hundred',
    3: 'three hundred',
    4: 'four hundred',
    5: 'five hundred',
    6: 'six hundred',
    7: 'seven hundred',
    8: 'eight hundred',
    9: 'nine hundred'
}

number_input = input('\n\tSelect a number (000-999): ')

number_input = int(number_input)

hundred_digit = number_input//100
tens_digit = number_input//10
ones_digit = number_input%10

special_tens_digit = (int(number_input * .1) % 10)
special_ones_digit = number_input%10


#print(f'\n\t{number_input} spelled out is: {small_number}')


if (number_input >= 1) and (number_input <= 19):
    small_word = ones[number_input]
    print(f'\n\t{number_input} spelled out is: {small_word}')
    
elif (number_input >= 20) and (number_input <= 99):
    tens_word = tens[tens_digit]
    ones_word = ones[ones_digit]
    print(f'\n\t{number_input} spelled out is: {tens_word} {ones_word}')
    
elif number_input >= 100:
    hundred_word = hundreds[hundred_digit]
    tens_word = tens[special_tens_digit]
    ones_word = ones[ones_digit] 
    print(f'\n\t{number_input} spelled out is: {hundred_word} & {tens_word} {ones_word}')
    
