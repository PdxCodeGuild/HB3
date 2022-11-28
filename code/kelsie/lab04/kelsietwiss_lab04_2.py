# get input of three cards
card_1 = input("What's your first card? ")
card_2 = input("What's your second card? ")
card_3 = input("What's your third card? ")

# create a dictionary with point values
blackjack_dict = {
    "A" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10
}

# add together the three cards to get total
total = (blackjack_dict[card_1] + blackjack_dict[card_2] + blackjack_dict[card_3])

# if one of the cards = "A" and the total with "A" = 1 is less than 11, 10 is added to the total to make "A" = 11
if card_1 == "A" and total < 11 : 
    total = total + 10
elif card_2 == "A" and total < 11 :
    total = total + 10
elif card_3 == "A" and total < 11 :
    total == total + 10
else :
    total == total


# create if/elif loop for hit, stay, blackjack, and busted
if total > 21 :   
        print(f"{total} Already Busted")
elif total == 21 :
        print (f"{total} Blackjack!")
elif total < 21 and total >= 17 :
        print(f"{total} Stay")
else :
        print(f"{total} Hit")





