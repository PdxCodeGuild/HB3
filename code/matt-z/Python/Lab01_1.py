# ask the user for a distance in feet
distance_from = int(input("What is the distance in feet? "))

# multiply the distance by .3048 because 1 ft is .3048 m
distance_to = distance_from * .3048

print(f'{distance_from} ft is {distance_to} m')