import math

grid_coordinates = {1:[1, 2, 3, 4], 
2:[1, 2, 3, 4], 
3:[1, 2, 3, 4], 
4:[1, 2, 3, 4]
}

# location1 = 
# location2 =               ????HOW DO I GET MY GRID_COORDINATES INTO THE MATH.DIST METHOD???
# print(location1)
# print(location2)

distance = math.dist([1, 1], [4, 4])
print(round(distance, 2))


# def scavenge():

#     scavenge_level = input("How thoroughly would you like to search? (1- low; 2- medium; 3- high) ")
#     while int(scavenge_level) not in range(1, 4):
#         print("Invalid input, please try again")
#         scavenge_level = input("How thoroughly would you like to search? (1- low; 2- medium; 3- high) ")
#     return(scavenge_level)

# def travel():

#     destination = input("Enter grid coordinate of desired location (ex: A1, B4, etc")