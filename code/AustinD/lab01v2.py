conversion = {
    'ft' : 0.3048,
    'mi' : 1609.34,
    'm' : 1,
    'km' : 1000
}

while True:
    dist = int(input('what is the distance? '))
    start_unit = input('What is the unit being converted? ').lower()
    acceptable = ', '.join(conversion.keys())
    if start_unit not in conversion:
        print(f'Not an accepted value, please select {acceptable}')
        print(start_unit)
    else:
        measurement = (conversion[start_unit])
        converted = dist * measurement/(conversion['m'])
        print(f'{dist} {start_unit} is {converted} meters.')
        break 