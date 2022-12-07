print('\n\tDad Joke Lab 07')

import requests

response = requests.get('https://icanhazdadjoke.com/', headers = ('accept': ))

data = response.json()

print(data.get('joke'))