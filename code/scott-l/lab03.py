'''
 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
      Project: HB3 - Lab 03 Credit Card Validation
      Author: Scott Lefgren
      Email: scojlefg@gmail.com
      Date: November 22, 2022
 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
'''

# Credit Card Validation

# Let's write a function which returns whether a string containing 
# a credit card number is valid as a boolean. The steps are as follows:

#     Convert the input string into a list of ints
#     Slice off the last digit. That is the check digit.
#     Reverse the digits.
#     Double every other element in the reversed list.
#     Subtract nine from numbers over nine.
#     Sum all values.
#     Take the second digit of that sum.
#     If that matches the check digit, the whole card number is valid.

# For example, the worked out steps would be:

#     4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
#     4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
#     5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
#     10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
#     1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
#     85
#     5
#     Valid!

# BEGIN
# STEP 1:
#     Convert the input string into a list of ints
credit_card_input = '4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5'

print(f'Credit card string input {credit_card_input}')
# split a string into a list, this will split on whitespace
list_numbers = credit_card_input.split()
print(f'Split string into a list {list_numbers}')  # DEBUG CODE
# convert the list numbers list of strings into integer types using short hand for loop
int_list = [int(num) for num in list_numbers]
print(f'Convert the list strings to integers {int_list}')  # DEBUG CODE

# STEP 2: 
#     Slice off the last digit. That is the check digit.
int_list_slice = int_list[0:(len(int_list)-1):]
print(f'Slice off the last digit {int_list_slice}')  # DEBUG

# STEP 3: 
#     Reverse the digits.
int_list_slice.reverse()
int_list_reverse = int_list_slice
print(f'Reverse the digits {int_list_reverse}')  # DEBUG

# STEP 4: 
#     Double every other element in the reversed list.
print(int_list_reverse[:len(int_list_reverse)-1:2]) # doesn't work

# int_list = [temp.append(int(list_numbers)) for temp in list_numbers]
# print(type(num))

# remove any blank spaces from string and convert the string into a int
# num = []
# for n in list_numbers:
#     if n != ' ':
#         num.append(int(n))
#         # print(n)  # DEBUG
#     # end if
# end for
# print(num)
# print(type(num))

# nums_list = list_numbers.remove(' ')
# print(nums_list)

# for n in credit_card_input:
#     num = int(n)
#     print(num)
# # end for

# Take the length of the string and convert each item as 

# list_convert = list(credit_card_input)
# list.remove(' ')
# print(list)
