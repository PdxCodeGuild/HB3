conversion_dict = {
    'ft' : 0.3048,
    'mi' : 1609.34,
    'm' : 1,
    'km' : 1000
}

distance_in = input("Enter distance ")
unit = input("Enter unit (ft, mi, m, km) ")

distance_out = round(int(distance_in) * conversion_dict[unit], 2)

print(f"{distance_in}{unit} is {distance_out}m ")