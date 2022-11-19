'''
 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
      Project: HB3 - Lab 02 version 1
      Author: Scott Lefgren
      Email: scojlefg@gmail.com
      Date: November 18, 2022
                    ___-___  o==o======   .   .   .   .   .
            =========== ||//
                    \ \ |//__
                    #_______/
                    
 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
'''
# Version 1
# Number to Phrase

# Convert a given number into its english representation. 
# For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

# Hint: you can use modulus to extract the ones and tens digit.

# x = 67
# tens_digit = x//10
# ones_digit = x%10

# Hint2: use the digit as an index to look up a string in a list.


# Create a Dictionary index for each of the digits
english_num = {
    1 : 'one',2 : 'two',3 : 'three', 4 : 'four', 5 : 'five',
    6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
    16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
    20: 'twenty',30: 'thirty', 40: 'forty', 50: 'fifty',60: 'sixty', 
    70: 'seventy', 80: 'eighty', 90: 'ninety'
}