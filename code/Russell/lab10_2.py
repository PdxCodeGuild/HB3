import requests
import json

while True:
    filter = input("Enter keyword to search for relevant quotes or 'q' to quit ").lower()
    if filter == 'q':
        break
    else:
        response = requests.get(f'https://favqs.com/api/qotd?filter={filter}', params = {'format': 'json'}, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
        response.encoding = 'utf-8'
        # print(response)
        # print(response.url)
        # print(response.text)
        # data = response.json
        # print(data)
        data = json.loads(response.text)
        print(data['quote']['body'] + '\n' + '-' + data['quote']['author'])