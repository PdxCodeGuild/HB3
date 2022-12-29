conversion_dict = {
    'ft' : 0.3048,
    'mi' : 1609.34,
    'm' : 1,
    'km' : 1000,
    'yd' : 0.9144,
    'in' : 0.0254
}

distance_in = input("Enter distance ")
unit_in = input("Enter unit to convert from (ft, mi, m, km, yd, in) ")
unit_out = input("Enter unit to convert to (ft, mi, m, km, yd, in) ")

in_meters = int(distance_in) * conversion_dict[unit_in]
distance_out = round(in_meters / conversion_dict[unit_out], 2)

print(f"{distance_in}{unit_in} is {distance_out}{unit_out} ")