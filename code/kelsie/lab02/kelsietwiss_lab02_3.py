x = input("Please pick a three digit number: ") 

# creating a list of the input characters
num_list = list(x) 


# accessing the appropriate index
hundreds_digit = int(num_list[0]) 
tens_digit = int(num_list[1])
ones_digit = int(num_list[2])


hundreds_dict = {
    0 : "",
    1 : "C",
    2 : "CC" ,
    3 : "CCC",
    4 : "CD",
    5 : "D",
    6 : "DC",
    7 : "DCC",
    8 : "DCCC",
    9 : "CM"
}


tens_dict = {
    0 : "", 
    1 : "X", 
    2 : "XX", 
    3 : "XXX", 
    4 : "XL", 
    5 : "L", 
    6 : "LX", 
    7 : "LXX", 
    8 : "LXXX", 
    9 : "XC"
}

ones_dict = {
    0 :"",
    1 :"I",
    2 : "II",
    3 : "III",
    4 : "IV",
    5 : "V",
    6 : "VI",
    7 : "VII",
    8 :"VIII",
    9 :"IX"
}


print(f"{hundreds_dict[hundreds_digit]}{tens_dict[tens_digit]}{ones_dict[ones_digit]}")