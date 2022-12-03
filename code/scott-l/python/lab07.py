'''
 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
      Project: Lab 7 - Dad Joke API
      Author: Scott Lefgren
      Email: scojlefg@gmail.com
      Date: December 2, 2022
___________________          _-_
\==============_=_/ ____.---'---`---.____
            \_ \    \----._________.----/
              \ \   /  /    `-_-'
          __,--`.`-'..'-_
         /____          ||
              `--.____,-'

 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
'''

# Use the Dad Joke API to get a dad joke and display it to the user. 
# You may want to also use time.sleep to add suspense.

# Part 1
# Use the requests library to send an HTTP request to https://icanhazdadjoke.com/ with 
# the accept header as application/json. This will return a dad joke in JSON format. 
# You can then use the .json() method on the response to get a dictionary. Get the 
# joke out of the dictionary and show it to the user

# BEGIN

import requests
import json

# # request headers to specify an API key 
response = requests.get('https://icanhazdadjoke.com/', headers={'accept':'application/json'})

# # # request headers to specify an API key 
# response = requests.get('https://icanhazdadjoke.com/')

# print(response.headers)

# Send a GET request
# response = requests.get('https://icanhazdadjoke.com/', params={'format': 'json'})

# print(response.text)  # raw json response
# print(response.url)
# print(response.status_code)
# response.encoding = 'utf-8'  # set encoding to utf-8
# print(response.encoding)
# print(response.headers)

# use the .json() method on the response to get a dictionary
data = response.json()   # turn json into a python dictionary
print(data)
# print(data.get('status'))


# # Get the joke out of the dictionary and show it to the user
print(data.get('joke'))


# data1 = json.loads(response.text)
# print(data1)
