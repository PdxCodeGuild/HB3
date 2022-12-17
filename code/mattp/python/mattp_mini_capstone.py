print(f"MINI CAPSTONE LAB: Fish to Dish")

# somehow i need to run portions of this API code on this file.

# i dont know if this is going to need to be visual at all, or how to do that

# do i need to create an interface with this, or am i allowed to run my capstone through the terminal.

### you are going to use request with different headers.

### it is like the dad joke API but using the FishWatch API

import bs4
import string
import re
import requests

'''variable_location = input('Input your zipcode or a zipcode you would like to know the fish of: ')

###input the fishmap.org api if you can, if not make due with fishwatch location option
'''


############ FishWatch Nutrition Finder: Working ############
'''
variable_fish = input('Input a fish from your location list to learn about its sustainability: ')

response = requests.get(f'https://www.fishwatch.gov/api/species/{variable_fish}', headers = {'accept': 'application/json'})



data = response.json()

for fish in data:
    fishname = fish['Species Name']
    fishlocation = fish['Location']
    fishcalories = fish['Calories']
    
    fishlocation = fishlocation.replace('</li>', '')
    fishlocation = fishlocation.replace('<li>', '')
    fishlocation = fishlocation.replace('<ul>', '')
    fishlocation = fishlocation.replace('</ul>', '')
    print(f"""Your fish, {fishname}, is located: {fishlocation}\n and it is {fishcalories} calories per serving.""")
    
'''
############ Wikipedia Fish Abstract Portion: Working ###########
'''
wiki_subject = input('Enter a fish to learn more about it: ')
url = 'https://en.wikipedia.org/w/api.php'
params = {
        'action': 'query',
        'format': 'json',
        'titles': wiki_subject,
        'prop': 'extracts',
        'exintro': True,
        'explaintext': True,
    }
 
response = requests.get(url, params=params)
data = response.json()
 
page = next(iter(data['query']['pages'].values()))

overview = page['extract'][:5000]
print(f"""Here is an overview of the {wiki_subject}:
      {overview}""")
   
'''    
    
