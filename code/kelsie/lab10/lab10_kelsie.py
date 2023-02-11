import requests

response = requests.get('https://favqs.com/api/qotd/' , headers={'accept': 'application/json'})

data = response.json()

info = data.get('quote')

author = info['author'] 
quote = info['body']

print(quote + ' - ' + author)