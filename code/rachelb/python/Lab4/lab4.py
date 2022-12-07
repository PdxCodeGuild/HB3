#write out a dictionary that has the value of each card

#create a inputs asking the user for 3 cards

# We need a fuction that collects the total number of cards

#create statments:
# x < 17 HIT    x >= 17 and x < 21 STAY     x = 21 Blackjack  x > 21 Already busteds

cards = {"A": 1, "2": 2,
"3": 3, "4": 4, 
"5": 5, "6": 6, 
"7": 7, "8": 8,
"9": 9, "10":10,
"J":10, "Q": 10, 
"K":10}

first = input("What's your first card? ")
second = input("What's your second card? ")
third = input("What's your third card? ")

total = cards[first] + cards[second] + cards[third]
# print(total)

if total >= 17 and total < 21:
    print( str(total) + ' ' + 'Stay')
elif total < 17:
    print( str(total) + ' ' + 'HIT')
elif total == 21:
    print( str(total)) + ' ' + 'Blackjack!!'
else: 
    total > 21
    print( str(total) + ' ' + 'Already busted')