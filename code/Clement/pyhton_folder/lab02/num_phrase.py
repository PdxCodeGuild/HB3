# Number To Phrase

print('\nWelcome To Number To Phrase')
print('Lets converts some numbers!!!!!!!\n')

num_phrase = {
    0:"zero",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"nineteen",
    20:"twenty",
    40:"forty",
    30:"thirty",
    50:"fifty",
    60:"sixty",
    70:"seventy",
    80:"eighty",
    90:"ninety",
    100:"Hundred", 

}

while True:
    num_enter = int(input('Please enter a number from(1-100):\n'))

    # Trying to address the numbers that in & not in the dictionary
    if num_enter < 100:
        print(num_phrase[(num_enter // 10 * 10)])
        
        if num_enter in num_phrase:
            value = num_phrase.get(num_enter)
            print(f"Your number {num_enter} and in word is ({value})\n")

    # To address bigger odd numbers like (35, 45,65,75 etc.)
        else:
            ones_digit_num = num_enter % 10
            ones_digit_num = num_phrase.get(ones_digit_num)

            tens_digit_num = num_enter // 10
            tens_digit_num *= 10
            tens_digit_num = num_phrase.get(tens_digit_num)
            result = tens_digit_num + "-" + ones_digit_num

            print(f"Your number {num_enter} and in word is ({result})\n")

    else:
        print(f"Your number {num_enter} is invalid number please enter a number from (0-100)\n")
        break