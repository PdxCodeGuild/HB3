units = {
    "feet": .3048
}

distance = input('\nWhat is the distance in feet?: ')

distance = int(distance)

meters = distance * units['feet']

print(f"\n{distance} ft is {round(meters, 4)} m\n")