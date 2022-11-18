'''
 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
      Project: HB3 - Lab 01 version 2
      Author: Scott Lefgren
      Email: scojlefg@gmail.com
      Date: November 17, 2022
                    ___-___  o==o======   .   .   .   .   .
            =========== ||//
                    \ \ |//__
                    #_______/
                    
 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
'''
''' Version 2
Allow the user to also enter the units. Then depending on the units, 
convert the distance into meters. The units we'll allow are feet, 
miles, meters, and kilometers.

1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m

Below is some sample input/output:

> what is the distance? 100
> what are the units? mi
> 100 mi is 160934 m
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
print("This program will convert units of your choice to meters\n")

# Ask the user for the distance
user_input_num = input("What is the distance?:  ")
# convert the input into an float
user_input_num = float(user_input_num)
# Ask the user for what units
user_input_units = input("What are the units? (Choose-- ft, mi, m, km):  ")

conversion_num = multiply(user_input_num,unit_convert[user_input_units])

print(f'{user_input_num} {user_input_units} is {round(conversion_num,4)} m')

# THE END

#    \_\
#    (_**)
#   __) #_
#  ( )...()
#  || | |I|
#  || | |()__/
#  /\(___)
# _-"""""""-_""-_
# -,,,,,,,,- ,,