# import random module to generate random numbers
import random

# generate 6 numbers ticket that user bought and print to screen
user_ticket = []
for i in range(0,6):
    user = random.randint(1,20) 
    user_ticket.append(user)

# Define function to generate the winning numbers that user playing against and print to screen
def pick():
    lottery = []
    for i in range(0,6):
        num = random.randint(1,20)
        lottery.append(num)
    return lottery
winning = pick()

# Define function to compare user ticket with winning numbers
def num_matches(x,y):
    counter = 0
    for nums in x:
        if nums in y:
           counter +=1
    if counter == 0:
        return 0
    elif counter == 1:
        return 4 - 2
    elif counter == 2:
        return 7 
    elif counter == 3:
        return 100 
    elif counter == 4:
        return 5000 
    elif counter == 5:
        return 1000000 
    elif counter == 6:
        return 25000000 
match_result = num_matches(winning,user_ticket)
    
balance = 0

for i in range(100):
    ticket = user_ticket
    balance -= 2
    match_result = num_matches(winning,user_ticket)
    balance += match_result
print(f'You have a balance of ${float(balance)}')
    
    


    
   
 

            
   



        
    
    
        