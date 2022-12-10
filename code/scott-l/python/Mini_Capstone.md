# Mini Capstone - 
## FM Software Define Radio (SDR) Power Spectral Density (PSD) Display 

FM SDR PSD2

Install the pyrtlsdr Python wrapper and interface with a general purpose low-cost software-define radio (SDR) reciever device supported by the RTL-SDR  USB DVB-T dongles Realtek RTL2832U chipset. 

https://pypi.org/project/pyrtlsdr/

The pyrtlsdr wraps many of the functions in the librtsdr library including asynchronous read support Pythonic API. 

## Installation

pyrtlsdr can be installed using the following command

<blockquote> pip install pyrtlsdr </blockquote> 

## Objective Project Design
Using python software a user will query from an FM query data base website and choose from the provided list an available FM radio channel band between 88 MHz and 108 MHz of choice. After the user selects a given channel the program will  connect with a SDR hardware device and record the radio frequency samples then display a graphical display Power Spectral Density plot using Matplotlib python 2D plotting library. 


## FM queary data base website Links
https://www.fcc.gov/media/radio/fm-query

https://www.fcc.gov/reports-research/developers/license-view-api

https://data.fcc.gov/download/license-view/fcc-license-view-data-sample.csv

https://www.fcc.gov/licensing-databases/search-fcc-databases


## Tasks Required to complete the Project
1. Create a function to query an FM data base from a website and extract all the FM stations filtered based on specified user location
1. Save the FM data base query to a file for reference and additional use
1. User choose a specified frequency from the FM station list
1. Using the pyrtlsdr library connect with a general purpose low-cost software-define radio reciever RTL-SDR USB DVB-T dongles device
1. Create a function that will take the specified frequency selected by the user and display the Power Spectral Density samples collected at the specified chosen frequency channel using the Matplotlib python 2D plotting library 

## Optional tasks
1. Data log sample parameters collected from the SDR hardware device. 
1. Create a function that will scanning parameters and plot the frequencies across a designated range provided by the user
1. Data log the results by saving into a file and then display using data visualization library. Listed below is some of the examples

    1. Matplotlib - A Python 2D plotting library
    1. Pygal - A Python SVG Charts creator
