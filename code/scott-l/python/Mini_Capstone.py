'''
 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
      Project: Mini_Capstone - Radio Station Search
      Author: Scott Lefgren
      Email: scojlefg@gmail.com
      Date: December 20, 2022
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
## Objective Project Design

Provide to the user a list of available online United States radio station streaming URLs that are 
located radius distance (km) from a specified city, state location.  The user will then be able to choose a 
a streaming radio station for listening.  The program will accomplish this by requesting streaming 
radio station information from radio garden website in a JSON format.  Using the python geopy library 
the program will calculate the geo distance between the lat/long streaming radio station 
location data and the lat/long of the specified city, state location.  
Only the radio station URLs that are within the given radius radius distance from the specified city, state location
will be provided and displayed to the user for selection.  The user will be able to select a URL and the 
radio garden website opening a web browser providing the user to listen streaming music. '''


import requests
import json
from geopy.geocoders import Nominatim
from pprint import pprint
from geopy.distance import geodesic


# define class radioList
class RadioList:

    def __init__(self):
        self.radio_struct = {}
        self.URL_lookup = ''
        self.location_lat_long = [0,0]
        self.fm_lat_long = [0,0]
    #end def __init__
        
    def write_file(self):
        file_contents_dict = {} # create an empty dictionary
        # 1) open file called 'radio_station_list.json' set option 'w' for write
        with open('radio_station_list.json', 'w') as radio_station_file:    
        # 2) put self.radio_struct in a dictionary with the key 'radio_list'
            file_contents_dict= {"radio_List" : self.radio_struct}
            # print(self.radio_struct)  # DEBUG
        # 3) convert the dictionary to a json string (json.dumps)
            radio_station_file_json = json.dumps(file_contents_dict)
            # print(radio_station_file_json)  # DEBUG
        # 4) write the json string to the file
            radio_station_file.write(radio_station_file_json)
            # radio_station_file.write(file_contents_dict)
    #end def RadioList.write_file 

    # RadioList.load_radio_garden_api performs the function to request from the 
    # radio garden API and then parses the data into a list of dictionaries
    # INPUT: URL <type str>
    # OUTPUT: list of fm stations <type list>  (list of dictionaries for fm stations in the United States)
    def load_radio_garden_api(self,URL_lookup):
        # url = "http://radio.garden/api/ara/content/places/"
        response = requests.get(URL_lookup, headers={'accept': 'application/json'})
        response.encoding = 'utf-8'
        data = response.json()
        # print(data) # DEBUG
        list_of_fm = []
        # extract the values of the information from the json file and create a dictionary
        for j in data['data']['list']:
            if j['country'] == 'United States':  # Filter results by country of United States
                # print(f"id: {i['id']},\ncity/state: {i['title']},\ncountry: {i['country']}\n")  # DEBUG
                list_of_fm.append({
                    'id':j['id'],
                    'url':j['url'],
                    'city/state':j['title'],
                    'country':j['country'],
                    'lat':j['geo'][1],
                    'long':j['geo'][0]            
                })
        # print(list_of_fm)  # DEBUG
        # save results into a list of dictionary format
        self.radio_struct = list_of_fm
        # print(type(list_of_fm)) # DEBUG
        # print(list_of_fm)  # DEBUG
        return list_of_fm # return the list of dictionaries
        
    # end RadioList.load_radio_garden_api

    # RadioList.search_geocoder provides the lat/long coordinates of a given city state 
    # INPUTS: city <type str>, state <type str>
    # OUTPUTS: location_lat_long <type list> [lat,lon]
    def search_geocoder(self,city,state):
        city_search = city
        # print(f'city {type(city_search)}') # DEBUG
        state_search = state
        # print(f'state {type(state_search)}') # DEBUG
        app = Nominatim(user_agent="tutorial") 
        # get location raw data
        location = app.geocode(f'{city_search},{state_search}').raw
        # print raw data
        # pprint(location) # DEBUG
        self.location_lat_long[0]=location["lat"]
        self.location_lat_long[1]=location["lon"]
        # print(self.location_lat_long)  # DEBUG
        # print(f'lat: {self.location_lat_long[0]}, long: {self.location_lat_long[1]}')  # DEBUG
        return self.location_lat_long
    # end def RadioList.search_geocoder

    # RadioList.get_fm_station takes the given index value of the fm station list and returns station
    # streaming URL and other component data characteristics
    # INPUT: Index value of the list <type int>
    # OUTPUT: Formated FM station list (single item) with URL <type list>  list of single dictionary
    def get_fm_station(self,index):
        list_of_fm=self.radio_struct  # assign the radio_struct to the list value
        # print(list_of_fm)  # DEBUG    
        list_fm_index = []  # instantiate a list 
        list_fm_index.append({
                    'id':list_of_fm[index]['id'],
                    'url':f"http://www.radio.garden{list_of_fm[index]['url']}",
                    'city/state':list_of_fm[index]['city/state'],
                    'country':list_of_fm[index]['country'],
                    'lat':list_of_fm[index]['lat'],
                    'long':list_of_fm[index]['long']            
                })
        # print(list_fm_index)  # DEBUG
        return list_fm_index[0]
    # end def RadioList.get_fm_station

