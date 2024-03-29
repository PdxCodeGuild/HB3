#---------------------------------
# PDX Code Guild: HB3
# Lab06: Automated Readibility Index
# Author: Daniel Smith
# Date: 2022.11.30
#---------------------------------

# The automated readability index (ARI) is a formula for
# computing the U.S. grade level for a given block of text.
# Compute the ARI for a given book.

from requests import get
from math import ceil

# Import a book.
response = get('https://www.gutenberg.org/files/236/236-0.txt')
# response = get('https://www.gutenberg.org/files/16/16-0.txt')
# response = get('https://www.gutenberg.org/files/76/76-0.txt')
# response = get('https://www.gutenberg.org/cache/epub/17208/pg17208.txt')
# response = get('https://www.gutenberg.org/cache/epub/120/pg120.txt')
# response = get('https://www.gutenberg.org/cache/epub/4980/pg4980.txt')
# response = get('https://www.gutenberg.org/files/2781/2781-0.txt')
# response = get('https://www.gutenberg.org/files/215/215-h/215-h.htm')
response.encoding = 'utf-8'
contents = response.text

# Find the title.
t = contents.split('Title:', 1)
t = t[1].split('\n', 1)
title = t[0].strip()

# Find the author.
a = contents.split('Author:', 1)
a = a[1].split('\n', 1)
author = a[0].strip()

# Remove unwanted header/footer data. 
# ...

# Find the number of chars, words, and sentences.
char_qty = len("".join(contents.split()))
word_qty = len(contents.split())
contents = contents.replace('. ', '! ').replace('? ', '! ') # Make all sentences end w/ same char as the .split() method can only handle 1 seperator. Alternatively, importing re.split() is a way to handle > 1 seperator.
sentence_qty = len(contents.split('! '))

#testing
print(f'\n{title}')
print(f'{char_qty} characters')
print(f'{word_qty} words')
print(f'{sentence_qty} sentences')

# ARI Formula:
# The score is computed by
# multiplying the number of characters divided by the number of words by 4.71,
# adding the number of words divided by the number of sentences multiplied by 0.5,
# and subtracting 21.43. If the result is a decimal, always round up,
# and if the result is higher than 14, it should be set to 14.
ari_score = ceil((char_qty / word_qty * 4.71) + (word_qty / sentence_qty * 0.5) - 21.43)

#testing
print(f'RARI = {ari_score}')

if ari_score > 14:
    ari_score = 14

# Once you’ve computed the ARI score, you can use the following
# dictionary to look up the age range and grade level.
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

# Format and display the output data.
grade = ari_scale[ari_score]['grade_level']
age = ari_scale[ari_score]['ages']
print('\n--------------------------------------------------------')
print(f'The ARI for {title} by {author} is {ari_score}.')
print(f'This corresponds to a {grade} level of difficulty.')
print(f'This is suitable for an average person {age} years old.')
print('--------------------------------------------------------\n')