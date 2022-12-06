'''
 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
      Project: Lab 6 - Automated Readability Index
      Author: Scott Lefgren
      Email: scojlefg@gmail.com
      Date: December 1, 2022
___________________          _-_
\==============_=_/ ____.---'---`---.____
            \_ \    \----._________.----/
              \ \   /  /    `-_-'
          __,--`.`-'..'-_
         /____          ||
              `--.____,-'

 *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
'''
"""
Let's compute the ARI for a given book. The automated readability 
index (ARI) is a formula for computing the U.S. grade level for a 
given block of text
The general formula to compute the ARI is as follows:

4.71*(characters/words)+0.5*(words/sentences)-21.43

The score is computed by multiplying the number of characters divided 
by the number of words by 4.71, adding the number of words divided by 
the number of sentences multiplied by 0.5, and subtracting 21.43. 
If the result is a decimal, always round up, and if the result is 
higher than 14, it should be set to 14.

Scores correspond to the following ages and grad levels:

    Score  Ages     Grade Level
     1       5-6    Kindergarten
     2       6-7    First Grade
     3       7-8    Second Grade
     4       8-9    Third Grade
     5      9-10    Fourth Grade
     6     10-11    Fifth Grade
     7     11-12    Sixth Grade
     8     12-13    Seventh Grade
     9     13-14    Eighth Grade
    10     14-15    Ninth Grade
    11     15-16    Tenth Grade
    12     16-17    Eleventh grade
    13     17-18    Twelfth grade
    14     18-22    College

Once you’ve computed the ARI score, you can use the following dictionary to look up the age range and grade level.

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

The output should look something like the following:

--------------------------------------------------------
The ARI for gettysburg-address.txt is 12
This corresponds to a 11th Grade level of difficulty
that is suitable for an average person 16-17 years old.
--------------------------------------------------------


"""

# BEGIN

import requests
import json

# ARI dictionary
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

# Book URL dictionary lookup
book_lib = {
    1: 'https://www.gutenberg.org/cache/epub/69452/pg69452.txt',  # Shells and pebbles, by Anonymous
    2: 'https://www.gutenberg.org/files/74/74-0.txt',   # Tom Sawyer, by Mark Twain
    3: 'https://www.gutenberg.org/files/35/35-0.txt'  # The Time Machine, by H.G. Wells
}

book1_url = 'https://www.gutenberg.org/cache/epub/69452/pg69452.txt'  # Shells and pebbles, by Anonymous
book2_url = 'https://www.gutenberg.org/files/74/74-0.txt'   # Tom Sawyer, by Mark Twain
book3_url = 'https://www.gutenberg.org/files/35/35-0.txt'  # The Time Machine, by H.G. Wells

# Send a GET request
response = requests.get(book_lib[1])
# convert the data text into a string type
data_text = response.text

print(f'length of string {len(data_text)}')  # DEBUG

# will need to remove the header and ending disclaimer at each end of the book text

# Beginning '*** START OF THE PROJECT GUTENBERG
data_begin_index = data_text.find('*** START OF THE PROJECT GUTENBERG')
print(f'Beginning string index is: {data_begin_index}')

# Ending '*** END OF THE PROJECT GUTENBERG'
data_end_index = data_text.find('*** END OF THE PROJECT GUTENBERG')
print(f'Ending string index is: {data_end_index}')
# remove the Beginning and ending disclaimer statements
data_text_slice = data_text[data_begin_index:data_end_index]

# calculate the number of characters in the book this will require ignoring white space
data_text_characters = data_text_slice.replace(' ','')
data_text_characters = data_text_slice.replace('\n','')
print(data_text_characters)



# split a string into a list, this will split on whitespace
data_text_list = data_text_slice.split()

print(f'List words without whitespace: {len(data_text_list)}')  # DEBUG


# # Append the following data in a file
# with open('text_book_001.txt', 'a') as text_book_file:
#     text_book_file.write(response.url)
#    # text_book_file.write(response.text)
#   #  text_book_file.write(response.status_code)
#     text_book_file.write(response.encoding)
#    #text_book_file.write(response.headers)
  
# print(response.url)
# print(response.text) 
# print(response.status_code) 
# print(response.encoding) 
# print(response.headers) 

# Algorithm outline

# calculate the number of characters in the book this will require ignoring white space
# print(len(response.text))



# calculate the number of words in the book this will require finding each word and counting

# calculate the number of sentences this will require finding the period of each sentence

# After finding all this information perform formula calculation 

# round up the result

# find the result from the dictionary look up table and print result




