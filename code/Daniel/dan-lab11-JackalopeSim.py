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

# year = 0 # Initialize a year counter. years == lope generations
# jackalopes = [0, 0] # Initialize a lope population of 2 at age 0.

# while len(jackalopes) < 1000: # Loop until population reaches 1000.

#     for lope in range(len(jackalopes)): # For all lopes:
#         if 4 <= jackalopes[lope] <= 8: # For all lopes of reproductive age:
#             jackalopes.append(0) # Add 1 new offspring per lope, equivalent to 2 offspring per pair of lopes.
#         jackalopes = [i for i in jackalopes if i != 10] # Remove all lopes of age 10.
#         # jackalopes = list(filter(lambda i: i != 10, jackalopes)) # Alternate method to remove all lopes of age 10.
#         jackalopes[lope] += 1 # Increment the age counter of all lopes by 1.

#     year += 1 # Increment the year counter by 1.

# print(f'Version 1: It will take {year} years for two jackalopes to create a population of 1000.') # Display the goal result.






# Version 2 (Optional)
# Now let's give the jackalopes distinct sexes and extend their gestation period to one year.
# Jackalopes can only mate with those immediately around them.
# Every generation the Jackalopes are randomly shuffled.

# We can represent each jackalope with a dictionary, thus our population will be a list of dictionaries.
# Each jackalope will have the following properties:
# name
# age
# sex
# whether they're pregnant

# tip: turn it into a method and apply it to a class.

import random

def makebebes():
    # Add 2 new fetuses per suitable pair. Each fetus has a gestation period of 1 year or an 'age' of -1. ##### Are fetuses counted? Are fetuses part of the lope population?
    jackalopes.append({ 
    'name': 'Jack',
    'age': -1,
    'sex': 'male',
    'pergnant': False
    })
    jackalopes.append({
    'name': 'Alope',
    'age': -1,
    'sex': 'female',
    'pergnant': False
    })

year = 0 # Initialize a year counter. years == lope generations
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
    }] # Initialize a lope population of 2 at age 0.

print(jackalopes) #testing

while len(jackalopes) < 1000: # Loop until the population reaches 1000.
    random.shuffle(jackalopes) # Every year the lopes are randomly shuffled.
    jackalopes = [lope for lope in jackalopes if lope['age'] != 10] # Remove all lopes of age 10.
    print(f'year: {year}\n') #testing
        
    for lope in range(len(jackalopes)): # Do for all lopes:
        jackalopes[lope]['age'] += 1 # Increment the age counter of all lopes by 1.
        # jackalopes = [lope for lope in jackalopes if lope['age'] != 10] # Remove all lopes of age 10.

        print(lope, jackalopes[lope]['age'], jackalopes[lope]['sex']) #testing
        
        # Jackalopes can only mate with partners immediately around them.
        if jackalopes[lope]['sex'] == 'female' and 4 <= jackalopes[lope]['age'] <= 8: # Do for all reproductive females:   ## and jackalopes[lope]['pergnant'] == False:

            
            # try:
            #     jackalopes[lope-1] or jackalopes[lope+1]
            #  if lope > 1:
            if (jackalopes[lope-1]['sex'] == 'male' and 4 <= jackalopes[lope-1]['age'] <= 8): # Check for an adjacent reproductive male to the left:
                makebebes() # call the makebebes() method
            # elif lope < len(jackalopes):
            elif (jackalopes[lope+1]['sex'] == 'male' and 4 <= jackalopes[lope+1]['age'] <= 8): # Check for an adjacent reproductive male to the right:
                makebebes() # call the makebebes() method

            # except:
            #     print(f'######### ERROR ##########')
            #     pass


        #lope['pergnant' == True] # Female is now pregante.
        # if lope['pergnant'] == True: # For all pargnant lopes:
        #     lope['pergnant'] == False # Fetuses are born into babies thus mothers are no longer gregnant.

    year += 1 # Increment the year counter by 1.
    

print(f'Version 2: It will take {year} years for two jackalopes to create a population of 1000.') # Display the goal/result.
# print(jackalopes) #testing
