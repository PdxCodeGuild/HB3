# create a dictionary with a key:value pair for english and metric to metric
dict_to_meters = {
    'in':.0254,
    'yd':.9144,
    'ft':.3048,
    'mi':1609.34,
    'm' :1,
    'km':1000,    
    }

#create a dictionary with a key:value pair for the conversion from metric to english
dict_from_meters = {
    'in':1/0.0254,
    'yd':1/0.9144,
    'ft':1/0.3048,
    'mi':1/1609.34,
    'm' :1,
    'km':1/1000,    
    }

distance = int(input("What is the distance? "))
units_from = input("What are the units (in, yd, ft, mi, m, km)? ")
units_to = input("What are the output units (in, yd, ft, mi, m, km)? ")

# create a function that takes three parameters: distance, units_from, and units_to
def convert(distance, units_from, units_to):
    total = dict_to_meters.get(units_from) * distance # get the distance in meters
    answer = total * dict_from_meters.get(units_to) # convert the distance from meters to the required units
    return answer

conversion = convert(distance, units_from, units_to)

# output the equivalent distance in meters.
print(f'{distance} {units_from} is {conversion:.2} {units_to}')