import requests 
import json

#filter =
# page = 1
#Find base url 
#Find end point 
#gram request  -----  r = request.get(baseurl + endpoint)
response = requests.get('https://favqs.com/api/qotd', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

data = response.json()
#body , id , url, author, pages
# print(response)---- Helps check our code
quote = data.get('quote').get('body')
author = data.get('quote').get('author')
# print(quote)
# print(author)


keyword = input('enter a keyword to search for quotes:')
page = input("enter 'next page' or 'done': ")
#Pages = 1 + next page
response = requests.get(f'https://favqs.com/api/quotes?page={page}>&filter=<{keyword}>',
headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

quotes = data.get('quote').get('body')
authors = data.get('quote').get('author')
