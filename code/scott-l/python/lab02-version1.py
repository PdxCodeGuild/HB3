'''
 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
      Project: HB3 - Lab 02 version 1
      Author: Scott Lefgren
      Email: scojlefg@gmail.com
      Date: November 21, 2022
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

#-BEGIN

# Create a English Dictionaries index for each of the digits between 0-99
english_ones_digit = {
    0: 'zero', 
    1 : 'one',
    2 : 'two',
    3 : 'three', 
    4 : 'four', 
    5 : 'five',
    6 : 'six', 
    7 : 'seven', 
    8 : 'eight', 
    9 : 'nine'
}

english_teens_digit = {
    0: 'ten', 
    1: 'eleven', 
    2: 'twelve', 
    3: 'thirteen', 
    4: 'fourteen',
    5: 'fifteen',
    6: 'sixteen', 
    7: 'seventeen', 
    8: 'eighteen', 
    9: 'nineteen'
}
english_tens_digit = {  
    2: 'twenty', 
    3: 'thirty', 
    4: 'forty',
    5: 'fifty', 
    6: 'sixty', 
    7: 'seventy', 
    8: 'eighty',
    9: 'ninety'
}

user_input_num = input("Enter a Number:  ")
user_input_num = int(user_input_num)  # convert input to integer
# print(user_input_num)  #DEBUG PRINT
# print(type(user_input_num))  # DEBUG PRINT

# Find the value in the tens value
tens_digit = user_input_num//10
# print(f'Ten digit', {tens_digit})  # DEBUG PRINT

# Find the value in the ones value
ones_digit = user_input_num%10
# print(f'One digit', {ones_digit})   # DEBUG PRINT

# If the one digit is 0-9 and the ten digit is 0 then use english_ones_digit
if tens_digit == 0:
    print(english_ones_digit[ones_digit])  # Condition for 0-9
# If the ten digit is 1 and ones digit is zero then use english_teens_digit with zero ones digit index
elif tens_digit == 1 & ones_digit == 0:
    print(english_teens_digit[ones_digit])  # Uniqe condition for ten
# if the ten digit is 1 and ones digits is 1-9 use the english_teens_digit
elif tens_digit == 1:
    print(english_teens_digit[ones_digit])  # conditions for 11-19
# if the ten digit is 2-9 then check the ones_digit
elif tens_digit > 1:
    # if the ones digit is 0 then use english_tens_digit 
    if ones_digit == 0:
       print(english_tens_digit[tens_digit]) 
    # Else if the ones digit is > than zero 
    else: 
       print(english_tens_digit[tens_digit] +'-'+ english_ones_digit[ones_digit]) # conditions for 20-99
    # end if     
#end if

# The End

#                 o
#            o       /
#             \     /
#              \   /
#               \ /
# +--------------v-------------+
# |  __________________      @ |
# | /          ,  ooo  \       |
# | |  ---=====|#O#### |  (\)  |
# | |          `  \ )  |       |
# | |   ,;`,      | |  |  (-)  |
# | |  // o ',    | |  |       |
# | \  ' o \ /,   | |  / :|||: |
# |  -ooo--------------  :|||: |
# +----------------------------+
#    []                    []

