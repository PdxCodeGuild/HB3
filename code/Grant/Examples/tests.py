import requests

import json



url = "http://radio.garden/api/ara/content/places/"

headers = {}

response = requests.get(url, headers={'accept': 'application/json'})

response.encoding = 'utf-8'

data = response.json()

list_of_fm = []

for i in data['data']['list']:

    if i['country'] == 'United States':

        print(f"id: {i['id']},\ncity/state: {i['title']},\ncountry: {i['country']}\n")
               
        list_of_fm.append({

            'id':i['id'],
            'city/state':i['title'],
            'country':i['country'],
            'lat':i['geo'][1],
            'long':i['geo'][0]            
        })

# print(list_of_fm)

json_file = json.dumps(list_of_fm, indent=2)

print(json_file)

with open('json_file.json', 'w') as file:

    json.dump(list_of_fm, file)





