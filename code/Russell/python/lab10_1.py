import requests
import json

response = requests.get('https://favqs.com/api/qotd', params = {'format': 'json'})
response.encoding = 'utf-8'
# print(response)
# print(response.url)
# print(response.text)
# data = response.json
# print(data)
data = json.loads(response.text)
print(data['quote']['body'] + '\n' + '-' + data['quote']['author'])