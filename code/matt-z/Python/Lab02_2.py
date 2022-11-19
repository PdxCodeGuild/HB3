dict_ones = {
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
}

dict_tens = {  
    2:"twenty",
    3:"thirty",
    4:"forty",
    5:"fifty",
    6:"sixty",
    7:"seventy",
    8:"eighty",
    9:"ninety"
}

def convert(num):
    '''This will convert an int into the string representation of its name'''
    if num < 20: 
        return dict_ones.get(num) # if number is less than 20 get the string representation from the ones dictionary using the integer as the key
    elif num < 100:
        tens = dict_tens.get(num // 10) # if the number is less than 100 get the tens place from the tens dictionary and the ones place from the ones dictionary using the computed values as keys
        ones = dict_ones.get(num % 10)
        return f'{tens} - {ones}'
    elif num > 100:
        hundreds = dict_ones.get(num//100)
        tens = num%100
        if tens < 20:
            ten_digit = dict_ones.get(tens)
            return f'{hundreds} hundred and {ten_digit}'
        elif tens > 20:
            ten_digit = dict_tens.get(tens // 10)
            one_digit = dict_ones.get(tens % 10)
            return f'{hundreds} hundred and {ten_digit}-{one_digit}'
    
number = int(input("What is your number? "))

print(convert(number))