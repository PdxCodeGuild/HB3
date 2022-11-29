number = input("enter your number:") #I have created a variable for the input
numbers = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'} #this key/value will cover 1-9
numbers_2 = {2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'nintey'} #this key/value will cover 20-90
first_twenty = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 
6:"Six", 7:"Seven", 8:"Eight",
9:"Nine", 10:"Ten", 11:"Eleven",
12:"Twelve", 13:"Thirteen", 14:"Fourteen",
15:"Fifteen", 16:"Sixteen", 17:"Seventeen",
18:"Eighteen", 19:"Nineteen" , 20:"twenty"}#these will cover the teens
if int(number) in first_twenty: #I have created an if statement that will check if the input is in the teens
    print(f"Your number is: {first_twenty[int(number)]}")#if so the print statment will print out the value for the appropriate key
else:#if it is not then the print statement will be the input number in word form
    tens_digit = int(number)//10
    ones_digit = int(number)%10
    print(f"Your number is: {numbers_2[tens_digit]} {numbers[ones_digit]}")