# write a program that allows the user to convert a number between units
#v.4
user_input_distance = float(input('What is the distance?: '))
user_input_start_units = input('What are the input units(ft, m, mi, km)?: ')
user_input_end_units = input('What are the output units(ft, m, mi, km)?: ')
# create a dictionary to store the conversion ratios
ratios = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
}
# convert the units to meters
result_m = round(user_input_distance * ratios[user_input_start_units], 4)
# covert meters to the output unit desired
if user_input_end_units == 'ft':
    result = result_m * (1/.3048)
elif user_input_end_units == 'mi':
    result = result_m * (1/1609.34)
elif user_input_end_units == 'km':
    result = result_m * (1/1000)
elif user_input_start_units == 'km' and user_input_end_units == 'm':
    result = result_m
else:
    result = user_input_distance
# print the result
print(f" {user_input_distance} {user_input_start_units} is {result} {user_input_end_units}")