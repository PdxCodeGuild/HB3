number = input("enter your number:")
numbers = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
test = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
numbers_2 = {1:'One', 2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'nintey'}
first_twenty = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 
6:"Six", 7:"Seven", 8:"Eight",
9:"Nine", 10:"Ten", 11:"Eleven",
12:"Twelve", 13:"Thirteen", 14:"Fourteen",
15:"Fifteen", 16:"Sixteen", 17:"Seventeen",
18:"Eighteen", 19:"Nineteen" , 20:"twenty"}
teens = number[1] + number[2] #This will be the variable for the hundreds place if it is in the teens
if int(number) in first_twenty:
    print(f"Your number is: {first_twenty[int(number)]}")
if int(number) == 100: #this is if the input is 100 since it is not in any of the list
    print('Your number is one hundred')
if int(teens) in first_twenty: #this will be the print statment if the teens variable matches the value in first twenty dic
    ones_digit =  int(number[0])
    tens_digit =  int(number[1])
    teen = number[1] + number[2]
    int(teens)
    print(f"Your number is: {numbers[ones_digit]}, hundred and {first_twenty[int(teens)]} ")
else: #if none of the statements above are true then it will print the word form of each number
    ones_digit =  int(number[0])
    tens_digit =  int(number[1])
    third_value = int(number[2])
    print(f"Your number is: {numbers[ones_digit]} hundred and {numbers_2[tens_digit]} {test[third_value]} ")