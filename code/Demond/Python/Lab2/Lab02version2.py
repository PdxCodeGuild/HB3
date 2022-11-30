number = input("enter your number:")
numbers = { 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
numbers_2 = {1:'One', 2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'nintey'}
hundreds_place = {100:"One - Hundred", 200:"Two - Hundred", 300:"Three - Hundred", 400:"Four - Hundred", 500:"Five - Hundred", 
600:"Six - Hundred", 700:"Seven - Hundred", 800:"Eight - Hundred",
900:"Nine - Hundred"} #This dictionary covers my hundred place if the input matches the key
hundreds = number[1] + number[2] #This will be the variable for the hundreds_place place if it is in the hundreds
if int(number) in hundreds_place:
    print(f"Your number is: {hundreds_place[int(number)]}")
elif int(hundreds) in hundreds_place: #this will be the print statment if the hundreds variable matches the value in first twenty dic
    ones_digit =  int(number[0])
    tens_digit =  int(number[1])
    teen = number[1] + number[2]
    int(hundreds)
    print(f"Your number is: {numbers[ones_digit]} hundred {hundreds_place} - {[int(hundreds)]} ")
elif int(number[2]) == 0:
    ones_digit =  int(number[0])
    tens_digit =  int(number[1])
    third_value = int(number[2])
    print: print(f"Your number is: {numbers[ones_digit]} hundred - {numbers_2[tens_digit]}")
else: #if none of the statements above are true then it will print the word form of each number
    ones_digit =  int(number[0])
    tens_digit =  int(number[1])
    third_value = int(number[2])
    print(f"Your number is: {numbers[ones_digit]} hundred {numbers_2[tens_digit]} - {numbers[third_value]} ")