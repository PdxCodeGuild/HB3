distance = { # converting to meters distance
    '1 ft': 0.3048,
}

dist_feet = input("What is the distance in feet?: ")
dist_meters = float(dist_feet) * distance["1 ft"]

print(f"{dist_feet} feet is {round(dist_meters)} meters.")