#end class RadioList

##########################################BEGIN##########################################


# URL dictionary lookup
URL_lookup = {
    0: 'http://radio.garden/api/ara/content/places/'
}

# instantiate RadioList Object
Radio_Obj = RadioList()
# Load the radio garden API and save the list of FM stations
list_of_fm = Radio_Obj.load_radio_garden_api(URL_lookup[0])
print(f'Total Number of FM Stations in list: {len(list_of_fm)}')
# print(list_of_fm) # DEBUG
# Write the API results to a file to save for later ..<This program does not extract the info from the file, this is work TBD in future
Radio_Obj.write_file()
radio_station_list = []  # instantiate a list 
fm_lat_long = [0,0] # instantiate a list for fm station lat/long values
location_lat_long = [0,0] # instantiate a list for user specified city and state lat/long values
city_input = input("Type the name of City: ")
state_input = input("Type the name of the State (two letters only): ")
range_distance = int(input("Provide the search radius distance from location (km): ")) # specify type-int result
# Find the city/state lat/long coordinates
print(f'''Input Parameters -------------
          City: {city_input}
          State: {state_input}
          Search Radius Distance: {range_distance}
          ------------------------------------
------CTRL+SELECT URL to Open Web browser and listen to online music stream----------''')
# Find the lat/long of the city/state input by user
location_lat_long = Radio_Obj.search_geocoder(city_input,state_input) 
# Compare each FM station in the list to the given lat/long of the user input city/state location
# determine if the radio station URL is within the given search radius
# only save the radis station records that meet the search radius parameters
for index in range(len(list_of_fm)):
    fm_lat_long[0]=list_of_fm[index]['lat']  # extract the lat from the list of fm stations
    fm_lat_long[1]=list_of_fm[index]['long']  # extract the long from the list of fm stations
    # Print the distance calculated in km
    # print(geodesic(location1,location2).km)  # DEBUG
    # calculate the distance between two locations with a given lat/long input
    distance = geodesic(fm_lat_long,location_lat_long).km
    # print(f'distance is - {distance}')  # DEBUG
    if distance < range_distance:  # if radio station is less than km radius from search location then save value in the list
        radio_station=Radio_Obj.get_fm_station(index)  # obtain the radio station record list at a given index value
        radio_station_list.append(radio_station) # save the dictionary record to the radio station list
        # print("save record")  # DEBUG
    # end if
        
# print(radio_station_list)  # DEBUG
print('-------------------------------------------------------------------------')
print(f'Found {len(radio_station_list)} stations within {range_distance} km of {city_input}, {state_input}')
print('-------------------------------------------------------------------------')
# print the URL radio stations within the search radius location
for j in range(len(radio_station_list)):
    print(radio_station_list[j]['url'])


########################END######################################

#  __________________/  /                       __________________/  /
# | _    _______    /  /                       | _    _______    /  /
# |(_) .d########b. //)| _____________________ |(_) .d########b. //)|
# |  .d############//  ||        _____        ||  .d############//  |
# | .d######""####//b. ||() ||  [RADIO]  || ()|| .d######""####//b. |
# | 9######(  )#_//##P ||()|__|  | = |  |__|()|| 9######(  )#_//##P |
# | 'b######++#/_/##d' ||() ||   | = |   || ()|| 'b######++#/_/##d' |
# |  "9############P"  ||   ||   |___|   ||   ||  "9############P"  |
# |  _"9a#######aP"    ||  _   _____..__   _  ||  _"9a#######aP"    |
# | |_|  `""""''       || (_) |_____||__| (_) || |_|  `""""''       |
# |  ___..___________  ||_____________________||  ___..___________  |
# | |___||___________| |                       | |___||___________| |
# |____________________|        BOOMBOX        |____________________|