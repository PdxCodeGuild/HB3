# Number = word
first_digit_words = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
# First digit key for concatonation with other dict value
second_digit_words = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
# First digit check uniquely identifies the unique numbers 10-19
unique_words = {0:'ten',1:'eleven',2:'twelve',3:'thirteen',4:'fourteen',5:'fifteen',6:'sixteen',7:'seventeen',8:'eighteen',9:'nineteen'}

def main():
    number = (input('Enter a number from 0-99:'))
    # Turned into list to make the entry indexable to grab keys
    digits = list(number)
    # Length as basis for conditions
    digit_length = (len(number))
    # Check for single digit word
    if digit_length !=2:
        word = first_digit_words.get(int(digits[0]))
        print(word)
        return
    elif int(digits[0]) !=1:
        if int(digits[1]) !=0:
            word = second_digit_words.get(int(digits[0]))+" "+first_digit_words.get(int(digits[1]))
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

main()
