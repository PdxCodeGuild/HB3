import requests 
import math

response = requests.get('https://www.gutenberg.org/cache/epub/64317/pg64317.txt')
response.encoding = 'utf-8'
# print(response)

contents = response.text
# print(len(contents))

character = 0
words = 0
sentences = 0

for char in contents:
    if char == ' ' or char == '.'  or char == '?' or char == '!':
        if char != ' ':
            sentences += 1 
        else:

            words += 1
    else:
        character += 1
# print(character)
# print(words)
# print(sentences)

Score = 4.71*(character/words) + 0.5*(words/sentences) - 21.43
ari = (math.ceil(Score))                                                              # Fun Tip: ceil = Ceiling and will round up, Floor division will round down 
for ari in range(ari):
    if ari > 14 : 
        ari = 14
    else:
        ari = ari 
print(f'The ARI for gettysburg-address.txt is {ari}')

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

for scale in ari_scale:
    if ari == ari_scale:
         print[ari_scale.get[1]]