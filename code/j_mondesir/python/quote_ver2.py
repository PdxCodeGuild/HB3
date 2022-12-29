import requests
import json
user_search = input('enter a keyword to search for quotes:\n> ')
page = 1
response = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={user_search}', headers = {'accept': 'application/json','Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
data = response.json()
for quotes in data['quotes']:
    print(quotes['body'])
while True:
    next_page = input('Enter Next to continue or Exit to stop: \n> ')
    if next_page == 'Next':
        page += 1
        response = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={user_search}', headers = {'accept': 'application/json','Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
        data = response.json()
        for quotes in data['quotes']:
            print(quotes['body'])
            #page += 1
        print(f'---Page {page} ---')
    else:
        break
    
