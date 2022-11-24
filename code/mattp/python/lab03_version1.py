print('\n\tCredit Card Validation Lab')

import string

credit_card_number = input('\nInput a FAKE credit card number (16 digits): ')


####### Part 1 #######

digits = [int(digit) for digit in str(credit_card_number)]
print(f'\n\t1. {digits}')

####### Part 2 #######

check_digit = digits[-1]
digits.pop()
print(f'\n\t2. {digits}')
      
####### Part 3 #######

digits.reverse()
print(f'\n\t3. {digits}')

####### Part 4 #######

digits2 = digits[:]
digits2[::2] = [digit*2 for digit in digits2[::2]]
print(f'\n\t4. {digits2}')

####### Part 5 #######

digits3 = []
for digit in digits2:
     
    if digit > 9:
        digit -= 9
        digits3.append(digit)
    else:
        digits3.append(digit)
print(f'\n\t5. {digits3}')

####### Part 6 #######

print(f'\n\t6. {sum(digits3)}')

####### Part 7 #######

print(f'\n\t7. {check_digit}')

####### Part 8 #######

if digits3[-1] == check_digit:
    print('\n\t8. Valid!')
else:
    print('\n\t8. Invalid...bummer')



    
        



 