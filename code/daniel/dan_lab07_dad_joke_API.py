#---------------------------------
# PDX Code Guild: HB3
# Lab07: Dad Joke API
# Author: Daniel Smith
# Date: 2022.12.2
#---------------------------------

# Use the Dad Joke API to get a dad joke and display it to the user.
# You may want to also use time.sleep to add suspense.
from time import sleep

# Part 1
# Use the requests library to send an HTTP request to https://icanhazdadjoke.com/
# with the accept header as application/json.
# This will return a dad joke in JSON format.
# You can then use the .json() method on the response to get a dictionary.
# Get the joke out of the dictionary and show it to the user.
from requests import get

response = get('https://icanhazdadjoke.com/', headers={'accept': 'application/json'})
data = response.json()
print('\n')
print(data.get('joke'))
print('\n')

# Part 2
# Add the ability to "search" for jokes using another endpoint.
# Create a REPL that allows one to enter a search term and go through
# jokes one at a time. You can also add support for multiple pages.
while True:
    
    searchterm = input('Enter a joke search term: ')
    response = get(f'https://icanhazdadjoke.com/search?term={searchterm}', headers={'accept':'application/json'})
    data = response.json()
    results = data['results']

    for i in range(len(results)):
        joke = results[i]['joke']
        print('.')
        sleep(0.5)
        print('..')
        sleep(0.5)
        print('...')
        sleep(0.5)
        print(f'\n{joke}')
        print('\n')
        userinput = input('Press Enter...')

    print(f'\nWe ain\'t got no mo jokes containing no "{searchterm}"... Goodbye!\n') 
    break