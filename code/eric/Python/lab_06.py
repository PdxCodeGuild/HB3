# compute the ARI for a given book. 

import requests

site_url = "https://www.gutenberg.org/"

# enter the book ID number from project gutenberg 
book_id = input("Enter Gutenberg book ID number:")
url = site_url + 'cache/epub/' + book_id + '/pg' + book_id + '.txt'
response = requests.get(url)
data = response.text

# count the number of characters
char = len(data)

# count the number of words
words = data.split()
word_count = len(words)

# count the number of sentences
sentences = data.splitlines()
sentence_count = len(sentences)
print(sentence_count)

# compute the ARI for the text
ARI = (4.71 * (char/word_count)) + (.5 * (word_count/char)) - 21.43

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

print('______________________________________________________')
print('The ARI for ', url, 'is', ARI)
print('This corresponds to a ', 'Grade level of difficulty')
