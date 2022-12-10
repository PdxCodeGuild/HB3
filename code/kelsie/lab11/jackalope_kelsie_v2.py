import random
from string import ascii_lowercase , digits

jackalopes_list = [
{'name' : '1a',
'age' : 0,
'sex' : 'f',
'pregnant' : 'n'},
{'name' : '2a',
'age' : 0,
'sex' : 'm',
'pregnant' : 'n'}
]
print(len(jackalopes_list))

years = 0
while len(jackalopes_list) < 1000 : 
    # add to each jackalopes age
    for index in range(len(jackalopes_list)) :
        if jackalopes_list[index]['age'] >= 4 and jackalopes_list[index]['age'] <= 8 and jackalopes_list[index]['sex'] == 'f' and jackalopes_list[index]['pregnant'] == 'n':

                new_jackalope = {
                    'name' :(''.join(random.choice(digits)) + ''.join(random.choice(ascii_lowercase))) , # creating a random name from a number and letter
                    'age' : 0,
                    'sex' : (random.choice('mf')), # random male or female
                    'pregnant' : 'N',
                    }

                new_jack_copy = new_jackalope.copy()
                jackalopes_list.append(new_jack_copy) # adding the new jackalope to the list 
        jackalopes_list[index]['age'] += 1
        if jackalopes_list[index]['age'] == 10:
            del jackalopes_list[index]
years +=1


   
        #[{k:v for k,v in d.items() if v == 10} for d in jackalopes_list]
        #jackalopes_list = (list(filter(lambda a: a!= ['age' : 10], jackalopes_list)))
    

#print(years)
print(jackalopes_list)