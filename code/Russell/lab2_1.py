numeral = int(input("Enter number to be converted to text "))

# hey this is new

ones_digit = int(numeral) % 10
tens_digit = int(numeral) // 10


alpha_teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

alpha_tens = ['', 'teen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

alpha_ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

if numeral >= 10 and numeral <= 19:
        print(alpha_teens[(numeral % 100)%10])

else:

    if ones_digit == 0 and numeral > 0:
        print(alpha_tens[tens_digit])
    
    elif tens_digit == 0:
        print(alpha_tens[tens_digit] + alpha_ones[ones_digit])

    else: 
        print(alpha_tens[tens_digit] + '-' + alpha_ones[ones_digit])