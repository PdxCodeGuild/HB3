import random

def pick6():
    numbers = [random.randint(1,99) for i in range(6)]
    return numbers

def num_matches(ticket, winning):
    matches = 0
    for i in range(6):
        if ticket[i] == winning[i]:
            matches += 1
    if matches == 0:
        return 0
    elif matches == 1:
        return 4
    elif matches == 2:
        return 7
    elif matches == 3:
        return 100
    elif matches == 4:
        return 50000
    elif matches == 5:
        return 1000000
    elif matches == 6:
        return 25000000
    
balance = 0

winning = pick6()

for i in range(100000):
    ticket = pick6()
    balance -= 2
    winnings = num_matches(ticket, winning)
    balance += winnings

print(f'Your balance is {balance}')

earnings = 200000 - abs(balance)

print(f'Your ROI is {int(((earnings-200000)/200000)*100)}%')