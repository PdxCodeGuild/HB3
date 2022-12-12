# Lab 10v2 -> list quotes by keyword
# Prompt the user for a keyword, list the quotes you get in response,
# and prompt the user to either show the next page or enter a new keyword. 
# You can use string concatenation to build the URL.

import requests

key_word = input("Enter a keyword to search for quotes: ")

next_page = 0
while next_page != 'done':
    page_num = 1
    # search the website and get the data
    url = (f'https://favqs.com/api/quotes?page={page_num}&filter={key_word}')
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    response = requests.get(url, headers=headers)
    data = response.json()
    num_quotes = len(data['quotes'])

    if page_num == 1:
        print(f'{num_quotes} quotes are associated with {key_word} - page {page_num}')
        for onequote in data['quotes']:
            print('\n', onequote.get('body'))
        next_page = input('Enter "next page" or "done": ')
        if next_page == 'done':
            break
        page_num = page_num + 1
    
    if page_num != 1:
            print(f'{num_quotes} quotes are associated with {key_word} - page {page_num}')
            url = (f'https://favqs.com/api/quotes?page={page_num}&filter={key_word}')
            headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
            response = requests.get(url, headers=headers)
            data = response.json()
            for onequote in data['quotes']:
                print('\n', onequote.get('body'))
            page_num = page_num + 1
            next_page = input('Enter "next page" or "done": ')
            if next_page == 'done':
                break
   
