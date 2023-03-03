# calculate how many years it will take for two jackalopes to create a population of 1000.
jackalopes = [0, 0]
year = 0

while len(jackalopes)< 1000:
    # Jackalopes are reproductive from ages 4-8 and die at age 10.
    for i in range(len(jackalopes)):
        jackalopes[i] += 1

        # Gestation is instantaneous. Each gestation produces two offspring.
        if jackalopes[i] >= 4 and jackalopes[i]:
            jackalopes.append(0)

        # The lifespan of jackalopes
        jackalopes = list(filter(lambda a: a !=10, jackalopes))
print(jackalopes)