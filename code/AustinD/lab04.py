#Card draw function, returned as a list for simplicity
def draw_cards():
    print('When prompted, enter your card as a number or as the first letter of your named card, capitalized.')
    x = input("What's your first card?")
    y = input("What's your second card?")
    z = input("What's your third card?")
    drawn_cards = [x, y, z]
    print(drawn_cards)
    return drawn_cards

#Advice function, where x is list of inputs to index a dict of int values for user card inputs
def advice(x):
    deck = {
    'A':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10,
    'J':10,
    'Q':10,
    'K':10,
    }

    #Converting to variable mostly for readability
    cardone = deck.get(x[0])
    cardtwo = deck.get(x[1])
    cardthree = deck.get(x[2])

    #Where n is net drawn value of cards for advice
    n = cardone+cardtwo+cardthree

    #Assessing net drawn value for advice and returning advice
    if n > 21:
        return "{n} Already Busted"
    if n == 21:
        return "{n} Blackjack!"
    if n > 17 or n == 17:
        return "{n} Stay"
    if n < 17:
        return "{n} Hit"

#Functions called for advice
print(advice(draw_cards()))