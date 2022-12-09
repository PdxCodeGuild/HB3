import random
from string import ascii_lowercase , digits

jackalopes_list = [
{'name' : '1a',
'age' : 0,
'sex' : 'f',
'pregnant' : 'n'},
{'name' : '2a',
'aga' : 0,
'sex' : 'm',
'pregnant' : 'n'}
]

print(jackalopes_list)

name = (''.join(random.choice(digits)) + ''.join(random.choice(ascii_lowercase)))
print(name)

new_jackalope = {
'name' :{name} ,
'age' : 0,
'sex' : (random.choice('mf')),
'pregnant' : 'N',
}

print(new_jackalope)

years = 0
while len(jackalopes_list) < 1000 : 
    # add one year
    years +=1
    # add to each jackalopes age
    for index in range(len(jackalopes_list)) :
        jackalopes_list[index]['age'] += 1
        print(jackalopes_list)

    # adding a new jackalope
    new_jack_copy = new_jackalope.copy()
    jackalopes_list.append(new_jack_copy) 
   
    
    #    if jackalopes_list[index] >=4 and jackalopes_list[index] <=8 :
    #        jackalopes_list.append(0)

    #    jackalopes_list = (list(filter(lambda a: a!= 10, jackalopes_list)))
    
    years += 1
#print(years)
print(jackalopes_list)