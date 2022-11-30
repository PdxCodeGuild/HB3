card_one = input("What's your first card? ") #lines 1-3 input/variable will assign users card inputs
card_two = input("What's your second card? ")
card_three = input("What's your third card? ")
face_cards = { 'Q':10, 'J':10, 'K':10, 'A':1 } #this dic is used to determine the face cards and their values
if card_one in face_cards: #lines 5 - 10 checks each input variable to see if they match the key and then changes their variable
    card_one = face_cards[card_one]
if card_two in face_cards:
    card_two = face_cards[card_two]
if card_three in face_cards:
    card_three = face_cards[card_three]
total_amount = int(card_one) + int(card_two) + int(card_three) #this will add the users input and assign it to a variable
if total_amount < 17: #lines 12 - 19 will output the appropriate print statement 
    print(f"{total_amount} Hit")
elif total_amount >= 17 or total_amount < 21:
    print(f"{total_amount} Stay")
elif total_amount == 21:
    print(f"{total_amount} Black Jack!")
elif total_amount > 21:
    print(f"{total_amount} Already Busted")