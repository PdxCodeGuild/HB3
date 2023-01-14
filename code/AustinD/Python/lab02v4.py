# Number = word
first_digit_words = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
# First digit key for concatonation with other dict value
second_digit_words = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
# First digit check uniquely identifies the unique numbers 10-19
unique_words = {0:'ten',1:'eleven',2:'twelve',3:'thirteen',4:'fourteen',5:'fifteen',6:'sixteen',7:'seventeen',8:'eighteen',9:'nineteen'}

def main():
    time = (input('Enter a time in the US standard format(without am/pm) ##:##:'))
    ampm = (input('Enter am or pm:'))
    # Turned into list to make the entry indexable to grab keys
    digits = list(time)
    digits.remove(':')
    print(digits)
    # Length as basis for conditions
    time_digits = (len(digits))
    # Check for single digit word
    if time_digits !=4:
        if int(digits[1]) !=0 and int(digits[2] !=0):
            if int(digits[1]) !=1:
                word = first_digit_words.get(int(digits[0]))+" "+second_digit_words.get(int(digits[1]))+" "+first_digit_words.get(int(digits[2]))+" "+ampm
                print(word)
                return
            else: 
                word = first_digit_words.get(int(digits[0]))+" "+unique_words.get(int(digits[2]))+" "+ampm
                print(word)
                return
        else:
            word = first_digit_words.get(int(digits[0]))+" "+ampm
            print(word)
            return
    else:
        if int(digits[2]) !=0 and int(digits[3]) !=0:
            if int(digits[2]) !=1:
                word = unique_words.get(int(digits[1]))+" "+second_digit_words.get(int(digits[2]))+" "+first_digit_words.get(int(digits[3]))+" "+ampm
                print(word)
                return
            else:
                word = unique_words.get(int(digits[1]))+" "+unique_words.get(int(digits[3]))+" "+ampm
                print(word)
                return
        else: 
            word = unique_words.get(int(digits[1]))+" "+ampm
            print(word)
            return
main()