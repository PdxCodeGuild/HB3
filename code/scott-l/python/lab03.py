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


def credit_card_validation(credit_card_input):

    # STEP 1:---------------
    #     Convert the input string into a list of ints
    print(f'Credit card string input {credit_card_input}')
    # split a string into a list, this will split on whitespace
    list_numbers = credit_card_input.split()
    # print(f'Split string into a list {list_numbers}')  # DEBUG CODE
    # convert the list numbers list of strings into integer types using short hand for loop
    int_list = [int(num) for num in list_numbers]
    # print(f'Convert the list strings to integers {int_list}')  # DEBUG CODE

    # STEP 2: ---------------
    #     Slice off the last digit. That is the check digit.
    int_list_slice = int_list[0:(len(int_list)-1):]
    # print(f'Slice off the last digit {int_list_slice}')  # DEBUG

    # STEP 3: --------------------
    #     Reverse the digits.
    int_list_slice.reverse()
    int_list_reverse = int_list_slice
    # print(f'Reverse the digits {int_list_reverse}')  # DEBUG

    # STEP 4: --------------------
    #     Double every other element in the reversed list.
    double_odd_list = []
    for n in range(len(int_list_reverse)):
        # compare the index value of the list and if the index is odd 
        # then append the value into a list and double the number
        if n%2 == 0:
            double_odd_list.append(int_list_reverse[n]*2)
            # print(double_odd_list)  # DEBUG
        # if the index is odd just append the value and continue
        else:
            double_odd_list.append(int_list_reverse[n])
            # print('Continue')  # DEBUG
            continue # skip the rest fo this iteration and begin the next loop
        # end if
    # end for
    # print(f'Double odd index of each unit {double_odd_list}')  # DEBUG 

    # STEP 5: -------------------------
    #     Subtract nine from numbers over nine.

    nine_less_list = []
    for n in double_odd_list:
        # list value is > 9 then subtract 9 
        # then append the value into a list and double the number
        if n > 9:
            nine_less_list.append(n-9)
            # print(nine_less_list)  # DEBUG
        # else if the value is less than 9 append and then continue
        else:
            nine_less_list.append(n)
            # print('Continue')  # DEBUG
            continue # skip the rest fo this iteration and begin the next loop
        # end if
    # end for 
    # print(f'Values over nine subtract nine {nine_less_list}')  # DEBUG

    # STEP 6:--------------------------------
    #     Sum all values.
    sum_value = 0
    for n in nine_less_list:
        sum_value = sum_value + n
    # end for
    # print(f'Sum all values {sum_value}')  # DEBUG

    # STEP 7: --------------------------------
    #     Take the second digit of that sum.
    # convert the number into a string
    string_val = str(sum_value)
    # take the second digit of the sum
    string_val = str(string_val[1])  
    # convert back into int
    string_val_int = int(string_val)
    # print(f'Take the second digit of the sum {string_val_int}')  # DEBUG

    # STEP 8:------------------------------
    #     If that matches the check digit, the whole card number is valid.

    # if the digit is equal to the whole card number at the end
    if string_val_int == int_list[-1]:
        # print("Valid Card Number") # DEBUG
        # print(int_list[-1])   # DEBUG
        valid_flag = True
    else:
        # print("Invalid Card Number")
        # print(int_list[-1]) # DEBUG
        valid_flag = False
    # end if

    return valid_flag
# end function credit_card_validation

#-------------------------------------------------------
 # BEGIN PROGRAM
 # Credit Card Example Test String
credit_card_input = '4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5'
# rund credit_card_validation function with test string
valid = credit_card_validation(credit_card_input)
# If valid is True then Valid Number
if valid:
    print("Valid Number")
# else if valid is false then Invalid Number
else:
    print("Invalid Number!")
# end if

# END PROGRAM

#           (                 ,&&&.
#             )                .,.&&
#            (  (              \=__/
#                )             ,'-'.
#          (    (  ,,      _.__|/ /|
#           ) /\ -((------((_|___/ |
#         (  // | (`'      ((  `'--|
#       _ -.;_/ \\--._      \\ \-._/.
#      (_;-// | \ \-'.\    <_,\_\`--'|
#      ( `.__ _  ___,')      <_,-'__,'
#       `'(_ )_)(_)_)'
