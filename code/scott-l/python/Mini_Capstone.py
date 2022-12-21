'''
 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
      Project: Mini_Capstone
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
## Objective Project Design
Using python software a user will query from an FM query 
data base website and choose from the provided list an 
available FM radio channel band between 88 MHz and 108 MHz of choice. 
After the user selects a given channel the program will  
connect with a SDR hardware device and record the radio 
frequency samples then display a graphical display Power 
Spectral Density plot using Matplotlib python 2D plotting library.


## Tasks Required to complete the Project
1. Create a function to query an FM data base from a website and extract 
all the FM stations filtered based on specified user location
2. Save the FM data base query to a file for reference and additional use
3. User choose a specified frequency from the FM station list
4. Using the pyrtlsdr library connect with a general purpose low-cost 
software-define radio reciever RTL-SDR USB DVB-T dongles device
5. Create a function that will take the specified frequency selected by the 
user and display the Power Spectral Density samples collected at the specified 
chosen frequency channel using the Matplotlib python 2D plotting library 
'''

# <NOTE-TO-SELF --INSERT INSTRUCTIONS HERE FOR MINI CAPSTONE FOR DOCUMENTATION PURPOSE LEVERAGE 
# OLD FUNCTION HEADER FORMAT from matlab code>

 # required install
 # pip install matplotlib
 # pip install pyrtlsdr

# BEGIN

from rtlsdr import RtlSdr
from pylab import *
from rtlsdr import *
import requests
import json
from geopy.geocoders import Nominatim
from pprint import pprint
from geopy.distance import geodesic



# URL dictionary lookup
URL_lookup = {
    1: 'https://www.fcc.gov/media/radio/fm-query',
    2: 'https://transition.fcc.gov/fcc-bin/fmq',
    3: 'https://www.fcc.gov/media/radio/am-fm-tv-textlist-key',
    4: 'https://www.fcc.gov/reports-research/developers',
    5: 'http://www.fcc.gov/fcc-bin/fmq',
    6: 'http://www.fcc.gov/fcc-bin/fmq?searchValue=FM&format=jsonp&jsonCallback=?',
    7: 'https://transition.fcc.gov/fcc-bin/fmq?&city=45432&freq=0.0&fre2=107.9',
    8: 'https://enterpriseefiling.fcc.gov/dataentry/public/tv/lmsDatabase.html',
    9: 'https://www.fcc.gov/licensing-databases/search-fcc-databases',
    10: 'https://transition.fcc.gov/fcc-bin/fmq?state=OH&city=Dayton&freq=87.9&fre2=107.9&serv=FM&list=1&ThisTab=Results+to+This+Page%',
    11: "https://transition.fcc.gov/mb/databases/querydata/AMFMTVqueries.xxx.js",
    12: 'https://radio-world-50-000-radios-stations.p.rapidapi.com/v1/radios/searchByCountry',
    13: 'https://radiostation.pro/docs/API/',
    14: 'https://c1.radioboss.fm/api/info/92?key=A1B2C3',
    15: 'http://data.fcc.gov/api/license-view/basicSearch/getLicenses?searchValue=OH&format=jsonp&jsonCallback=?',
    16: 'http://data.fcc.gov/lpfmapi/rest/v1/lat/36/long/-119?format=json&secondchannel=true',
    17:  'https://enterpriseefiling.fcc.gov/dataentry/login.html',
    18: ' https://radio-locator.com/cgi-bin/locate?select=city&city=45432&x=0&y=0',
    19: 'https://streamfinder.com/internet-radio-api/',
    20: 'https://worldradiomap.com/us-oh/dayton',
    21: 'http://data.fcc.gov/lpfmapi/rest/v1/lat/36/long/-119?format=json&secondchannel=true',
    22:  'http://de1.api.radio-browser.info/json/states/OH/',
    23:  'https://api.radioreference.com/js/?key={key}&scid={scid}',
    24:  'http://de1.api.radio-browser.info/json/stations/bystate/OH',
    25: 'https://radio-locator.com/cgi-bin/locate?select=city&city=45432&x=0&y=0',
    26: 'http://radio.garden/api/ara/content/places/'

}

# Defined Dictionary list
# order is [FM, Frequency, City, State, Callsign, ERP]

# radio_station_info = {
#     0: ['FM',88.1,"Dayton","OH","WDPR","0.78 Kw"],
#     1: ['FM',89.5,"MHz","Dayton","OH","WQRP","6 Kw"]
# }

