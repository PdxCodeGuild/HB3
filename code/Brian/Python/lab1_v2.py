distance = { # converting to meters distance
    'ft': 0.3048, 
    'mi': 1609.34, 
    'm': 1, 
    'km': 1000,
}

# created distance list for usage in later function line
distance_list = ["ft, mi, m, km"]

# created user_distance variable which equates to using the input function to capture what the user will record
user_distance = input('What is the distance?: ')


'''
created user_units variable which equates to a user inputted f string which asks what units of measurement are being entered 
by the user, while showing them the list of available unit of measurements from the earlier created 
distance_list , without brackets thanks to the join function
'''
user_units = input(f"What are the units? Your available options are {', '.join(distance_list)}: ")


'''
created selected_distance variable to equate what the solution would be between the float variation of the users' inputted distance
and multiplying that by the distance dictionary which contains the user_units string so that the users' inputted unit of measure would
match up with what is within my key and values in the distance dictionary above
'''
selected_distance = float(user_distance) * distance[user_units]

'''
created print function with f string to print out the users' inputted distance and units of measurement stating that what they inputted is
the rounded version of their answer, utilizing the round function on my selected_distance variable cerated earlier.
'''
print(f"{user_distance} {user_units} is {round(selected_distance)} m")