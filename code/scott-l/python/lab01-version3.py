'''
 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
      Project: HB3 - Lab 01 version 3
      Author: Scott Lefgren
      Email: scojlefg@gmail.com
      Date: November 17, 2022
                    ___-___  o==o======   .   .   .   .   .
            =========== ||//
                    \ \ |//__
                    #_______/
                    
 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
'''
''' Version 3

Add support for yards, and inches.

1 yard is 0.9144 m
1 inch is 0.0254 m

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
    'km': 1000, # (1 km is 1000 meters)
    'yd': 0.9144, #( 1 yard is 0.9144 meters)
    'in': 0.0254 # (1 inch is 0.0254 meters)
}

print("Welcome to the Distance Converter Program")
print("This program will convert units of your choice to meters\n")

# Ask the user for the distance
user_input_num = input("What is the distance?:  ")
# convert the input into an float
user_input_num = float(user_input_num)
# Ask the user for what units
user_input_units = input("What are the units? (Choose-- ft, mi, m, km, yd, in):  ")

conversion_num = multiply(user_input_num,unit_convert[user_input_units])

print(f'{user_input_num} {user_input_units} is {round(conversion_num,4)} m')

# THE END

# _(\     |@@|
# (__/\__ \--/ __
#    \___|----|  |   __
#        \ }{ /\ )_ / _\
#        /\__/\ \__O (__
#       (--/\--)    \__/
#       _)(  )(_
#      `---''---`