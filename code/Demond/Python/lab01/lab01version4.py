dictionary_2 = {'ft':0.3048 , 'mi':1609.34 , 'km':1000, 'm': 1} #I have created a dictionary with the conversions 
distance = input('What is the distance?: ') # I have made a variable for user input for distance
units = input('What are the input units?: ') #I have made a variable for user input for units
ounits = input('What are the output units?') #I have made a variable for user input for user outputs
converts = (float(distance) * float(dictionary_2[units])) #this should convert the units to meters and then convert the appropraite output
if ounits == 'ft':
    answer = converts * 1/.3048
elif ounits == 'mi':
    answer = converts * 1/1609.34
elif ounits == 'km':
    answer = converts * 1/1000
elif units == 'km' and ounits == 'm':
    answer = converts
else:
    answer = distance
print(f" {distance} {units} is {answer} {ounits}") #this print statment will show the results