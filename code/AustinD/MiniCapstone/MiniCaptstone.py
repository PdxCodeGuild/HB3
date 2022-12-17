#MiniCapstone
import random
import requests 
import googlemaps 

api_key = input('Insert API key')

def get_location():
  #Gets the user's current location coordinates by calling geolocate API and converting json to python dict
  current_location = requests.post(f'https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}')
  current_location = current_location.json()
  x = current_location.get('location').get('lat')
  y = current_location.get('location').get('lng')
  return x, y

def get_restaurants(x, y):
  #Gets nearby restaurants(Roughly 10 miles, radius # is in meters) using Nearby Search API and converts json to python dict
  nearby_restaurants = requests.post(f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={x},{y}&radius=16000&keyword=restaurant&opennow&delivery&key={api_key}")
  available_restaurants = nearby_restaurants.json()
  return available_restaurants 
  #Gets random restaurant, gets name and place_id, uses place_id from Nearby Search API to call Place Details API for contact information after converting json to python
def random_restaurant(available_restaurants):
  restaurants = available_restaurants['results']
  random_restaurant = random.choice(restaurants)
  name = random_restaurant['name']
  place_id = random_restaurant['place_id']
  place = requests.post(f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name%2Crating%2Cformatted_phone_number&key={api_key}")
  restaurant = place.json()
  phone = restaurant['result']['formatted_phone_number']
  return f"{name}\n{phone}"

def main():
  result = random_restaurant(get_restaurants(*get_location()))
  return result

print(main())
exit()