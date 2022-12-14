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


# BEGIN

from rtlsdr import RtlSdr
