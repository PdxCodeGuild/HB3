# Lab 7 -> Dad jokes
import requests

response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
data = response.json()
print(data.get('joke'))