numeral = input("Enter number to be converted to text ")


ones_digit = int(numeral) % 10
tens_digit = (int(numeral) // 10) % 10
hundreds_digit = (int(numeral) // 100) % 10


# print(ones_digit)
# print(tens_digit)
# print(hundreds_digit)


alpha_hundreds = ['', 'one hundred ', 'two hundred ', 'three hundred ', 'four hundred ', 
'five hundred ', 'six hundred ', 'seven hundred ', 'eight hundred ', 'nine hundred ']

alpha_tens = ['', 'teen', 'twenty-', 'thirty-', 'forty-', 'fifty-', 'sixty-', 'seventy-', 'eighty-', 'ninety-']

alpha_ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

if int(numeral) > 99:
    new_num = int(numeral) - hundreds_digit * 100
    # print(hundreds_digit)
    # print(new_num)

    if int(new_num) == 10:
        alpha_num = alpha_hundreds[hundreds_digit] + 'ten'

    elif int(new_num) == 11:
        alpha_num = alpha_hundreds[hundreds_digit] + 'eleven'

    elif int(new_num) == 12:
        alpha_num = alpha_hundreds[hundreds_digit] + 'twelve'

    elif int(new_num) == 13:
        alpha_num = alpha_hundreds[hundreds_digit] + 'thirteen'

    elif int(new_num) == 15:
        alpha_num = alpha_hundreds[hundreds_digit] + 'fifteen'    

    else:
        if ones_digit == 0:
            alpha_num = alpha_hundreds[hundreds_digit] + alpha_tens[tens_digit] 
        else: 
            alpha_num = alpha_hundreds[hundreds_digit] + alpha_tens[tens_digit] + alpha_ones[ones_digit]



    print(alpha_num)

else:

    if int(numeral) == 10:
        alpha_num = 'ten'

    elif int(numeral) == 11:
        alpha_num = 'eleven'

    elif int(numeral) == 12:
        alpha_num = 'twelve'

    elif int(numeral) == 13:
        alpha_num = 'thirteen'

    elif int(numeral) == 15:
        alpha_num = 'fifteen'    

    else:
        alpha_num = alpha_tens[tens_digit] + alpha_ones[ones_digit]



    print(alpha_num)