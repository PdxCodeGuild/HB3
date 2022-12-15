import random
import requests
import raylib

def main():
  #Set your Foursquare API credentials
  client_id = 'Insert'
  client_secret = 'Insert'

  #Set the parameters for the API requests
  parameters = {
      'client_id': client_id,
      'client_secret': client_secret,
      'v': '20221215',  
  }

  #Sets the Foursquare API endpoint for getting a user's location
  location_endpoint = 'https://api.foursquare.com/v2/users/self/locations'

  #Sets the Foursquare API endpoint for getting nearby venues
  venue_endpoint = 'https://api.foursquare.com/v2/venues/explore'

def get_location():
  with requests.get(location_endpoint, params=parameters) as response:
    location = response.json().get('response', {}).get('locations', [{}])[0]
    lat, lng  = location.get('lat'), location.get('lng')
    return lat, lng

def get_nearby_restaurants(lat, lng):
  #Sets the parameters for the API request
  parameters = parameters
  parameters['ll'] = f"{lat},{lng}"
  parameters['section'] = 'food'  #Sets a filter for the type/category it's searching for 

  # Make the API request to get nearby venues
  with requests.get(venue_endpoint, params=parameters) as response:
    #Searches request response to get the names of the nearby restaurants
    restaurants = [venue['name'] for venue in response.json()['response']['groups'][0]['items']]

    return restaurants

  lat, lng = get_location()

  # Get the names of nearby restaurants
  restaurants = get_nearby_restaurants(lat, lng)

  # Return the names of the nearby restaurants
  return restaurants

print(main())