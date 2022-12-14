'''
 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
      Project: Lab 10 - Quotes API -Version 1
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
Quotes API

For this lab we'll be using the Favqs Quotes API to first 
get a random quote, and then allow the user to find quotes 
by keyword. To accomplish this we'll be using the requests 
library.

Version 1: Get a Random Quote

The URL to get a random quote is https://favqs.com/api/qotd, 
send a request here, parse the JSON in the response into a 
python dictionary, and show the quote and the author.

'''
# BEGIN

import requests
import json

# URL dictionary lookup
URL_lookup = {
    1: 'https://favqs.com/api/qotd',  # Random Quote
    2: 'placeholder'
}

# SET a GET request select the random quote from the URL dictionary lookup table
response = requests.get(URL_lookup[1])
response.encoding = 'utf-8' # set encoding to utf-8
# convert the data text into a string type
data_text = response.text

# convert the text into a python dictionary (json.loads)
# print(f'The data contents read is {type(data_text)}')  # DEBUG
data_text_contents = json.loads(data_text)  # loads the file from the JSON string format into a dict format
# print(f'The data contents after JSON load is {type(data_text_contents)}') #DEBUG

print(f''' Random Quote Generator

"{data_text_contents['quote']['body']}"
          --{data_text_contents['quote']['author']}--
''')


# END


#          *                 *                  *              *
#                                                       *             *
#                         *            *                             ___
#   *               *                                          |     | |
#         *              _________##                 *        / \    | |
#                       @\\\\\\\\\##    *     |              |--o|===|-|
#   *                  @@@\\\\\\\\##\       \|/|/            |---|   |d|
#                     @@ @@\\\\\\\\\\\    \|\\|//|/     *   /     \  |w|
#              *     @@@@@@@\\\\\\\\\\\    \|\|/|/         |  U    | |b|
#                   @@@@@@@@@----------|    \\|//          |  S    |=| |
#        __         @@ @@@ @@__________|     \|/           |  A    | | |
#   ____|_@|_       @@@@@@@@@__________|     \|/           |_______| |_|
# =|__ _____ |=     @@@@ .@@@__________|      |             |@| |@|  | |
# ____0_____0__\|/__@@@@__@@@__________|_\|/__|___\|/__\|/___________|_|_


