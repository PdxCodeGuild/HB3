# get input of number and convert it to an integer
x = input("Pick a number from 1 - 99: ")
num = int(x)

# extract tens digit and ones digit
tens_digit = num//10

ones_digit = num%10

# create a list for the tens digits and ones digits

tens_list = [
    "", 
    "teen", 
    "twenty-", 
    "thirty-", 
    "forty-", 
    "fifty-", 
    "sixty-", 
    "seventy-", 
    "eighty-", 
    "ninety-"
    ]

ones_list = [
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
    ]


# if tens digit is 1, the verbal tens digit must come after the one digit (ex. fifteen, not teen-five). 10, 11, 12, 13, 15, and 18 are special cases

if tens_digit == 1 and ones_digit == 0 :
    print("ten")
elif tens_digit == 1 and ones_digit == 1 :
    print("eleven")
elif tens_digit == 1 and ones_digit == 2 :
    print("twelve")
elif tens_digit == 1 and ones_digit == 3 :
    print("thirteen")
elif tens_digit == 1 and ones_digit == 5 :
    print("fifteen")
elif tens_digit == 1 and ones_digit == 8 :
    print("eighteen")
elif tens_digit == 1 :
    print(f"{(ones_list[ones_digit])}{(tens_list[tens_digit])}")
else :
    print(f"{(tens_list[tens_digit])}{(ones_list[ones_digit])}")
