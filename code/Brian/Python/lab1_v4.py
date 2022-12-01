distance = { # dictionary for converting to meters distance
    'ft': 0.3048, 
    'mi': 1609.34, 
    'm': 1, 
    'km': 1000,
    'yd': 0.9144,
    'inch': 0.0254,
}

output_distance = { # dictionary to store conversions to and from other unit of measurements, other than meters
    'ft': 1/0.3048,
    'mi': 1/1609.34,
    'm': 1/1,
    'km': 1/1000,
    'yd': 1/0.9144,
    'inch': 1/0.0254,
}

# created distance list for usage in later function line
distance_list = ["ft, mi, m, km, yd, inch"]

# created user_distance variable which equates to using the input function to capture what the user will record
user_distance = input('What is the distance?: ')


'''
created user_units variable which equates to a user inputted f string which asks what units of measurement are being entered 
by the user, while showing them the list of available unit of measurements from the earlier created 
distance_list , without brackets thanks to the join function
'''
user_units = input(f"What are the units? Your available options are {', '.join(distance_list)}: ")

'''
created output_units to indicate the users' specific unit of measurement they'd like to get their measurement as
'''
output_units = input(f"What are the output units? Your available options are {', '.join(distance_list)}: ")


'''
created selected_distance variable to equate what the solution would be between the float variation of the users' inputted distance
and multiplying that by the distance dictionary which contains the user_units string so that the users' inputted unit of measure would
match up with what is within my key and values in the distance dictionary above
'''
selected_distance = float(user_distance) * distance[user_units]

'''
created selected_units variable to equate to what the solution is from the above selected_distance variable
and now multiplying that formula to the output_distance dictionary above by which unit of measurement the user chose
'''
selected_units = selected_distance * output_distance[output_units]

'''
created print function with f string to print out the users' inputted distance as well as the unit of measurement they chose
with now having their selected_unit of measurement calculated, with also including the output_units of the users'choice
'''
print(f"{user_distance} {user_units} is {round(selected_units)} {output_units}")