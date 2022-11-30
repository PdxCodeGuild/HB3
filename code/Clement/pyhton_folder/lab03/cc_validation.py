print("\nWelcome To Credit Card Validation!!!!!!!\n")
print("Let check for a valid credit card numbers\n")

def is_valid():

    # Convert the input string into a list of ints
    c_card_num = list(input("Please enter your sixteen digit credit card number:\n"))

    # Slice off the last digit
    check_digit = (c_card_num[15:16])

    # new list after slicing the last digit
    c_card_num = c_card_num[:15]

    # slicing and saving it here as (check_d)
    check_d = int(check_digit[0])

    # Reverse the digits from end to start.
    c_card_num.reverse()
    doubled_digit = []

    # conditional statements to validate a card number
    for x in range(len(c_card_num)):
        credit_card = c_card_num[x]
        if x % 2 == 0:

    # Double every other element in the reversed list and subtract nine from numbers over nine.
            c_doubled_num = int(credit_card) * 2
            if c_doubled_num > 9:
                c_doubled_num -= 9
            doubled_digit.append(c_doubled_num)

        else:
            doubled_digit.append(int(credit_card))

    sum_all_values = sum(doubled_digit)
    total_num = sum_all_values % 10
    if total_num == int(check_d):
        return True

    else:
        return False

print(is_valid())