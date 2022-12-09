import requests

keyword = input("Enter a keyword to search for quotes: ")
page = 1

while True:
    response = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={keyword}', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

    r = response.json()

    number_of_quotes = len(r['quotes'])

    print(f'{number_of_quotes} quotes associated with {keyword} - page {page}')

    for i in r['quotes']:
        print(i.get('body') + ' By: ' + i.get('author'))
        
    next_or_done = input("Enter 'next page' or 'done': ")
    if next_or_done == 'done':
        break
    if next_or_done == 'next page':
        page += 1