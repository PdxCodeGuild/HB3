import requests

response = requests.get('https://favqs.com/api/qotd')

r = response.json()

quote = r.get('quote').get('body')
author = r.get('quote').get('author')

print(quote, author)