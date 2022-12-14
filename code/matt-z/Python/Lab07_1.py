import requests

response = requests.get("https://icanhazdadjoke.com", headers={'Accept': 'application/json'})

r = response.json()

print(r.get("joke"))