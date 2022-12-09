import random 
#Start your balance at 0
balance = 0
#Winnings parameters
winnings = {0:0, 1:4, 2:7, 3:100, 4:50000, 5:1000000, 6:25000000}
#Generate a list of 6 random numbers representing the winning tickets
winning = random.sample(range(1, 99), 6)
#Find how many numbers match
def num_matches(winning, ticket):
        match_count = 0
        for i in range(0, len(ticket)-1):
            if ticket[i] == winning[i]:
                match_count += 1
            else:
                break
        return match_count

def pick_6():
    #Generate a list of 6 random numbers representing the ticket
    ticket = random.sample(range(1, 99), 6)
    return (ticket)
#Loop 100,000 times, for each loop:
for x in range(100000):
    #Subtract 2 from your balance (you bought a ticket)
    balance -= 2
    #Add to your balance the winnings from your matches
    x = num_matches(winning, pick_6())
    balance += winnings[x]
    #print(balance)
#The ROI (return on investment) is defined as (earnings - expenses)/expenses. Calculate your ROI, print it out along with your earnings and expenses.
expenses = 200000
roi = (balance/expenses)*100
earnings = balance + expenses
#print(f'Your net winnings are ${balance}.\nEarnings: ${earnings}\nExpenses: $200,000\nROI: {roi}%')