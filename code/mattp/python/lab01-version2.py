units = {
    "feet": .3048
}

distance = input('\nWhat is the distance in feet?: ')

distance = int(distance)

meters = distance * units['feet']

print(f"\n{distance} ft is {round(meters, 4)} m\n")

########### Version 2

print('\nVersion 2')
#adding to units dictionary

units['miles'] = 1609.34   #adding the extra conversions
units['meters'] = 1
units['kilometers'] = 1000

measurement = input('\nWhat is the distance?: ')

measurement = int(measurement)

unit = input('\nWhat unit are you converting to meters (feet, miles, meters, kilometers)?: ')

unit_switch = units[unit]

conversion = measurement * unit_switch

print(f'\n{measurement} {unit} is {round(conversion, 4)} meters.')
