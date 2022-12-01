# create a dictionary with a key:value pair for english and metric to metric
dict_to_meters = {
    'ft':.3048,
    'mi':1609.34,
    'm' :1,
    'km':1000,    
    }

# ask the user for the distance and store it as an int
distance = int(input("What is the distance? "))
units_from = input("What are the units (ft, mi, m, km)? ")

# look up the value from the dictionary for the units being converted from and multiply by distance
total = dict_to_meters.get(units_from) * distance

print(f'{distance} {units_from} is {total} m')