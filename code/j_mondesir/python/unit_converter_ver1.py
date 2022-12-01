# Asking user to enter a number 
user = int(input('what is the distance in feet: '))
# Create a dictionary with conversion
distance ={'meter': 0.3048*user}
# Print answer to user
print(user,'ft is', distance['meter'], 'm')