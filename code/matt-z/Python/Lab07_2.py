import requests

search_term = input("What would you like to hear a joke about? ")

response = requests.get(f"https://icanhazdadjoke.com/search?term={search_term}", headers={'Accept': 'application/json'})

r = response.json()

for result in r['results']:
    print(result['joke'])