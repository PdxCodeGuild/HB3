#---------------------------------
# PDX Code Guild: HB3
# Lab01: Unit Converter
# Author: Daniel Smith
# Date: 2022.11.17
#---------------------------------

# Ask the user for the numerical distance, the input unit of measure, and the output unit of measure.
dist_input = float(input('What is the distance? '))
unit_input = input('What are the input units (mi, yd, ft, in, km, m, cm, mm)? ')
unit_output = input('What are the output units (mi, yd, ft, in, km, m, cm, mm)? ')

# Initialize a dictionary that stores units of measure and their respective conversion ratios from 1 meter as key:value pairs.
conversion_table = {
    'mi': 1609.34,
    'yd': 0.9144,
    'ft': 0.3048,
    'in': 0.0254,
    'km': 1000,
    'm' : 1,
    'cm': 0.01,
    'mm': 0.001
    }

# Convert the input distance from the input units to meters, then convert from meters to the output units.
dist_in_meters = dist_input * conversion_table[unit_input]
converted_output = round(dist_in_meters / conversion_table[unit_output], 4) # Round the output to 4 sigfigs.
print(f'\n{dist_input} {unit_input} is {converted_output} {unit_output}\n') # Format and pass the data to the terminal.