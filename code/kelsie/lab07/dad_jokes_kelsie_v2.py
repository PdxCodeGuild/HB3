import requests

response = requests.get('https://icanhazdadjoke.com/', headers={'accept': 'application/json'})

search_term = input('Search Term or "done": ')
for word in search_term:
    if search_term == 'done' :
        print("Thanks for playing!")
    else :
        search = (f'https://icanhazdadjoke.com/search?term={search_term}')
        response = requests.get(search , headers={'accept': 'application/json'})
data = response.json()
print(list(data))












   
#data_list.append(search_response.json())
#print(data_list)
#jokes = []
#for data in data_list :
#    [ x['joke'] for x in data_list]
    
    
#print(jokes)
    #for data in data_list :
     #   print(data_list.get('joke'))
    
                # figure out how to print just one joke
    
                # then go to next joke, etc
                # "another" or done for break
    

   



