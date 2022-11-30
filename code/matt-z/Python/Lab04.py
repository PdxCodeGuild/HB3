dict = {
    'A' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    'J' : 10,
    'Q' : 10,
    'K' : 10
}

first_card = input("What's your first card? ")
second_card = input("What's your second card? ")
third_card = input("What's your third card? ")

first = dict.get(first_card)
second = dict.get(second_card)
third = dict.get(third_card)

total = first + second + third

def advice(total):
    if total < 17:
        return f'{total} Hit'
    elif total >= 17 and total < 21:
        return f'{total} Stay'
    elif total == 21:
        return f'{total} Blackjack!'
    elif total > 21:
        return f'{total} Already Busted'
    
print(advice(total))