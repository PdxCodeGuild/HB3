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
    num_length = len(str(num))

    # Reject bad input outside of limits.
    if (num_length == 0) or (num_length > 3):
        print('Error. Please enter a number 0-999.')
        return

    # Explicitly handle zero.
    if num == 0:
        print('zero')
        return

    # List of word strings for numerals 0-19.
    zero_to_19 = ['', 'one', 'two', 'three', 'four', 'five', 
        'six', 'seven', 'eight', 'nine', 'ten', 
        'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 
        'sixteen', 'seventeen', 'eighteen', 'nineteen']

    # List of word strings for the tens digit.
    tens = ['', '', 'twenty ', 'thirty ', 'forty ', 'fifty ', 
    'sixty ', 'seventy ', 'eighty ', 'ninety ']

    # Convert num variable (int) to list (of ints).
    # num = list(map(int, str(num))) # Alternative method.
    num = [int(digit) for digit in str(num)] # Append digit as integer to num list for each digit in num variable. Num list overwrites num variable.

    # For one digit numbers.
    if num_length == 1:
        print(zero_to_19[num[-1]])
        return

    # For two digit numbers.
    if num_length == 2:
        # For 10-19
        if num[-2] == 1:
            print(zero_to_19[num[-1]+10])
            return
        # For 20-99
        else:
            print(tens[num[-2]] + ' ' + zero_to_19[num[-1]])
            return

    # For 3 digit numbers.
    if num_length == 3:
        hundreds = f'{zero_to_19[num[-3]]} hundred '
        # For X10-X19
        if num[-2] == 1:
            print(hundreds + zero_to_19[num[-1]+10])
            return
        # For X20-X99
        else:
            print(hundreds + tens[num[-2]] + zero_to_19[num[-1]])
            return

num = int(input('Please enter a number 0-999: '))
num_in_words = number_to_words(num)