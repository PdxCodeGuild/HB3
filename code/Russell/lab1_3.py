conversion_dict = {
    'ft' : 0.3048,
    'mi' : 1609.34,
    'm' : 1,
    'km' : 1000,
    'yd' : 0.9144,
    'in' : 0.0254
}

distance_in = input("Enter distance ")
unit = input("Enter unit (ft, mi, m, km) ")

distance_out = round(int(distance_in) * conversion_dict[unit], 2)
