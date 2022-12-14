'''
This program queries the user for a topic for a photo and fetches a random photo
from pexels.com and also downloads the photo saving it as the description from the URL.
'''

from pexels_api import API
import requests
import shutil
import random

search_term = input("What would you like to find photos of? ")
PEXELS_API_KEY = '563492ad6f91700001000001ea041ef42b514471bd2c2be13d23d465'

api = API(PEXELS_API_KEY)

page = random.randint(1,10)

api.search(search_term, page=page, results_per_page=1)

photos = api.get_entries()
for photo in photos:
  print('Photographer: ', photo.photographer)
  print('Photo url: ', photo.url)
  print('Photo original size: ', photo.original)
  
filename = photo.url.split("/")[-2]+'.jpg'
  
r = requests.get(photo.original, stream = True)
  
if r.status_code == 200:
    r.raw.decode_content = True
      
    with open(filename,'wb') as f:
        shutil.copyfileobj(r.raw, f)
    print("Image successfully downloaded: ", filename)
    
else:
    print("Image couldn't be retrieved")