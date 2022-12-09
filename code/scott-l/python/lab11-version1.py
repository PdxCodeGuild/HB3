'''
 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
      Project: lab 11 - Jackalope (Mob Coding)
      Author: Scott Lefgren
      Email: scojlefg@gmail.com
      Date: December 8, 2022
___________________          _-_
\==============_=_/ ____.---'---`---.____
            \_ \    \----._________.----/
              \ \   /  /    `-_-'
          __,--`.`-'..'-_
         /____          ||
              `--.____,-'

 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
'''
# Mob Coding

# The goal is to calculate how many years it will take for two jackalopes to create a population of 1000.

#     Jackalopes are reproductive from ages 4-8 and die at age 10.
#     Gestation is instantaneous. Each gestation produces two offspring.
#     Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do

# With these conditions in mind, we can represent our population as a list of ints.

jackalopes = [0,0]
years = 0

while len(jackalopes) < 1000:

    for index in range(len(jackalopes)):

        jackalopes[index] += 1

        # Determine how many can reproduce
        if jackalopes[index] >=4 and jackalopes[index] <= 8:
            jackalopes.append(0)
      
        jackalopes = list(filter(lambda a: a!=10, jackalopes))
    # end for loop
    years +=1 
# end while

# print(jackalopes)
print(f'How long will it take to reach a population of 1000 Jackalopes')
print(f'It will take {years} years')



