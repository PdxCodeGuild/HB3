#creating an empty list
jackalopes = [0,0]
years = 0

#begins with a while loop 
while len(jackalopes) < 1000:
    #consider that any jackalop that lives longer than 10 dies and can no longer reproduce
    for x in range(len(jackalopes)):
        jackalopes[x] += 1 #they each get older per every year

        #Elgible deer to reproduce
        if jackalopes[x] >= 4 and jackalopes[x]:
            jackalopes.append(0)

            #Jackalopes will die at an age of 10 therefore are not included
            jackalopes = list(filter(lambda a: a !=10, jackalopes))
    #we will now add a year to the total years
    years += 1
print(f"It will take {years} years for two jackalopes to create a population of 1000.")