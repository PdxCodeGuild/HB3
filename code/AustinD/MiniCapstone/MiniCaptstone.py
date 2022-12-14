import raylib 
import random
import requests 
import googlemaps 

def get_location():
  api_key = 'Insert'
  # Get the user's current location
  current_location = requests.post(f'https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}')
  current_location = current_location.json()
  x = current_location.get('location').get('lat')
  y = current_location.get('location').get('lng')
  return x, y

def get_restaurants(x, y):
  #Use the latitude and longitude to get a list of nearby restaurants
  #nearby_restaurants = googlemaps.
  #location=(x, y)
  #radius=500
  #type='restaurant'

  # Create a dictionary to store information about each restaurant
  restaurants = {restaurant['name']: {
    'website': restaurant['website'],
    'phone': restaurant['phone'],
    'delivers': restaurant['delivers'],
    'menu': restaurant['menu']
  } for restaurant in ['results']}

  # Return the dictionary of restaurants
  return restaurants

#GUI function
def GUI(x, y, restaurants):
  #Initialize the window
  raylib.InitWindow(x, y, "Click GUI")

  #Set the background color
  raylib.SetBackgroundColor(raylib.WHITE)

  #Run the GUI until the user closes it
  while not raylib.WindowShouldClose():
    #Check if the user clicks the mouse button
    if raylib.IsMouseButtonPressed(raylib.MOUSE_LEFT_BUTTON):
      # Choose a random restaurant from the dictionary
      random_restaurant = random.choice(list(restaurants.keys()))

      #Print the name of the restaurant
      print(random_restaurant)

    #Update the screen
    raylib.UpdateScreen()

  #Close the window
  raylib.CloseWindow()

# Call the createClickGui function
GUI(500, 500, get_nearby_restaurants((get_current_location())))