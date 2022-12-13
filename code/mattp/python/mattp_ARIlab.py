print('\n\tARI Lab 06')

import requests
import math
import re
import string

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

response = requests.get('https://www.gutenberg.org/files/62897/62897-0.txt')
book = response.text


def character_count(book):
    characters = 0
    for letter in book:
        if letter == ' ':
            pass
        else:
            characters += 1
    return characters
print(f'\n\tCharacters in book: {character_count(book)}')

def word_count(book):
    words = 0
    for letter in book:
        if letter == ' ':
            words += 1
    return words
print(f'\n\tWords in book: {word_count(book)}')

def sentence_count(book):    
    sentence = 0
    for letter in book:
        if letter == '.' or letter == '!' or letter == '?':
            sentence += 1
    return sentence
print(f'\n\tSentences in book: {sentence_count(book)}')

####### ARI Problem #######

ari_solution = int((4.71 * (character_count(book)/word_count(book))) + (.5 * (word_count(book)/sentence_count(book))) - 21.43)
for ari_solution in range(ari_solution):
    if ari_solution > 14:
        ari_solution = 14
    elif ari_solution < 14:
        ari_solution = ari_solution
    else:
        print('bummer')
       
print(ari_solution)

print(f'''\n\tThe ARI for Peter Pan is {ari_solution}
\n\tThis corresponds to a {ari_scale[ari_solution]['grade_level']} Grade level of difficulty,
\n\tthat is suitable for an average person {ari_scale[ari_solution]['ages']} years old.''')   


 
    
