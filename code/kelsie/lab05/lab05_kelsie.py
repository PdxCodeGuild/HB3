import random

def pick6() :
    win_list = random.sample(range(1 , 99), 6)  # create a list 0f 6 randomly generated numbers between 1-99
    return win_list
    
#winning_list = pick6()


def num_matches(winning = pick6(), ticket = random.sample(range(1 , 99), 6)) :
    match_list = [] # create an empty list to hold matches
    
    balance = [0] # create a list for the balance

    ticket = random.sample(range(1 , 99), 6)  # create a list of our 6 random numbers
   
    winning = pick6()
   
    for int in ticket :
        if ticket[0] == winning[0] :
         match_list.append[int]
    else :
        print("No match")

    for int in match_list :             # if match_list is x int long, then winnings are $x
        if len(match_list) == 1 :
            balance == balance + 4
        elif len(match_list) == 2 :
            balance == balance + 7
        elif len(match_list) == 3 :
            balance == balance + 100 
        elif len(match_list) == 4 :
            balance == balance + 50,000
        elif len(match_list) == 5 :
            balance == balance + 1,000,000  
        elif len(match_list) == 6 :
            balance == balance + 25,000,000



    # within loop subtract $2 from balance



pick6()

num_matches()

#match_list = [] # create an empty list to hold matches

#num_list = random.sample(range(1 , 99), 6)  # create a list of our 6 random numbers

# create a loop generating 6 random numbers to be your ticket
#for int in num_list :
 #   if num_list[0] == winning_list[0] :
  #      match_list.append[int]
   # else :
    #    print("No match")


    

# determine how many numbers match



# dtermine winnings and add to the balance