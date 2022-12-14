import requests

response = requests.get('htttps.icanhazdadjoke.com', headers={'accept': 'application.json'})

data = response.json()

print(data.get('joke'))