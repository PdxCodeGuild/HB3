# Black Jack Game

print("\n=============Welcome to Blackjack Game===========\n")


# asking for the user input
card_1 = input("Please enter your first card?\n").upper()
card_2 = input("Please enter your second card?\n").upper()
card_3 = input("Please enter your third card?\n").upper()


# create a dictionary that holds all keys and values of the playing cards
p_cards = {
    "A": 1,
    "J": 10,
    "Q": 10,
    "K": 10,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10":10,

    }

total = []

total.append(p_cards[card_1])
total.append(p_cards[card_2])
total.append(p_cards[card_3])

# total = p_cards[card_1] + p_cards[card_1] + p_cards[card_1] or
totals = sum(total)

# Greater than or equal to 17, but less than 21, advise to "Stay"
if totals >= 17 and totals < 21:
    print(f"Your cards value is {totals}, and l advice you 'Stay'")

# Less than 17, advise to "Hit"
elif totals < 17:
    print(f"Your cards value is {totals}, and l advice you 'Hit'")

# Over 21, advise "Already Busted"
elif totals > 21:
        print(f"Your cards value is {totals}, and you 'Busted!") 

# Exactly 21, advise "Blackjack!"
elif totals == 21:
    print(f"Your cards value is {totals} 'Blackjack!")