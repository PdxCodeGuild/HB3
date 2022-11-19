# write a program that allows the user to convert a number between units
# v.2 & 3 
user_input_distance = float(input('What is the distance?: '))
user_input_units = input('What are the units(ft, m, mi, km, yd, in)?: ')

# create a dictionary to store the conversion ratios
ratios = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254,
    }
# convert the units 
result = round(user_input_distance * ratios[user_input_units], 4)
# print the result
print(f" {user_input_distance} {user_input_units} is {result} m")