import random

ticket = []
for i in range(0,6):
    user = int(input('Enter your selected numbers to Win some Cash!!!: '))
    ticket.append(user)
print(ticket)

def pick():
    lotteryNumbers = []
    for i in range(0,6):
        num = random.randint(1,99)
        lotteryNumbers.append(num)
    return lotteryNumbers
winning = pick()
print(pick())

def num_matches(winning,ticket):
    counter = 0
    for x in ticket:
        if x in winning:
            counter +=1
    if counter == 0:
        return 'Bad luck'
    elif counter == 1:
        return 'You win $4'
    elif counter == 2:
        return 'You win $7'
    elif counter == 3:
        return 'You win $100'
    elif counter == 4:
        return 'You win $50,000'
    elif counter == 5:
        return 'You win $1,000,000'
    elif counter == 6:
        return 'You win $25,000,000'

print(num_matches(winning,ticket))
        
    
    
        