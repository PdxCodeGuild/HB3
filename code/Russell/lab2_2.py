numeral = int(input("Enter number to be converted to text "))


ones_digit = numeral % 10
tens_digit = (numeral // 10) % 10
hundreds_digit = (numeral // 100) % 10


alpha_hundreds = ['', 'one hundred ', 'two hundred ', 'three hundred ', 'four hundred ', 
'five hundred ', 'six hundred ', 'seven hundred ', 'eight hundred ', 'nine hundred ']

alpha_tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

alpha_ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

alpha_teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

if numeral > 99:
    if numeral % 100 >= 10 and numeral % 100 <= 19:
        print(alpha_hundreds[hundreds_digit] + alpha_teens[(numeral % 100)%10])
    
    else:
        if ones_digit == 0:
           print(alpha_hundreds[hundreds_digit] + alpha_tens[tens_digit])
        
        elif tens_digit == 0:
            print(alpha_hundreds[hundreds_digit] + alpha_tens[tens_digit] + alpha_ones[ones_digit])

        else: 
            print(alpha_hundreds[hundreds_digit] + alpha_tens[tens_digit] + '-' + alpha_ones[ones_digit])

else:

    if numeral >= 10 and numeral <= 19:
        print(alpha_teens[(numeral % 100)%10])

    else:

        if ones_digit == 0 and numeral > 0:
           print(alpha_tens[tens_digit])
        
        elif tens_digit == 0:
            print(alpha_tens[tens_digit] + alpha_ones[ones_digit])

        else: 
            print(alpha_tens[tens_digit] + '-' + alpha_ones[ones_digit])