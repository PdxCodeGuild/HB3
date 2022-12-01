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
    balance = 0
    print(f"The winning ticket is {winning}")
    for i in range(100000):
        
        ticket = pick6()
        balance -= 2
        if num_matches(winning, ticket) == 1:
            balance += 4
        elif num_matches(winning, ticket) == 2:
            balance += 7
        elif num_matches(winning, ticket) == 3:
            balance += 100
        elif num_matches(winning, ticket) == 4:
            balance += 50000
        elif num_matches(winning, ticket) == 5:
            balance += 1000000
        elif num_matches(winning, ticket) == 6:
            balance += 25000000
        
    print(f"Total balance is {balance}")
        
        # print(f"Your ticket - {ticket}")
        # print(f"Winning ticket - {winning}")

        # print(f"Total number of matches - {num_matches(winning, ticket)}")

main(pick6())
