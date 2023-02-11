# Lab 11 (MOB) -> calculate how many years it will take for two Jackalopes ("Jackos") to create a population of 1000.

# makew a list for a starting pair of jackolopes
jackalopes = [0, 0]
years = 0

# use a while loop to run functions until there are 1000 Jackos
while len(jackalopes) < 1000:

    for index in range(len(jackalopes)):
        
        # increase the age of each Jacko by 1
        jackalopes[index] += 1

        # determine reproduction numbers
        if jackalopes[index] >= 4 and jackalopes[index] <= 8: jackalopes.append(0)

        # remove the number 10 from the list as the Jackos die at 10 years old
        jackalopes = list(filter(lambda a: a != 10, jackalopes))

    years += 1

print('It will take', years, 'years to produce 1000 Jackos.')