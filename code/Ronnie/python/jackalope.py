# Jackalopes population to 1000
# Jackalopes are reproductive from ages 4-8 and die at age 10.
# Gestation is instantaneous. 
# Each gestation produces two offspring.
# It takes a pair to reproduce, but any pair will do

jackalopes = [0, 0]
years = 0

while len(jackalopes) <= 1000:
    # how many numbers between 4 and 8
    for index in range(len(jackalopes)):
        jackalopes[index] += 1

        # determine how many can reproduce
        if jackalopes[index] >= 4 and jackalopes[index] <= 8:
            jackalopes.append(0)

        # how many jackalopes died of old age
        jackalopes = list(filter(lambda a: a != 10, jackalopes))
    years += 1 
    
print(years)