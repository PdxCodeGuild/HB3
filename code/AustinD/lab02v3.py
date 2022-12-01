# Repurposed code from lab02v2(words terminology maintained over numeral)
# Added separate third digit dict
# Removed teens/teen conditionals
# Removed strings for hundred or spaces in concatonation
first_digit_words = {0:' ',1:'I',2:'I',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX'}
second_digit_words = {2:'XX',3:'XXX',4:'XL',5:'L',6:'LX',7:'LXX',8:'LXXX',9:'XC'}
third_digit_words = {1:'C',2:'CC',3:'CCC',4:'CD',5:'D',6:'DC',7:'DCC',8:'DCCC',9:'CM'}

def main():
    number = (input('Enter a number from 0-999:'))
    digits = list(number)
    digit_length = (len(number))
    if digit_length < 2:
        word = first_digit_words.get(int(digits[0]))
        print(word)
        return
    elif digit_length == 2:
        if int(digits[1]) !=0:
            word = second_digit_words.get(int(digits[0]))+first_digit_words.get(int(digits[1]))
            print(word)
            return
        else:
            word = second_digit_words.get(int(digits[0]))
            print(word)
            return
    else: 
        if int(digits[2]) !=0:
            if int(digits[1]) !=0:
                word = third_digit_words.get(int(digits[0]))+second_digit_words.get(int(digits[1]))+first_digit_words.get(int(digits[2]))
                print(word)
                return
            else: 
                word = third_digit_words.get(int(digits[0]))+first_digit_words.get(int(digits[2]))
                print(word)
                return
        else: 
            word = third_digit_words.get(int(digits[0]))
            print(word)
            return
main()