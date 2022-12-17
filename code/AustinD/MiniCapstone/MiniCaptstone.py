#MiniCapstone
import random
import requests 
import googlemaps 

api_key = 'AIzaSyD7NVh0Xb-3w8bS5bpH9ZLk-ZPsaulArhE'

def get_location():
  #Gets the user's current location coordinates, converting json to python dict
  current_location = requests.post(f'https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}')
  current_location = current_location.json()
  x = current_location.get('location').get('lat')
  y = current_location.get('location').get('lng')
  return x, y

def get_restaurants(x, y):
  #Gets nearby restaurants, converting json to python dict
  nearby_restaurants = requests.post(f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={x},{y}&radius=1000&keyword=restaurant&opennow&delivery&key={api_key}")
  nearby_restaurants = nearby_restaurants.json()
  return nearby_restaurants

def random_restaurant(available_restaurants):
  restaurants = available_restaurants['results']
  random_restaurant = random.choice(restaurants)
  name = random_restaurant['name']
  return name

def main():
  result = random_restaurant(get_restaurants(*get_location()))
  return result 

print(main())