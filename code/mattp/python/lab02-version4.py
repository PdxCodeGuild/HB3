units = {
    "feet": .3048
}

#distance = int(distance)

#meters = distance * units['feet']

#print(f"\n{distance} ft is {round(meters, 4)} m\n")

########### Version 2

#print('\nVersion 2')
#adding to units dictionary

units['miles'] = 1609.34   #adding the extra conversions
units['meters'] = 1
units['kilometers'] = 1000

#measurement = input('\nWhat is the distance?: ')

#measurement = int(measurement)

#unit = input('\nWhat unit are you converting to meters (feet, miles, meters, kilometers)?: ')

#unit_switch = units[unit]

#conversion = measurement * unit_switch

#print(f'\n{measurement} {unit} is {round(conversion, 4)} meters.')

#print('\nVersion 3')
units['yards'] = 0.9144
units['inches'] = 0.0254

print(f'\n{units}')

#measurement = input('\nWhat is the distance?: ')

#measurement = int(measurement)

#unit = input('\nWhat unit are you converting to meters (feet, miles, meters, kilometers, yards, inches)?:')

#unit_switch = units[unit]

#conversion = measurement * unit_switch

#print(f'\n{measurement} {unit} is {round(conversion, 4)} meters.')

print('\nVersion 4')

distance = input('\nWhat is the distance: ')

distance = int(distance)

input_unit = input('\nWhat are the input units (feet, miles, meters, kilometers): ')

output_unit = input('\nWhat are the output units (feet, miles, meters, kilometers): ')

unit_switch = units[input_unit]

conversion = distance * unit_switch

print(conversion)