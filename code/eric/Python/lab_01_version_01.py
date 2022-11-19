# write a program that allows the user to convert a number between units

# v.1
user_input = float(input('What is the distance in feet?: '))
ratio = {'ft': 0.3048}
result = round(user_input * ratio['ft'], 4)
print(user_input, "ft", "is", result, "m")