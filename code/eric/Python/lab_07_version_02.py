# Lab 7v2 -> Dad jokes
import requests
import time


term = input('Enter a term to search: ')
response = requests.get(f'https://icanhazdadjoke.com/search?term={term}', headers={'Accept': 'application/json'})
data = response.json()

print(f'There are', data['total_jokes'], 'jokes aasssociated with this term.')

for x in data['results']:
    print(x.get('joke'))
    time.sleep(3)