class RadioList:

    def __init__(self):
        self.radio_struct = {}
        self.URL_lookup = ''
        self.location_lat_long = [0,0]
        self.fm_lat_long = [0,0]

    #end def __init__

    def load_api(self,URL_lookup):
        # SET a GET request select the random quote from the URL dictionary lookup table
        # SYNTAX requests.get(url, params={key: value}, args) 
        # response = requests.get(URL_lookup)
        response = requests.get(URL_lookup,params={'format': 'json'})
        # response = requests.get(URL_lookup, headers={'accept': 'application/json'})
        response.encoding = 'utf-8' # set encoding to utf-8
        # data = response.json()
        # print(f'length of data is {len(data)}')
        # print(f'response is type {type(data)}')
        # print(data[0]['name'])
        # print(data[0]['state'])


        # data_text = response.text
        # print(response)
        # print(response.text)
        # print(response.json())
        # print(response.links)
        # print(response.apparent_encoding)
        # print(response.encoding)
        # print(response.headers)

        # load the response into data structure
        self.radio_struct = response.json()
        print(f'response is type {type(self.radio_struct)}')


        # self.radio_struct = response.text
        # self.radio_struct = json.loads(response)

        # file_contents_dict = {self.radio_struct}
        # file_contents_dict= {"radio_List" : self.radio_struct}
        # print(f'response text type {type(file_contents_dict)}')
        
        # print(self.radio_struct)  # DEBUG
        # print(f'response text type {type(self.radio_struct)}')
        

        print(len(self.radio_struct))

    #end def load_api
        
    def write_file(self):

        file_contents_dict = {} # create an empty dictionary
        # 1) write api.radio.browser.info into 'radio_station_list.json' set option 'w' for write
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

    #end def write_file ...

    def print_record(self):

        radio_list = self.radio_struct
        for j in range(len(radio_list)):
            print(f'{j}--Name: {radio_list[j]["name"]}, State: {radio_list[j]["state"]}')
            
        # end for

    #end def print_state

    def load_radio_garden_api(self,URL_lookup):
        # url = "http://radio.garden/api/ara/content/places/"
        response = requests.get(URL_lookup, headers={'accept': 'application/json'})
        response.encoding = 'utf-8'
        data = response.json()
        # print(data)
        list_of_fm = []
        # extract the values of the information from the json file and create a dictionary
        for i in data['data']['list']:
            if i['country'] == 'United States':
                # print(f"id: {i['id']},\ncity/state: {i['title']},\ncountry: {i['country']}\n")
                list_of_fm.append({
                    'id':i['id'],
                    'url':i['url'],
                    'city/state':i['title'],
                    'country':i['country'],
                    'lat':i['geo'][1],
                    'long':i['geo'][0]            
                })
        # print(list_of_fm)
        # dictionary format
        self.radio_struct = list_of_fm
        # print(type(list_of_fm))
        # print(list_of_fm)

        # json format
        # json_file = json.dumps(list_of_fm, indent=2)
        # self.radio_struct = json_file
        # print(json_file)

        return len(list_of_fm) # return number of records
        
    # end load_radio_garden_api

    def radio_garden_search(self,index):
        list_of_fm=self.radio_struct
        # print(list_of_fm)

        # DEBUG
        # print(f"index: {index}")
        # print(f"id: {list_of_fm[index]['id']}")
        # print(f"url: http://www.radio.garden{list_of_fm[index]['url']}")
        # print(f"city/state: {list_of_fm[index]['city/state']}")
        # print(f"lat: {list_of_fm[index]['lat']}")
        # print(f"long: {list_of_fm[index]['long']}")

        self.fm_lat_long[0]=list_of_fm[index]['lat']
        self.fm_lat_long[1]=list_of_fm[index]['long']

    # end def radio_garden_search
    
    def search_geocoder(self,city,state):

        city_search = city
        # print(f'city {type(city_search)}') # DEBUG
        state_search = state
        # print(f'state {type(state_search)}') # DEBUG
        app = Nominatim(user_agent="tutorial") 
        # get location raw data
        # location = app.geocode("Dayton, Ohio").raw
        location = app.geocode(f'{city_search},{state_search}').raw
        # print raw data
        # pprint(location) # DEBUG
        self.location_lat_long[0]=location["lat"]
        self.location_lat_long[1]=location["lon"]
        # print(self.location_lat_long)  # DEBUG
        # print(f'lat: {self.location_lat_long[0]}, long: {self.location_lat_long[1]}')  # DEBUG

        location1 = (self.location_lat_long[0],self.location_lat_long[1])
        location2 = (self.fm_lat_long[0],self.fm_lat_long[1])
        # Print the distance calculated in km
        # print(geodesic(location1,location2).km)
        return geodesic(location1,location2).km

    # end def search_geocoder

    def distance_geodesic(self,lat1,long1,lat2,long2):
        location1 = (lat1,long1)
        location2 = (lat2,long2)

        # Print the distance calculated in km
        # print(geodesic(location1,location2).km)  # DEBUG

    # end def distance_geodesic

    def get_fm_station(self,index):

        list_of_fm=self.radio_struct
        # print(list_of_fm)
    
        list_fm_index = []

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

        # print(f"index: {index}")
        # print(f"id: {list_of_fm[index]['id']}")
        # print(f"url: http://www.radio.garden{list_of_fm[index]['url']}")
        # print(f"city/state: {list_of_fm[index]['city/state']}")
        # print(f"lat: {list_of_fm[index]['lat']}")
        # print(f"long: {list_of_fm[index]['long']}")

        # self.fm_lat_long.append(list_of_fm[index]['lat'])
        # self.fm_lat_long.append(list_of_fm[index]['long'])

    # end def get_fm_station


