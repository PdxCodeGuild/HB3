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

# print(response.headers)  #DEBUG

# print(response.text)  # raw json response  # DEBUG
# print(response.url)    # DEBUG
# print(response.status_code) # DEBUG
# response.encoding = 'utf-8'  # set encoding to utf-8  #DEBUG
# print(response.encoding)  # DEBUG
# print(response.headers)     # DEBUG

# use the .json() method on the response to get a dictionary
data = response.json()   

# print(data)  # DEBUG
# print(data.get('id'))  # DEBUG API
# print(data.get('status'))  # DEBUG API

# Get the joke out of the dictionary and show it to the user
print(data.get('joke'))

# END


#        !
#        !
#        ^
#       / \
#      /___\
#     |=   =|
#     |     |
#     |     |
#     |     |
#     |     |
#     |     |
#     |     |
#     |     |
#     |     |
#     |     |
#    /|##!##|\
#   / |##!##| \
#  /  |##!##|  \
# |  / ^ | ^ \  |
# | /  ( | )  \ |
# |/   ( | )   \|
#     ((   ))
#    ((  :  ))
#    ((  :  ))
#     ((   ))
#      (( ))
#       ( )
#        .
#        .
#        .