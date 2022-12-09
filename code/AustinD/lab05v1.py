import random 
#Start your balance at 0
balance = 0
#Winnings parameters
winnings = {0:0, 1:4, 2:7, 3:100, 4:50000, 5:1000000, 6:25000000}
#Generate a list of 6 random numbers representing the winning tickets
winning = random.sample(range(1, 99), 6)
#Find how many numbers match
def num_matches(winning, ticket):
        for i in range(len(winning)):
            print(i)
            if ticket[i] == winning[i]:
                match_count += 1
            else:
                pass
            #print(match_count)
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

#After the loop, print the final balance
print(f'Your balance is ${balance}.')