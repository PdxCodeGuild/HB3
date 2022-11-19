# Unit Convertor


print("Welcome To Unit Converter!!!!")

units = ['ft', 'mi', 'm', 'km']

num = int(input('Please what is your distance in number?\n'))

print(f'Please choose from the following units:')

# running for loop to get all the units from the list.
for unit in units:
    print(unit, end='  ')
  
choice = str(input('\nPlease enter your unit?\n'))


# conditional statements
if choice in units:
    if choice == 'ft':
        conv_num = num * 0.3048

    elif choice == 'mi':
        conv_num = num * 1609.34

    elif choice == 'm':
        conv_num = num * 1

    elif choice == 'km':
        conv_num = num * 1000   


print(f"Your distance {num}{choice} is equal to {conv_num}m")