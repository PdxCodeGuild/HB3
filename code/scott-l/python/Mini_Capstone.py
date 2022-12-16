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
    19: 'https://streamfinder.com/internet-radio-api/'

}

# SET a GET request select the random quote from the URL dictionary lookup table
# SYNTAX requests.get(url, params={key: value}, args) 
# response = requests.get(URL_lookup[18])
response = requests.get(URL_lookup[18],params={'format': 'json'})
response.encoding = 'utf-8' # set encoding to utf-8
# convert the data text into a string type
# data_text = response.text
print(response)
# print(response.text)
# print(response.json())
# print(response.links)
# print(response.apparent_encoding)
# print(response.encoding)
# print(response.headers)

# # convert the text into a python dictionary (json.loads)
# print(f'The data contents read is {type(data_text)}')  # DEBUG
# # print(data_text)  # DEBUG
# data_text_contents  = response.json() # turn a raw json into a python dictionary
# print(data_text_contents)
# # data_text_contents = json.loads(data_text)  # loads the file from the JSON string format into a dict format
# # print(f'The data contents after JSON load is {type(data_text_contents)}') #DEBUG

'''

# simple way to read and print some samples from the RTL-SDR

# This code is directly lifted from the examples -need to customize the code and format into 
# given function and structure format

sdr = RtlSdr()

# configure device
sdr.sample_rate = 2.048e6   # Hertz (Hz)
sdr.center_freq = 97.3e6      # Hertz (Hz)
sdr.freq_correction = 60    # Parts per Million (PPM)
sdr.gain =35

samples = sdr.read_samples(256*1024)
sdr.close()

# use matplotlib to estimate and plot the PSD

psd(samples, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)
xlabel('Frequency (MHz)')
ylabel('Relative Power (dB)')

show()


'''