dictionary = {'meters': .3048} #I have created a list with 1 as the key and value 0.3058 as this is what we multiply
user = input('What is the distance in feet: ') #input statment for user in feet
base = dictionary['meters'] #I have created a variable with the key from my dictionary
print(f'{user} ft is {int(user) * round(base, 4)} m') 