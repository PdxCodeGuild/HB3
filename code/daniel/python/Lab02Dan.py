#---------------------------------
# PDX Code Guild: HB3
# Lab02: Number to Phrase
# Author: Daniel Smith
# Date: 2022.11.18
#---------------------------------

# Convert a given number into its english representation.
# For example: 67 becomes 'sixty-seven'. Handle numbers from 0-999.

def number_to_words(num):

    # Collect the number's length.
    length = len(str(num))

    # Reject bad input outside of limits.
    if (length == 0) or (length > 3):
        print('Error. Please enter a number 0-999.')
        return

    # Explicitly handle zero.
    if num == 0:
        print('zero')
        return

    # Initiate list of word strings for numbers 0-19.
    zero_to_19 = ['', 'one', 'two', 'three', 'four', 'five', 
        'six', 'seven', 'eight', 'nine', 'ten', 
        'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 
        'sixteen', 'seventeen', 'eighteen', 'nineteen']

    # Initiate list of word strings for the tens digit.
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 
    'sixty', 'seventy', 'eighty', 'ninety']

    # Convert the integer num input to a list of integers.
    # num = str(num)
    num = list(map(int, str(num)))

    # For one digit numbers.
    if length == 1:
        print(zero_to_19[num[-1]])
        return

    # For two digit numbers.
    if length == 2:
        # For 10-19
        if num[-2] == 1:
            print(zero_to_19[num[-1]+10])
            return
        # For 20-99
        else:
            print(tens[num[-2]] + ' ' + zero_to_19[num[-1]])
            return

    # For 3 digit numbers.
    if length == 3:
        hundreds = f'{zero_to_19[num[-3]]} hundred'
        # For X10-X19
        if num[-2] == 1:
            print(hundreds + ' ' + zero_to_19[num[-1]+10])
            return
        # For X20-X99
        else:
            print(hundreds + ' ' + tens[num[-2]] + ' ' + zero_to_19[num[-1]])
            return

num = int(input('Please enter a number 0-999: '))
num_in_words = number_to_words(num)