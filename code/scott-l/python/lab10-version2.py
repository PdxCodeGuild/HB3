'''
 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
      Project: Lab 10 - List Quotes by keywords -Version 2
      Author: Scott Lefgren
      Email: scojlefg@gmail.com
      Date: December 13, 2022
___________________          _-_
\==============_=_/ ____.---'---`---.____
            \_ \    \----._________.----/
              \ \   /  /    `-_-'
          __,--`.`-'..'-_
         /____          ||
              `--.____,-'

 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
'''
'''
The Favqs Quote API also supports getting a list of quotes 
associated with a given keyword https://favqs.com/api/quotes?page=<page>&filter=<keyword>. 
Prompt the user for a keyword, list the quotes you get in response, 
and prompt the user to either show the next page or enter a new keyword. 
You can use string concatenation to build the URL.

> enter a keyword to search for quotes: nature
25 quotes associated with nature - page 1
<list of quotes>
> enter 'next page' or 'done': next page
25 quotes associated with nature - page 2
<list of quotes>
> enter 'next page' or 'done': done
> enter a keyword to search for quotes:

This API endpoint requires an API key be included in a 
request header. You can find documentation of specifying 
request headers here and documentation on authorization with 
the Favqs API here under "Authorization".
'''

# BEGIN

import requests
import json


while True:
    # Obtain the keyword from the user
    keyword_input = input('enter a keyword to search for quotes: ')
    page = str(1)
    URL_lookup = 'https://favqs.com/api/quotes?page='+ page +'&filter=' + keyword_input
    print(f'URL Lookup string is')  # DEBUG
    print(URL_lookup)  # DEBUG

    # SET a GET request select the random quote from the URL dictionary lookup table
    response = requests.get(URL_lookup,headers={'Authorization': 'Token token=b66f8dffde403c426aac8259a7476206'})
    response.encoding = 'utf-8' # set encoding to utf-8
    # convert the data text into a string type
    data_text = response.text

    # convert the text into a python dictionary (json.loads)
    # print(f'The data contents read is {type(data_text)}')  # DEBUG
    data_text_contents = json.loads(data_text)  # loads the file from the JSON string format into a dict format
    print(f'The data contents after JSON load is {type(data_text_contents)}') #DEBUG

    # Get the list of quotes out of the dictionary  
    quote_list = data_text_contents['quotes']

    # NUMBER quotes associated with nature - page X
    print(f'{len(data_text_contents["quotes"])} quotes associated with {keyword_input} - page {page}')
    # <list of quotes>
    print(f'Quotes BEGIN----page {page}')
    # print(quote_list)  # DEBUG

    for quote_index in range(len(quote_list)):
        print(f'{quote_index+1}: "{quote_list[quote_index]["body"]}" Author:-- {quote_list[quote_index]["author"]}-- ')
    # end for

    input_command = input("Enter 'next page' or 'done': ")
    if input_command == 'next page':
    # repeat process above
    elif input_command == 'done'
    # finish code

