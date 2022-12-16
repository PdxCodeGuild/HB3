print('Lab 10: Quotes Lab Version 2')

 
import requests
import json
 
keyword = input('Enter a keyword to search for quotes: ')
 
page = 1
 
while True:
    #response = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={keyword}')
 
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    
    response = requests.get((f'https://favqs.com/api/quotes?page={page}&filter={keyword}'), headers=headers)
    #response.encoding = 'utf-8'
    quoter = response.json()
    
    quotes = len(quoter['quotes'])
    
 
    print(f'{quotes} quotes associated with {keyword} - page {page}')
    
    statements = quoter['quotes']
    for statement in statements:
        print('_____________________________________________________________________')
        print(statement['author'])
        print(statement['body'])
    
    proceed = input("Enter 'next page' or 'done': ")
 
    if proceed == 'next page':
        page = page + 1
    elif proceed == 'done':
        print('Goodbye!')
        break
    
