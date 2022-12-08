#---------------------------------
# PDX Code Guild: HB3
# Lab10: Quotes API
# Author: Daniel Smith
# Date: 2022.12.7
#---------------------------------

# Version 1: Get a Random Quote
# The URL to get a random quote is https://favqs.com/api/qotd.
# Send a request,
# parse the JSON in the response into a python dictionary,
# then show the quote and the author.

import requests
response = requests.get('https://favqs.com/api/qotd')
response_dict = response.json()
print('\n')
print('Random Quote:')
print(response_dict.get('quote').get('body'))
print(response_dict.get('quote').get('author'))
print('\n')

# Version 2: List Quotes by Keyword
# The Favqs Quote API also supports getting a list of quotes associated with
# a given keyword https://favqs.com/api/quotes?page=<page>&filter=<keyword>.
# Prompt the user for a keyword,
# list the quotes you get in response,
# and prompt the user to either show the next page or enter a new keyword.
# You can use string concatenation to build the URL.

keyword = '' # initialize keyword variable here so we can use it as a conditional for the while loop.
while keyword != 'done':
    keyword = input('Enter a keyword to search for quotes: ')
    page = 1 # initialize a results page counter
    user_input = '' # initialize user_input here so we can use it as a conditional for the while loop.
    while user_input != 'done':
        r2 = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={keyword}', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
        r2dict = r2.json()
        quotes_qty = len(r2dict['quotes'])
        print(f'{quotes_qty} quotes associated with {keyword} - page {page}\n')
        for quote in r2dict['quotes']:
            print(quote.get('body'))
            print(quote.get('author'))
            print('\n')
        user_input = input("Enter 'next page' or 'done': ")
        if r2dict.get('last_page') == True: # catch final page of results to prevent overflow
            user_input = 'done'
        else:
            page += 1

# "The pursuit of truth and beauty is a sphere of activity in which we are permitted to remain children all our lives."
# - Albert Einstein