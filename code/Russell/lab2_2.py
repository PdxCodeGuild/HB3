numeral = input("Enter number to be converted to text ")


ones_digit = int(numeral) % 10
tens_digit = (int(numeral) // 10) % 10
hundreds_digit = (int(numeral) // 100) % 10


print(ones_digit)
print(tens_digit)
print(hundreds_digit)

alpha_hundreds = ['', 'one hundred ', 'two hundred ', 'three hundred ', 'four hundred ', 
'five hundred ', 'six hundred ', 'seven hundred ', 'eight hundred ', 'nine hundred ']

alpha_tens = ['', 'teen', 'twenty-', 'thirty-', 'forty-', 'fifty-', 'sixty-', 'seventy-', 'eighty-', 'ninety-']

alpha_ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


if ones_digit == 0 and tens_digit == 1:
    alpha_num = 'ten'

elif tens_digit == 1 and ones_digit == 1:
    alpha_num = 'eleven'

elif tens_digit == 1 and ones_digit == 2:
    alpha_num = 'twelve'

elif tens_digit == 1 and ones_digit == 3:
    alpha_num = 'thirteen'

elif tens_digit == 1 and ones_digit == 5:
    alpha_num = 'fifteen'    

elif tens_digit == 1 and ones_digit != 0 and ones_digit != 1 and ones_digit != 2 and ones_digit != 3:
    alpha_num = alpha_ones[ones_digit] + alpha_tens[tens_digit]

else:
    alpha_num = alpha_hundreds[hundreds_digit] + alpha_tens[tens_digit] + alpha_ones[ones_digit]



print(alpha_num)