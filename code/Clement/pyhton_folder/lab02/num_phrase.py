# Number To Phrase

print('\nWelcome To Number To Phrase!!!!\n')

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

num_enter = int(input('Please enter a number from(1-100):\n'))

if num_enter <= 100:
    if num_enter in num_phrase:
        value = num_phrase.get(num_enter)
        print(value)

else:
    print(f"Invalid number please a number from (0-100)")