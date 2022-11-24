print('\n\tNumber to Phrase Lab: Version 1')

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

number_input = input('\n\tSelect a number (00-99): ')

number_input = int(number_input)

tens_digit = number_input//10
ones_digit = number_input%10


#print(f'\n\t{number_input} spelled out is: {small_number}')


if (number_input >= 1) and (number_input <= 19):
    small_word = ones[number_input]
    print(f'\n\t{number_input} spelled out is: {small_word}')
    
elif number_input >= 20:
    tens_word = tens[tens_digit]
    ones_word = ones[ones_digit]
    
    print(f'\n\t{number_input} spelled out is: {tens_word} {ones_word}')

    
    