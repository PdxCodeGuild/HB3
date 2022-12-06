import requests

#response = requests.get('https://icanhazdadjoke.com/', headers={'accept': 'application/json'})

search_term = input('Search Term or "done": ')
for search_term in search_term :
    if search_term == "done" :
        print("Thank You!")
    

    elif search_term != "done" :
        search = (f'https://icanhazdadjoke.com/search?term={search_term}')
        search_response = requests.get(search, headers={'accept': 'application/json'})

    data_dict = {}     
    data_dict.update(search_response.json())
    for data in data_dict :
        print(data_dict.get('joke'))
    #for x in jokes :
     #   print(jokes.get('joke'))
                # figure out how to print just one joke
    
                # then go to next joke, etc
                # "another" or done for break
    

   



