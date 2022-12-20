import random
from string import ascii_lowercase , digits

jackalopes_list = [
{'name' : '1a',
'age' : 0,
'sex' : 'f',
'pregnant' : 'N'},

{'name' : '2a',
'age' : 0,
'sex' : 'm',
'pregnant' : 'N'}
]

print(len(jackalopes_list))




years = 0
while True:

    for index in range(len(jackalopes_list)) :

        if (jackalopes_list[index]['age']) >= 4 and (jackalopes_list[index]['age']) <= 8 :
            if (jackalopes_list[index]['sex']) == 'f' and (jackalopes_list[index]['pregnant']) == 'N':
                (jackalopes_list[index]['pregnant']) = 'Y'
                    
                    
                    
            if (jackalopes_list[index]['pregnant']) == 'Y' :    
                    new_jackalope = {
                    'name' :(''.join(random.choice(digits)) + ''.join(random.choice(ascii_lowercase))) , # creating a random name from a number and letter
                    'age' : 0,
                    'sex' : (random.choice('mf')), # random male or female
                    'pregnant' : 'N',
                    }

                    new_jack_copy = new_jackalope.copy()
                    jackalopes_list.append(new_jack_copy) # adding the new jackalope to the list 
                    

        if (jackalopes_list[index]['age']) == 10:
            del jackalopes_list[index]
    
        (jackalopes_list[index]['age']) += 1
        years +=1
        if len(jackalopes_list) == 1000 :
            break

        

print(years)
print(jackalopes_list)
