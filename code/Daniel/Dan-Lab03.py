#---------------------------------
# PDX Code Guild: HB3
# Lab03: Credit Card Validation
# Author: Daniel Smith
# Date: 2022.11.22
#---------------------------------


# write a function which returns whether a string containing a credit card number is valid as a boolean.
def is_valid(num):
    # Convert the input string into a list of ints
    num_list = [int(digit) for digit in num]

    # Slice off the last digit. That is the check digit.
    check_digit1 = num_list.pop()

    # Reverse the digits.
    num_list.reverse()

    # Double every other element in the reversed list.
    # num_list[::2] = [index*2 for index in num_list[::2]] ### Advanced alternative method.
    for index in range(len(num_list)):
        if index % 2 == 0:
            num_list[index] *= 2

    # Subtract nine from numbers over nine.
    for index in range(len(num_list)):
        if num_list[index] > 9:
            num_list[index] -= 9

    # Sum all values.
    num_sum = sum(num_list)

    # Take the second digit of that sum.
    # Convert num_sum to a str to access the char at index 1, then return that value as an int.
    check_digit2 = int(str(num_sum)[1])

    # If that matches the check digit, the whole card number is valid.
    if check_digit1 == check_digit2:
        return True
    else:
        return False


num = str(4556737586899855)
valid = is_valid(num)
print(valid)