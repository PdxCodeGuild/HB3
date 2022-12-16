print('Lab 10: Quotes Lab Version 1')

import requests
import json
 
response = requests.get('https://favqs.com/api/qotd')
response.encoding = 'utf-8'
quoter = json.loads(response.text)
 
print(quoter['quote']['author'])
print(quoter['quote']['body'])
