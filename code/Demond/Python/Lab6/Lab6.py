#Import Request
import requests
import re

#This is where the user will input the .txt file or URL, the data is then extracted and stored within the text variable
Input_URL = input("Enter URL:")
URL = requests.get(f'{Input_URL}') # Must use ' ' after .get()
data = URL.text

#Lines 11 - 16 are used to the determine its appropriate variable name's value
number_of_characters = len(data)
data_converted_to_string_format = str(data)
words_in_data = data.split()
number_of_words_in_data = len(words_in_data) #THIS IS THE number_of_words_in_data COUNTING
sentences = re.split('[,.?!]', data_converted_to_string_format) #this sentences is trouble 2.
number_of_sentences = len(sentences)

"""""
print(number_of_characters)
print(number_of_words_in_data)
print(number_of_sentences)

"""""
# This is the equation to find out the ARI, I have concatetenated this equation
Total_score = round((4.71 * (number_of_characters/number_of_words_in_data)) + (.5 * number_of_words_in_data/number_of_sentences) - 21.43)

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

#Lines 45 - 49 are the print statements
print("------------------------------------------------------------------------------")
print('The ARI for', Input_URL, 'is', Total_score)
print('This corresponds to a', ari_scale[Total_score]['grade_level'],'level of difficulty')
print('that is suitable for an average person', ari_scale[Total_score]['ages'], 'years old.')
print("------------------------------------------------------------------------------")