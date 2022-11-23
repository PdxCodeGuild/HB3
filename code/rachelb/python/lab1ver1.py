distance = int(input('what is the distance? '))
from_input = input('what are the input units? ')
to_input = input('what are the output units? ')


feet = 0.3048* distance
mile = 1609.34 * distance
meter = 1 * distance
kilometer = 1000 * distance


#conversion
#If 1 ft equals
#0.000189394 / 1 ft = 000189394 * 100 (input) = 0.018939

if from_input == 'ft':
    print(f'{distance} is {feet} mi')
elif from_input == 'mi':
    print(f'{distance} is {mile} mi')
elif from_input == 'm':
    print(f'{distance} is {meter} mi')
