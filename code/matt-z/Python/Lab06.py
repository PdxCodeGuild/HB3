import requests
import re
import string

url = 'https://www.gutenberg.org/cache/epub/2641/pg2641.txt'

response = requests.get(url)
response.encoding = 'utf-8'

text = response.text
letters = string.ascii_letters

def count_words(text):
    words = text.split(" ")
    return len(words)

def count_chars(text):
    chars = []
    for char in text:
        if char in letters:
            chars.append(char)
    return len(chars)

def count_sentences(text):
    sentences = re.split('\.| ! | \? | \.\.\.', text)
    return len(sentences)

def ari(word, char, sentence):
    return int(4.71*(char/word) + .5*(word/sentence) - 21.43)

word_count = count_words(text)
char_count = count_chars(text)
sentence_count = count_sentences(text)

adjusted_ri = ari(word_count, char_count, sentence_count)

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

print(f'''
The ARI for filename is {adjusted_ri}
This corresponds to a {ari_scale[adjusted_ri]['grade_level']} level of difficulty
that is suitable for an average person {ari_scale[adjusted_ri]['ages']} years old.
''')