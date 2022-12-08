# Lab 10v1 -> Get a random quote

import requests

response = requests.get('https://favqs.com/api/qotd', headers={'Accept': 'application/json'})
data = response.json()

author = data.get('quote').get('author')
body = data.get('quote').get('body')

print('The quote of the day is:', '\n', '"'+ body+'"')
print('\t', '~', author)