import requests

keyword = input("What word would you like to search for? ")

response = requests.get(f'https://favqs.com/api/quotes?page=<page>&filter=<{keyword}>/' , headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

data = response.json()

print(data)