#---------------------------------
# PDX Code Guild: HB3
# Lab11: Jackalope Simulator
# Author: Daniel Smith
# Date: 2022.12.8
#---------------------------------

# Mob Programming Version 1
# The goal is to calculate how many years it will take for two jackalopes to create a population of 1000.
# Jackalopes are reproductive from ages 4-8, and die at age 10.
# Gestation is instantaneous. Each gestation produces two offspring.
# Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do.
# With these conditions in mind, we can represent our population as a list of ints.

year = 0 # Initialize a year count. years == lope generations
jackalopes = [0, 0] # Initialize a lope population of 2 at age 0.

while len(jackalopes) < 1000: # Loop until population reaches 1000.

    for lope in range(len(jackalopes)): # For all lopes:
        if 4 <= jackalopes[lope] <= 8: # For all lopes of reproductive age:
            jackalopes.append(0) # Add 1 new offspring per lope, equivalent to 2 offspring per pair of lopes.
        jackalopes = [i for i in jackalopes if i != 10] # Remove all lopes of age 10.
        # jackalopes = list(filter(lambda i: i != 10, jackalopes)) # Alt. method to remove all lopes of age 10.
        jackalopes[lope] += 1 # Increment the age of all lopes by 1.

    year += 1 # Increment the year count by 1.

print(f'Version 1: It will take {year} years for two jackalopes to create a population of 1000.') # Display the goal/result.
# print(jackalopes) #testing


# Version 2 (Optional)
# Now let's give the jackalopes distinct sexes and extend their gestation period to one year.
# We can represent each jackalope with a dictionary, thus our population will be a list of dictionaries.
# Jackalopes can only mate with those immediately around them.
# Every generation Jackalopes are randomly shuffled.

# tip: turn it into a method and apply it to a class.

# Each jackalope will have the following properties:
# name
# age
# sex
# whether they're pregnant

import random
year = 0 # Initialize a year count. years == lope generations
# Initialize a lope population of 2 at age 0.
jackalopes = [{ 
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

while len(jackalopes) < 1000: # Loop until the population reaches 1000.
    for lope in jackalopes: # For all lopes:

        # Jackalopes can only mate with suitable partners immediately around them.
        if 4 <= lope['age'] <= 8 and lope['sex'] == 'female': #and 'pergnant' == False: # For all reproductive females:
            if (4<= jackalopes[lope-1]['age'] <= 8 and jackalopes[lope-1]['sex'] == 'male') or (4<= jackalopes[lope+1]['age'] <= 8 and jackalopes[lope+1]['sex'] == 'male'): # Check for an adjacent reproductive male:
                # lope['pergnant' == True] # Female turns pregante.
                # Add 2 new fetuses per suitable pair. Each fetus has a gestation period of 1 year.
                jackalopes.append({ 
                'name': 'Jack',
                'age': -1,
                'sex': 'male',
                'pergnant': False
                },
                {
                'name': 'Alope',
                'age': -1,
                'sex': 'female',
                'pergnant': False
                })

        jackalopes = [lope for lope in jackalopes if lope['age'] != 10] # Remove all lopes of age 10.
        jackalopes = random.shuffle(jackalopes) # Every year all lopes are randomly shuffled.
        lope['age'] += 1 # Increment the age of all lopes by 1.
        # if lope['pergnant'] == True: # Fetuses are born into babies thus mothers no longer gregnant.
        #     lope['pergnant'] == False

    year += 1 # Increment the year count by 1.
