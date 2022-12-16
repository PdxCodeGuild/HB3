import requests
import json

response = requests.get('https://favqs.com/api/qotd', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}) # params={'format': 'json'})

# load the response in the variable
jresponse = json.loads(response.text)


# print the author and the body
# print(jresponse['quote']['author']) 
# print(jresponse['quote']['body'])


keyword = input("enter a keyword to search for quotes: ")
page = 1

test = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={keyword}', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

secondtest = json.loads(test.text)

for i in secondtest:
    if i['body'] == 'body':
        print(i)


# list = secondtest['quotes']
# print(list["quotes"])

# data = json.loads(secondtest)

# print(data['body'])
# print(data)
# print(test.text)