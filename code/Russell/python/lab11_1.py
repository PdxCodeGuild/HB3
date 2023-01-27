jackalopes = [0, 0]
years = 0

while len(jackalopes) < 1000:
    # how many numbers between 4 and 8
    for index in range(len(jackalopes)):
        jackalopes[index] += 1

        # determine how many can reproduce
        if jackalopes[index] >= 4 and jackalopes[index] <= 8:
            jackalopes.append(0)

        # how many jackalopes died of old age
        dead_jackalopes = list(filter(lambda a: a > 10, jackalopes))
        
    years += 1 
    
print(f"It would take {years} years for a population of jackalopes to go from 2 to 1000+....")
print(f"After which point there would be {len(jackalopes)} living jackalopes...")
print(f"With {len(dead_jackalopes)} jackalopes having died of old age.")