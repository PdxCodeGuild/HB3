
# get input of number 
x = input("Pick a number from 100 - 999: ")


# turn entered number into a list
num_list = list(x)


#access individual digits using indices
hundreds_digit = int(num_list[0])
tens_digit = int(num_list[1])
ones_digit = int(num_list[2])

# create dictionaries for ones, tens, and hundreds
hundreds_dict = {
    0 : "",
    1 : "one hundred",
    2 : "two hundred" ,
    3 : "three hundred",
    4 : "four hundred",
    5 : "five hundred",
    6 : "six hundred",
    7 : "seven hundred",
    8 : "eight hundred",
    9 : "nine hundred"
}

tens_dict = {
    0 : "", 
    1 : "teen", 
    2 : "twenty", 
    3 : "thirty", 
    4 : "forty", 
    5 : "fifty", 
    6 : "sixty", 
    7 : "seventy", 
    8 : "eighty", 
    9 : "ninety"
}

ones_dict = {
    0 :"",
    1 :"one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 :"eight",
    9 :"nine"
}


# special circumstances for unusual numbers (10, 11, 12, 13, 15, and 18)
if tens_digit == 1 and ones_digit == 0 : 
    print(f"{hundreds_dict[hundreds_digit]} ten")
elif tens_digit == 1 and ones_digit == 1 :
    print(f"{hundreds_dict[hundreds_digit]} eleven")
elif tens_digit == 1 and ones_digit == 2 :
    print(f"{hundreds_dict[hundreds_digit]} twelve")
elif tens_digit == 1 and ones_digit == 3 :
    print(f"{hundreds_dict[hundreds_digit]} thirteen")
elif tens_digit == 1 and ones_digit == 5 :
    print(f"{hundreds_dict[hundreds_digit]} fifteen")
elif tens_digit == 1 and ones_digit == 8 :
    print(f"{hundreds_dict[hundreds_digit]} eighteen")
elif tens_digit == 1 :
    print(f"{hundreds_dict[hundreds_digit]} {ones_dict[ones_digit]}{tens_dict[tens_digit]}")
else :
    print(f"{hundreds_dict[hundreds_digit]} {tens_dict[tens_digit]}-{ones_dict[ones_digit]}")