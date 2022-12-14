import requests

response = requests.get('https://icanhazdadjoke.com/', headers={'accept': 'application/json'})

search_term = input('Search Term or "done": ')

if search_term == 'done' :
    print("Thanks for playing!")

else :
    search = (f'https://icanhazdadjoke.com/search?term={search_term}')
    response = requests.get(search , headers={'accept': 'application/json'})


data_dict = {}
data_dict.update(response.json())
jokes = data_dict.pop('results')
joke_list = [x['joke'] for x in jokes]


index = 0  
for joke in joke_list :
    print(joke_list[index])
    another = input("Would you like to hear another? Y/N: ")
    index += 1
    if another == 'Y' :
        continue
    
    elif another == 'N' :
        print("Thanks for playing!")
        break

page_number = 1
if index >= 19:
    page = input("Would you like to go to the next page? Y/N: ")
    if page == 'N' :
        print("Thanks for playing!")
    elif page == 'Y' :
        page_number += 1
        search = (f'https://icanhazdadjoke.com/search?term={search_term}/search?page={page_number}')
        response = requests.get(search , headers={'accept': 'application/json'})
    data_dict = {}
    data_dict.update(response.json())
    jokes = data_dict.pop('results')
    joke_list = [x['joke'] for x in jokes]
    index = 0  
    for joke in joke_list :
        print(joke_list[index])
        another = input("Would you like to hear another? Y/N: ")
        index += 1
        if another == 'Y' :
            continue
    
        elif another == 'N' :
            print("Thanks for playing!")
            break
    


    







    
