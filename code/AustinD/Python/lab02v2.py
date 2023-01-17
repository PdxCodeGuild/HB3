# Number = word
first_and_third_digit_words = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
# First digit key for combination with other dict value, shared value for hundreds
second_digit_words = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
# First digit check uniquely identifies the unique numbers 10-19
unique_words = {0:'ten',1:'eleven',2:'twelve',3:'thirteen',4:'fourteen',5:'fifteen',6:'sixteen',7:'seventeen',8:'eighteen',9:'nineteen'}

def main():
    number = (input('Enter a number from 0-999:'))
    # Turned into list to make the entry indexable to grab keys
    digits = list(number)
    # Length as basis for conditions
    digit_length = (len(number))
    # Check single digit first
    if digit_length < 2:
        word = first_and_third_digit_words.get(int(digits[0]))
        print(word)
        return
    # Check two digit words with conditionals for zero in the single digit or uniques
    elif digit_length == 2:
        if int(digits[0]) !=1:
            if int(digits[1]) !=0:
                word = second_digit_words.get(int(digits[0]))+" "+first_and_third_digit_words.get(int(digits[1]))
                print(word)
                return
            else:
                word = second_digit_words.get(int(digits[0]))
                print(word)
                return
        else:
            word = unique_words.get(int(digits[1]))
            print(word)
            return
    # Checks for triple digit words with conditionals for zero, second digit no third digit, third digit but no second digit, and uniques
    else: 
        if int(digits[2]) !=0 and int(digits[1] !=0):
                if int(digits[1]) !=0:
                    if int(digits[1]) !=1:
                        if int(digits[2]) !=0:
                            word = first_and_third_digit_words.get(int(digits[0]))+" hundred "+second_digit_words.get(int(digits[1]))+" "+first_and_third_digit_words.get(int(digits[2]))
                            print(word)
                            return
                    else: 
                        word = first_and_third_digit_words.get(int(digits[0]))+" hundred and "+unique_words.get(int(digits[2]))
                        print(word)
                        return
                else:
                    word = first_and_third_digit_words.get(int(digits[0]))+" hundred and "+first_and_third_digit_words.get(int(digits[2]))
                    print(word)
                    return
        else: 
            if int(digits[1]) !=0:
                word = first_and_third_digit_words.get(int(digits[0]))+" hundred and "+second_digit_words.get(int(digits[1]))
                print(word)
                return
            else:
                word = first_and_third_digit_words.get(int(digits[0]))+" hundred"
                print(word)
                return
main()
