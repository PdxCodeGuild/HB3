import requests
import json
response = requests.get('https://favqs.com/api/quotes?page=<page>&filter=<keyword>') # params={'format': 'json'})
# jresponse = response.json()
jresponse = json.loads(response.text)
# print(jresponse['author'])
print(jresponse['quote']['author'])
print(jresponse['quote']['body'])
# step3 = json.loads(str(response))