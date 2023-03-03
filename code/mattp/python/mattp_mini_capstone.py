print(f"\n\tMINI CAPSTONE LAB: Fish to Dish\n")

# somehow i need to run portions of this API code on this file.

# i dont know if this is going to need to be visual at all, or how to do that

# do i need to create an interface with this, or am i allowed to run my capstone through the terminal.

### you are going to use request with different headers.

### it is like the dad joke API but using the FishWatch API


import string
import re
import requests
import wikipedia

'''variable_location = input('Input your zipcode or a zipcode you would like to know the fish of: ')

###input the fishmap.org api if you can, if not make due with fishwatch location option
'''

############ FishMap API Location ###########################



############ FishWatch Nutrition Finder: Working ############

variable_fish = input('Input a fish from your location list to learn about its sustainability: ')

response = requests.get(f'https://www.fishwatch.gov/api/species/{variable_fish}', headers = {'accept': 'application/json'})



data = response.json()

for fish in data:
    fishname = fish['Species Name']
    fishlocation = fish['Location']
    fishhabitat = fish['Habitat']
    fishphoto = fish['Species Illustration Photo']
    
    fishcalories = fish['Calories']
    fishcarbohydrates = fish['Carbohydrate']
    fishcholesterol = fish['Cholesterol']
    fishfat = fish['Fat, Total']
    fishfiber = fish['Fiber, Total Dietary']
    fishprotein = fish['Protein']
    fishSfat = fish['Saturated Fatty Acids, Total']
    fishsodium = fish['Sodium']
    fishtaste = fish['Taste']
    fishtexture = fish['Texture']
    fishhealth = fish['Health Benefits']
    
    fishfarming = fish['Farming Methods']
    fishenvironment = fish['Environmental Effects']
    fishrate = fish['Fishing Rate']
    
    fishlocation = fishlocation.replace('</li>', '')
    fishlocation = fishlocation.replace('<li>', '')
    fishlocation = fishlocation.replace('<ul>', '')
    fishlocation = fishlocation.replace('</ul>', '')
    fishlocation = fishlocation.replace('&nbsp;', '')
    fishhabitat = fishhabitat.replace('</li>', '')
    fishhabitat = fishhabitat.replace('<li>', '')
    fishhabitat = fishhabitat.replace('<ul>', '')
    fishhabitat = fishhabitat.replace('</ul>', '')
    fishhabitat = fishhabitat.replace('&nbsp;', '')
    fishtaste = fishtaste.replace('</p>', '')
    fishtaste = fishtaste.replace('<p>', '')
    fishtaste = fishtaste.replace('&nbsp;', '')
    fishtexture = fishtexture.replace('<p>', '')
    fishtexture = fishtexture.replace('</p>', '')
    fishtexture = fishtexture.replace('&nbsp;', '')
    
    print(f"""\nThe {fishname} is located: 
        {fishlocation}\n""")
    print(f"""\nTheir habitat is described as:
        {fishhabitat}\n""")
    print(f"""Some nutritional information:\n
    The {fishname} has:       {fishcalories} calories per serving.
                                {fishcarbohydrates} carbohydrates per serving.
                                {fishprotein} of protein per serving.
                                {fishfat} of fat per serving.
                                {fishSfat} of saturated fat per serving.
                                {fishcholesterol} units of cholesterol per serving.
                                {fishsodium} of sodium per serving.
                                {fishfiber} of dietary fiber per serving.
                              \n""")
    ######## Fish taste info ########
    print(f"""\nSome food info about {fishname}:\n
          Taste: {fishtaste}
          Texture: {fishtexture}""")
    ####### Fish sustainability info
    print(f"""\nSome farming/sustainability info about {fishname}:\n
          Farming Method: {fishfarming}\n
          Fishing Rate: {fishrate}\n
          Fishing Environmental Impact: {fishenvironment}""")

############ Wikipedia Fish Abstract Portion: Working ###########

#wiki_subject = input('Enter a fish to learn more about it: ')
url = 'https://en.wikipedia.org/w/api.php'
params = {
        'action': 'query',
        'format': 'json',
        'titles': variable_fish,
        'prop': 'extracts',
        'exintro': True,
        'explaintext': True,
    }
 
response = requests.get(url, params=params)
data = response.json()
 
page = next(iter(data['query']['pages'].values()))

overview = page['extract'][:5000]
print(f"""\n\nHere is an overview of the {variable_fish}: 
        
        {overview}""")
   
   
    
