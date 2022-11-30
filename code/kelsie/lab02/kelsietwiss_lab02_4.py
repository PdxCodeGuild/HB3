x = input("What is the time? ")


# create a list of the input characters
num_list = list(x) 


# get an accurate hour by combining the first two characters in the list
hour = int((num_list[0]) + (num_list[1])) 
tens_min = int(num_list[3]) 
ones_min = int(num_list[4]) 


hours_dict = {
    0 : "",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve"
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
if tens_min == 1 and ones_min == 0 :  
    print(f"{hours_dict[hour]} ten")
elif tens_min == 1 and ones_min == 1 :
    print(f"{hours_dict[hour]} eleven")
elif tens_min == 1 and ones_min == 2 :
    print(f"{hours_dict[hour]} twelve")
elif tens_min == 1 and ones_min == 3 :
    print(f"{hours_dict[hour]} thirteen")
elif tens_min == 1 and ones_min == 5 :
    print(f"{hours_dict[hour]} fifteen")
elif tens_min == 1 and ones_min == 8 :
    print(f"{hours_dict[hour]} eighteen")
elif tens_min == 1 :
    print(f"{hours_dict[hour]} {ones_dict[ones_min]}{tens_dict[tens_min]}")
else :
    print(f"{hours_dict[hour]} {tens_dict[tens_min]}-{ones_dict[ones_min]}")
