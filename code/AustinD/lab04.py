#Card draw function
def draw_cards():
    print('When prompted, enter your card as a number or as the first letter of your named card, capitalized.')
    x = input("What's your first card?")
    y = input("What's your second card?")
    z = input("What's your third card?")
    drawn_cards = [x, y, z]
    print(drawn_cards)
    return drawn_cards

#Advice function
def advice(x):
    deck = {
    'A':1,
    2:2,
    3:3,
    4:4,
    5:5,
    6:6,
    7:7,
    8:8,
    9:9,
    10:10,
    'J':10,
    'Q':10,
    'K':10,
    }
    print(x[0])
    cardone = deck.get(x[0])
    print(cardone)
    cardtwo = deck.get(x[1])
    print(cardtwo)
    cardthree = deck.get(x[2])
    print(cardthree)

    """ net_drawn_value = cardone+cardtwo+cardthree
    n = net_drawn_value

    if n > 21:
        return "Already Busted"
    if n == 21:
        return "Blackjack!"
    if n > 17 or n == 17:
        return "Stay"
    if n < 17:
        return "Hit" """

print(advice(draw_cards()))