#end class RadioList


# Radio Reference application key:   
# Radio Reference Template:  https://api.radioreference.com/js/?key=DOMAIN_KEY&scid=SUBCAT_ID


Radio_Obj = RadioList()

# num_records = Radio_Obj.load_api(URL_lookup[25])
num_records = Radio_Obj.load_radio_garden_api(URL_lookup[26])
print(f'Number of records: {num_records}')
Radio_Obj.write_file()
radio_station_list = []
for index in range(10):
    Radio_Obj.radio_garden_search(index)   # search the radio file by index and save the lat/long of fm station
    distance = Radio_Obj.search_geocoder('Dayton','Ohio') # search the city/state and find the distance between the index searh and city/state search input
    # print(f'distance is - {distance}')  # DEBUG
    if distance < 100:  # if radio station is less than KM radius from search location then save value
        radio_station=Radio_Obj.get_fm_station(index)
        radio_station_list.append(radio_station)
        # print("save record")  # DEBUG
        
print(radio_station_list)
# Radio_Obj.print_record()







# # convert the text into a python dictionary (json.loads)
# print(f'The data contents read is {type(data_text)}')  # DEBUG
# # print(data_text)  # DEBUG
# data_text_contents  = response.json() # turn a raw json into a python dictionary
# print(data_text_contents)
# # data_text_contents = json.loads(data_text)  # loads the file from the JSON string format into a dict format
# # print(f'The data contents after JSON load is {type(data_text_contents)}') #DEBUG



# simple way to read and print some samples from the RTL-SDR

# This code is directly lifted from the examples -need to customize the code and format into 
# given function and structure format

# sdr = RtlSdr()

# # configure device  Default Setup
# sdr.sample_rate = 2.048e6   # Hertz (Hz)
# sdr.center_freq = 97.3e6      # Hertz (Hz)
# sdr.freq_correction = 60    # Parts per Million (PPM)
# sdr.gain =35

# for index in range(len(radio_station_info)):
#     # print(f'{index}')
#     # print(type(index))
#     print(f'{index} {radio_station_info[index][0]},{radio_station_info[index][1]}, {radio_station_info[index][2]}, {radio_station_info[index][3]}, {radio_station_info[index][4]}, {radio_station_info[index][5]}')
# #end for

# tuner_select = int(input("Choose which frequency to tune the radio (select number from list): "))

# print(radio_station_info[tuner_select][1]*1e6)
# print(97.3e6)

# # configure device  
# sdr.sample_rate = 2.048e6   # Hertz (Hz)
# sdr.center_freq = radio_station_info[tuner_select][1]*1e6    # Hertz (Hz)
# sdr.freq_correction = 60    # Parts per Million (PPM)
# sdr.gain = 40

# print(f'Radio Frequency Tuned to: {radio_station_info[tuner_select][1]/1e6} MHz ')

# samples = sdr.read_samples(256*1024)
# sdr.close()

# # use matplotlib to estimate and plot the PSD

# psd(samples, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)
# xlabel('Frequency (MHz)')
# ylabel('Relative Power (dB)')

# show()


