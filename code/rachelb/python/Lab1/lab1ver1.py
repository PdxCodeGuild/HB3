distance = int(input('what is the distance? '))
from_input = input('what are the input units? ')
to_input = input('what are the output units? ')

#convert to meters
unit = {'ft':0.3048,
'mi':1609.34, 
'm':1,
'km':1000}

#distance to any unit 
convert_to = distance * unit[from_input]
#Furthermore you can convert them FROM meters
#by dividing a distance 

unit_convert = convert_to / unit[to_input]
print(unit_convert)

#conversion
#If 1 ft equals
#0.000189394 / 1 ft = 000189394 * 100 (input) = 0.018939

# feet = 0.3048* distance
# mile = 1609.34 * distance
# meter = 1 * distance
# kilometer = 1000 * distance

# if from_input == 'ft':
#     print(f'{distance} is {feet} mi')
# elif from_input == 'mi':
#     print(f'{distance} is {mile} mi')
# elif from_input == 'm':
#     print(f'{distance} is {meter} mi')
# elif from_input == 'km' :
#         print(f'{distance} is {kilometer} mi')