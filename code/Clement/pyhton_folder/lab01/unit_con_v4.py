# Unit Convertor


print("Welcome To Unit Converter!!!!")

units = ['ft', 'mi', 'm', 'km']

num = int(input('Please what is your distance in number?\n'))

print(f'Please choose from the following units:')

# running for loop to get all the units from the list.
for unit in units:
    print(unit, end='  ')

#   asking the user input
choice_1 = str(input('Please enter your unit?\n'))
choice_2 = str(input('Please enter your unit?\n'))


# conditional statements
# (if from_units == 'mi' and to_units == 'km')
if choice_1 in units and choice_2:

# ===================For feet to other units=====================

    if choice_1 == 'ft' and choice_2 == 'ft':
        converter_num = num * 1

    elif choice_1 == 'ft' and choice_2 == 'mi':
        converter_num = num * 0.000189394

    elif choice_1 == 'ft' and choice_2 == 'm':
        converter_num = num * 0.3048

    elif choice_1 == 'ft' and choice_2 == 'km':
        converter_num = num * 0.0003048

# ===================For mile to other units=====================
    
    elif choice_1 == 'mi' and choice_2 == 'mi':
        converter_num = num * 1 

    elif choice_1 == 'mi' and choice_2 == 'ft':
        converter_num = num * 5280

    elif choice_1 == 'mi' and choice_2 == 'm':
        converter_num = num * 1609.34

    elif choice_1 == 'mi' and choice_2 == 'km':
        converter_num = num * 1.60934
  

# ===================For meter to other units=====================

    elif choice_1 == 'm' and choice_2 == 'm':
        converter_num = num * 1 

    elif choice_1 == 'm' and choice_2 == 'ft':
        converter_num = num / 0.3048

    elif choice_1 == 'm' and choice_2 == 'mi':
        converter_num = num / 1609.34

    elif choice_1 == 'm' and choice_2 == 'km':
        converter_num = num / 1000

    
# ===================For kilometer to other units=====================
    
    elif choice_1 == 'km' and choice_2 == 'km':
        converter_num = num * 1 

    elif choice_1 == 'km' and choice_2 == 'ft':
        converter_num = num * 3280.84

    elif choice_1 == 'km' and choice_2 == 'mi':
        converter_num = num * 0.621371

    elif choice_1 == 'km' and choice_2 == 'm':
        converter_num = num * 1000
    

print(f"Your distance {num}{choice_1} is equal to {converter_num}{choice_2}")