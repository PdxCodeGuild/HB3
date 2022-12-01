First_Choice = input("What's your first card? ") #lines 1-3 input/variable will assign users card inputs
Second_Choice = input("What's your second card? ")
Third_Choice = input("What's your third card? ")
ACE_Or_Face_Cards = { 'Q':10, 'J':10, 'K':10, 'A':1 } #this dic is used to determine the face cards and their values
if First_Choice in ACE_Or_Face_Cards: #lines 5 - 10 checks each input variable to see if they match the key and then changes their variable
    First_Choice = ACE_Or_Face_Cards[First_Choice]
if Second_Choice in ACE_Or_Face_Cards:
    Second_Choice = ACE_Or_Face_Cards[Second_Choice]
if Third_Choice in ACE_Or_Face_Cards:
    Third_Choice = ACE_Or_Face_Cards[Third_Choice]
Users_Total_Amount = int(First_Choice) + int(Second_Choice) + int(Third_Choice) #this will add the users input and assign it to a variable
if Users_Total_Amount < 17: #lines 12 - 19 will output the appropriate print statement 
    print(f"{Users_Total_Amount} Hit")
elif Users_Total_Amount >= 17 and Users_Total_Amount <= 20:
    print(f"{Users_Total_Amount} Stay")
elif Users_Total_Amount == 21:
    print(f"{Users_Total_Amount} Black Jack!")
elif Users_Total_Amount <= 22:
    print(f"{Users_Total_Amount} Already Busted")