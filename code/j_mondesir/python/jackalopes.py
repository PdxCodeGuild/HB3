jackalopes = [0,0]
years = 0


while len(jackalopes) <= 1000:
    
    for index in range(len(jackalopes)):
        jackalopes[index] += 1

        if jackalopes[index] >= 4 and jackalopes[index]<=8:
           jackalopes.append(0)

        jackalopes = list(filter(lambda a: a != 10, jackalopes))

    years +=1

print(years)
