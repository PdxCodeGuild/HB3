import requests
import json

response = requests.get('https://favqs.com/api/qotd', headers={'accept': 'application/json'})

data = response.json()
quotes_author = data['quote']['author']
quote = data['quote']['body']

print(f'{quote} The author is {quotes_author}')
