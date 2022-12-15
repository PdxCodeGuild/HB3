import raylib 
import random
import requests 

def get_location():
  
  return x, y

def get_restaurants(x, y):
  #

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