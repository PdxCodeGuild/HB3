#For use in step 4 of validation
def double(x):
    return x*2

#For use in step 5 of validation
def subtract_9_if_over_9(x):
    if x > 9:
        return x-9
    else:
        return x

def creditcard():
    entry = input('Enter a credit card number with no spaces:')
    #Converts the input string into a list of ints
    cc = list(map(int, list(entry)))
    #Slices off the last digit, assigned as check digit variable.
    check_digit = cc[-1]
    #Reverses the digits
    validation_digits = cc[-2::-1]
    #Doubles every other digit with double function
    validation_digits [0::2] = map(double,validation_digits[0::2])
    #Subtracts 9 from every number over 9 with the subtrat_9_if_over_9 function
    validation_digits = list(map(subtract_9_if_over_9, validation_digits))
    #Sums all values
    validation_digits = sum(validation_digits)
    #Checks the second digit of the sum against the check digit for invalid and valid credit card numbers
    if str(check_digit) != str(validation_digits)[-1]:
        return False
    else:
        return True

print(creditcard())