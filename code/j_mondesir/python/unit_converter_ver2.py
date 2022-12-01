# Asking user to enter a number and unit of conversion
user = int(input('what is the distance in feet: '))
user_2 = input('What are the unit: ')
# Create a dictionary with conversion
distance ={'ft': 0.3048,
           'mi': 1609.34,
           'km': 1000,
           'm': 1,
           'yrd': 0.9144,
           'in': 0.0254
           }
# Print answer to user
print(user, user_2, 'is', distance[user_2]*user, 'm')