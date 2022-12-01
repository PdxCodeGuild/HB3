import random
print("\nWelcome To Pick6 Winning Tickets Game\n")
print("Are you ready let's play now!!\n")


def pick_6():
    tickets = []

    for n in range(6):
        nums_picks = random.randint(1, 100)
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

for game in range(nums_of_loops):
    nums_match = pick_6()
    count_lottery = 0
    for x in range(6):
        if winning_nums[x] == nums_match[x]:
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
    
 # Version 2 is checking for total amt spent and how much gain
expenses = cost_per_ticket * nums_of_loops
earnings = investments(win_ticket, expenses)

print(winning_nums)
print(nums_match,'\n')

print(f"The amount spent on investment is ${expenses}, and your total returns is ${earnings}")