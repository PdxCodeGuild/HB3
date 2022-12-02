import random
print("\nWelcome To Pick6 Winning Tickets Game\n")
print("Are you ready let's play now!!\n")

def pick_6():
    tickets = []
    for n in range(6):
        nums_picks = random.randint(1, 99)
        tickets.append(nums_picks)
    return tickets
    
def investments(win_ticket, expenses):
    return ((win_ticket - expenses) / expenses)

winning_nums = pick_6()
win_ticket = 0
cost_per_ticket = 2
nums_of_loops = 100000

"""
Looping through an indexes of a list, and print each.
Use each index to print it value from both list
And then compare the values at each index and count and see how many tickets matches
"""

def num_matches(winning, ticket):
    count_lottery = 0
    win_ticket = 0
    for x in range(6):
        if winning[x] == ticket[x]:
            count_lottery += 1      

    if count_lottery == 1:
        win_ticket  += 4
    elif count_lottery == 2:
        win_ticket  += 7
    elif count_lottery == 3: 
        win_ticket  += 100
    elif count_lottery == 4:
        win_ticket  += 50000
    elif count_lottery == 5:
        win_ticket  += 1000000
    elif count_lottery == 6:
        win_ticket  += 25000000
    return win_ticket
winnings = 0
for game in range(nums_of_loops):
    ticket = pick_6()
    winnings += num_matches(winning_nums, ticket)


 # Version 2 is checking for total amt spent and how much gain
expenses = cost_per_ticket * nums_of_loops
earnings = investments(winnings, expenses)
print(f"The amount spent is ${expenses}, total returns is ${winnings}, and your ROI is {earnings}%")