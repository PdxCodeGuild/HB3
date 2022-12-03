import random




def pick6() :
    num_list = random.sample(range(1 , 99), 6)  # create a list 0f 6 randomly generated numbers between 1-99
    return num_list
    



def num_matches(winning , ticket ) :
    total_matches = 0                   # create an empty list to hold matches
    ticket = pick6()
    winning = pick6()
     
    for int in ticket :                 # for each exact match, one is added to the total_matches
        if ticket[0] == winning[0] :
         total_matches =+ 1
        if ticket[1] == winning[1] :
         total_matches =+ 1
        if ticket[2] == winning[2] :
         total_matches =+ 1
        if ticket[3] == winning[3] :
         total_matches =+ 1
        if ticket[4] == winning[4] :
         total_matches =+ 1
        if ticket[5] == winning[5] :
         total_matches =+ 1
    return(total_matches)

    
    
winning_ticket = pick6() # setting the winning ticket
print(f"The winning ticket is {winning_ticket}")

final_matches = 0 # setting the variable to total the number of matches
balance = 0 # setting the starting balance

for x in range(100001) :   # for loop that will loop 100,000 times

    balance -= 2 # each loop will subtract 2 from the balance

    matches = num_matches(winning_ticket , pick6()) # variable "matches" is assigned to the list of matches created by the num_matches function
    
    final_matches += matches       # adding the number of matches to the overall number of matches
   

    if matches == 1 :            # conditional if/elif statements for the number of potential matches
            balance += 4
    elif matches == 2 :
            balance += 7
    elif matches == 3 :
            balance += 100 
    elif matches == 4 :
            balance += 50,000
    elif matches == 5 :
            balance += 1,000,000  
    elif matches == 6 :
            balance += 25,000,000
    
print(f"The number of matches is {final_matches}")
print(f"The final balance is {balance}")

    


