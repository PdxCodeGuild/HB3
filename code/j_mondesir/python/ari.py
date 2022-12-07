import os 
import math

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

user_text = input('Enter the name of the file you are checking: ')

def check_grade_level(text):
    open_file = open(user_text, 'r')
    read_file = open_file.read()
    num_words = len(read_file.split())
    print(num_words)
    num_sentences = read_file.count('.') + read_file.count('!') + read_file.count(';') + read_file.count(':') + read_file.count('?')
    print(num_sentences)
    characters = 0
    for char in read_file:
        characters += 1
        print(characters)
    ari = round((4.71*(characters/num_words)) + (0.5*(num_words/num_sentences))-21.43)
    return ari
ARI = check_grade_level(user_text)

print(f'The ARI for {user_text} is {ARI}')

        
    
    

