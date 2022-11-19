# Asking user to enter a number and unit of conversion
user = int(input('what is the distance in feet: '))
from_unit = input('What are the unit: ')
to_unit = input('What are the output? ')
# Create a dictionary with conversion
distance ={'ft': 0.3048,
           'mi': 1609.34,
           'km': 1000,
           'm': 1,
           'yrd': 0.9144,
           'in': 0.0254
           }
# create a for loop to convert any unit to meters, then convert the distance in meters to any other unit.
for x in distance:
    x = distance[from_unit]*user
    y = x/distance[to_unit]
    break
print(f'{user} {from_unit} is {y} {to_unit}')
