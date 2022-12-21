import requests
import json

page = 1
filter = input("Enter keyword to search for relevant quotes or 'q' to quit ").lower()
response = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={filter}', params = {'format': 'json'}, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
data = json.loads(response.text)

while data:
    
    quote_num = 0
    data = json.loads(response.text)
    for d in data['quotes']:
        quote_num += 1
        print(f"{quote_num} - {d['body']} \n - {d['author']}")
    userin = input('next page or q to quit ')

    if userin == 'next page':
        page += 1
        quote_num = 0
        response = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={filter}', params = {'format': 'json'}, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
        data = json.loads(response.text)
        for d in data['quotes']:
            quote_num += 1
            print(f"{quote_num} - {d['body']} \n - {d['author']}")
        # userin = input('next page or q to quit ')
    elif userin == 'q':
        break