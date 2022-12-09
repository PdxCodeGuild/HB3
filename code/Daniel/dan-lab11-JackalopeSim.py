#---------------------------------
# PDX Code Guild: HB3
# Lab11: Jackalope Simulator
# Author: Daniel Smith
# Date: 2022.12.8
#---------------------------------

# Mob Programming Version 1
# The goal is to calculate how many years it will take for two jackalopes to create a population of 1000.
# Jackalopes are reproductive from ages 4-8 and die at age 10.
# Gestation is instantaneous. Each gestation produces two offspring.
# Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do
# With these conditions in mind, we can represent our population as a list of ints.

years = 0 # Initialize a year count.
jackalopes = [0, 0] # Initialize a jackalope population of 2 at age 0.

while len(jackalopes) < 1000: # Loop until the population of jackalopes reaches 1000.
    years += 1 # Increase year count by 1.

    for index in range(len(jackalopes)): # Iterate through all existing jackalopes.
        jackalopes[index] += 1 # Increase the age of all jackalopes by 1.
        if jackalopes[index] >= 4 and jackalopes[index] <= 8: # Identify all jackalopes of reproductive age.
            jackalopes.append(0) # Reporductive-age 'lopes have 1 baby each for a total of 2 babies per pair.
        jackalopes = [i for i in jackalopes if i != 10] # Remove all jackalopes that died of old age.
        # jackalopes = list(filter(lambda i: i != 10, jackalopes)) # Alt. method to remove all jackalopes that died of old age.

# Display the results.
# print(jackalopes)
print(f'Version 1: It took {years} years to reach a population of 1000 jackalopes.')


# Version 2 (Optional)
# Now let's give the jackalopes distinct sexes and extend their gestation period to one year.
# We can represent each jackalope with a dictionary, thus our population will be a list of dictionaries.
# Jackalopes can only mate with those immediately around them.
# Every generation Jackalopes are randomly shuffled.

# Each jackalope will have the following properties:
# name
# age
# sex
# whether they're pregnant

years = 0 # Initialize a year count.
jackalopes = [{ # Initialize a jackalope population of 2 at age 0.
    'name': 'Jack',
    'age': 0,
    'sex': 'male',
    'pergnant': False
    },
    {
    'name': 'Alope',
    'age': 0,
    'sex': 'female',
    'pergnant': False
    }]

while len(jackalopes) < 1000: # Loop until the population of jackalopes reaches 1000.
    years += 1 # Increase year count by 1.

    for i in range(len(jackalopes)): # Iterate through all existing jackalopes.
        jackalopes[i]['age'] += 1 # Increase the age of all jackalopes by 1.

        if jackalopes[i] >= 4 and jackalopes[i] <= 8: # Identify all jackalopes of reproductive age.
            ###### jackalopes.append(0) # Reporductive-age 'lopes have 1 baby each for a total of 2 babies per pair.

            # Jackalopes can only mate with those immediately around them.
            # Every generation Jackalopes are randomly shuffled.

        jackalopes = [i for i in jackalopes if i['age'] != 10] # Remove all jackalopes that died of old age.
        # jackalopes = list(filter(lambda i: i[age] != 10, jackalopes)) # Alt. method to remove all jackalopes that died of old age.

# tip: turn it into a method and apply it to a class.