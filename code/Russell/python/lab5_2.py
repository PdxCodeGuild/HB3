import random

def pick6():

    nums = [random.randint(0, 99) for i in range(6)]
    return nums



def num_matches(winning, ticket):

    matches = 0
    for i in range(len(winning)):
        if winning[i] == ticket[i]:
            matches += 1
            return matches


def main(winning):
    earnings = 0
    expenses = 0
    print(f"The winning ticket is {winning}")
    for i in range(100000):
        
        ticket = pick6()
        expenses += 2
        if num_matches(winning, ticket) == 1:
            earnings += 4
        elif num_matches(winning, ticket) == 2:
            earnings += 7
        elif num_matches(winning, ticket) == 3:
            earnings += 100
        elif num_matches(winning, ticket) == 4:
            earnings += 50000
        elif num_matches(winning, ticket) == 5:
            earnings += 1000000
        elif num_matches(winning, ticket) == 6:
            earnings += 25000000

    net = earnings - expenses
    return_on_investment =   (earnings - expenses)/expenses  
    print(f"Total earnings: {earnings}")
    print(f"Total expenses: {expenses}")
    print(f"Net: {net}")
    print(f"ROI: {return_on_investment}")
        
        # print(f"Your ticket - {ticket}")
        # print(f"Winning ticket - {winning}")

        # print(f"Total number of matches - {num_matches(winning, ticket)}")

main(pick6())
