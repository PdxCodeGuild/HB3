dictionary_2 = {'ft':0.3048 , 'mi':1609.34 , 'km':1000, 'm': 1} #I have created a dictionary with the conversions 
distance = input('What is the distance?: ') # I have made a variable for user input for distance
units = input('What are the input units?: ') #I have made a variable for user input for units
ounits = input('What are the output units?')
answer = dictionary_2.get(units, ) #This .GET method will check for keys and output the value
x = int(distance) * int(answer)
print(x)