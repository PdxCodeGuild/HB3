'''
 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
      Project: HB3 - Lab 01 version 1
      Version: 1.0
      Author: Scott Lefgren
      Email: scojlefg@gmail.com
      Date: November 17, 2022
         ___-___  o==o======   .   .   .   .   .
=========== ||//
        \ \ |//__
        #_______/

 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
'''
''' Version 1

Ask the user for the number of feet, and print out the equivalent 
distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output 
in meters by multiplying the input distance by 0.3048.

Below is some sample input/output.
> what is the distance in feet? 12
> 12 ft is 3.6576 m
'''
import math

ft_unit_convert = 0.3048  # Unit conversion (1 ft = 0.3048)

# define simple multiply function
def multiply(a,b):
    return a * b
# end def multiply

print("Welcome to the Distance Converter Program")
print("This program will convert feet into meters\n")

user_input_num = input("What is the distance in feet?  ")
# convert the input into an float
user_input_num = float(user_input_num)

conversion_num = multiply(user_input_num,ft_unit_convert)

print(f'{user_input_num} ft is {round(conversion_num,4)} m')

# THE END

#      ,     ,
#     (\____/)
#      (_oo_)
#        (O)
#      __||__    \)
#   []/______\[] /
#   / \______/ \/
#  /    /__\
# (\   /____\
