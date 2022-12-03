conversion = {
    'ft' : 0.3048,
    'mi' : 1609.34,
    'm' : 1,
    'km' : 1000,
    'yards' : 0.9144,
    'inches' : 0.0254
}

while True:
    dist = int(input('what is the distance? '))
    start_unit = input('What is the unit being converted? ').lower()
    end_unit = input('What is the unit being converted to? ').lower()
    acceptable = ', '.join(conversion.keys())
    if start_unit not in conversion:
        print(f'Not an accepted value, please select {acceptable}')
        print(start_unit)
    if end_unit not in conversion:
        print(f'Not an accepted value, please select {acceptable}')
        print(end_unit)
    else:
        measurement = (conversion[start_unit])
        target = (conversion[end_unit])
        converted = dist * measurement/target
        print(f'{dist} {start_unit} is {converted} {end_unit}')
        break 