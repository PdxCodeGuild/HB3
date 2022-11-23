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


# create if/while loops for hit, stay, blackjack, and busted
if total > 21 :
    print(f"{total} Already Busted")
elif total == 21 :
    print (f"{total} Blackjack!")
elif total < 21 and total >= 17 :
    print(f"{total} Stay")
else :
    print(f"{total} Hit")
