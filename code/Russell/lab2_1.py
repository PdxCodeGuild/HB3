numeral = input("Enter number to be converted to text ")

# isolate digits
ones_digits = int(numeral) % 10
tens_digits = int(numeral) // 10

'''
print(ones_digits)
print(tens_digits)
'''
# define textual representation
alpha_tens = ['', 'teen', 'twenty-', 'thirty-', 'forty-', 'fifty-', 'sixty-', 'seventy-', 'eighty-', 'ninety-']

alpha_ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


# put it all together

if ones_digits == 0 and tens_digits == 1:
    alpha_num = 'ten'

elif tens_digits == 1 and ones_digits == 1:
    alpha_num = 'eleven'

elif tens_digits == 1 and ones_digits == 2:
    alpha_num = 'twelve'

elif tens_digits == 1 and ones_digits == 3:
    alpha_num = 'thirteen'

elif tens_digits == 1 and ones_digits == 5:
    alpha_num = 'fifteen'    

elif tens_digits == 1 and ones_digits != 0 and ones_digits != 1 and ones_digits != 2 and ones_digits != 3:
    alpha_num = alpha_ones[ones_digits] + alpha_tens[tens_digits]

else:
    alpha_num = alpha_tens[tens_digits] + alpha_ones[ones_digits]

print(alpha_num)