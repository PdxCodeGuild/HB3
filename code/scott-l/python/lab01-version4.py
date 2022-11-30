'''
 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
      Project: HB3 - Lab 01 version 4
      Author: Scott Lefgren
      Email: scojlefg@gmail.com
      Date: November 17, 2022
                    ___-___  o==o======   .   .   .   .   .
            =========== ||//
                    \ \ |//__
                    #_______/
                    
 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
'''
''' 
Version 4

Now we'll ask the user for the distance, the starting units, 
and the units to convert to.

You can think of the values for the conversions as elements in a matrix, 
where the rows will be the units you're converting from, and the columns 
will be the units you're converting to. Along the horizontal, the values 
will be 1 (1 meter is 1 meter, 1 foot is 1 foot, etc).

But instead of filling out that matrix, and checking for each pair of units 
(if from_units == 'mi' and to_units == 'km'), we can just convert any unit 
to meters, then convert the distance in meters to any other unit.

Furthermore you can convert them from meters by dividing a distance (in meters) 
by those same values used above. So first convert from the input units to meters, 
then convert from meters to the output units.

Below is some sample input/output:

> what is the distance? 100
> what are the input units? ft
> what are the output units? mi
100 ft is 0.0189394 mi

'''
import math

# define simple multiply function
def multiply(a,b):
    return a * b
# end def multiply

# create a unit conversion dictionary
unit_convert = {
    'ft': 0.3048,  # (1 foot = 0.3048 meters)
    'mi': 1609.34, # (1 mile = 1609.34 meters)
    'm' : 1, # (1 meter = 1 meter)
    'km': 1000 # (1 km is 1000 meters)
}

print("Welcome to the Distance Converter Program")
print("This program will convert units of your choice\n")

# Ask the user for the distance
user_input_num = input("What is the distance?:  ")
# convert the input into an float
user_input_num = float(user_input_num)
# Ask the user what are the input units
user_input_units = input("What are the input units? (Choose-- ft, mi, m, km):  ")
# first convert the input units to meters
conversion_num_meters = multiply(user_input_num,unit_convert[user_input_units])

# Ask the user what are the output units
user_output_units = input("What are the output units? (Choose-- ft, mi, m, km):  ")
# Convert from meters by dividing a distance in meters by the same values in the unit
# conversion. 
conversion_output_result = (conversion_num_meters/unit_convert[user_output_units])

print(f'{user_input_num} {user_input_units} is {round(conversion_output_result,4)} {user_output_units}')

# THE END

#       [ ]
#      (   )
#       |>|
#    __/===\__
#   //| o=o |\\
# <]  | o=o |  [>
#     \=====/
#    / / | \ \
#   <_________>