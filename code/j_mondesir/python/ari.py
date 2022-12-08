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

def ari_ARI(text):
    open_file = open(user_text, 'r')
    read_file = open_file.read()
    num_words = len(read_file.split())
    num_sentences = read_file.count('.') + read_file.count('!') + read_file.count(';') + read_file.count(':') + read_file.count('?')
    characters = read_file.replace(" ","")
    n_of_ch = len(characters)
    ari = round(4.71*(n_of_ch/num_words) + 0.5*(num_words/num_sentences)-21.43)
    return ari
ARI = ari_ARI(user_text)

print(f'The ARI for {user_text} is {ARI}')

if ARI == 1:
    print('This correspond to a',ari_scale[1]['grade_level'], 'Grade level of difficulty' '\nthat is suitable for an average person', ari_scale[1]['ages'], 'years old')
elif ARI == 2:
    print('This correspond to a',ari_scale[2]['grade_level'], 'Grade level of difficulty' '\nthat is suitable for an average person', ari_scale[2]['ages'], 'years old')
elif ARI == 3:
    print('This correspond to a',ari_scale[3]['grade_level'], 'Grade level of difficulty' '\nthat is suitable for an average person', ari_scale[3]['ages'], 'years old')
elif ARI == 4:
    print('This correspond to a',ari_scale[4]['grade_level'], 'Grade level of difficulty' '\nthat is suitable for an average person', ari_scale[4]['ages'], 'years old')
elif ARI == 5:
    print('This correspond to a',ari_scale[5]['grade_level'], 'Grade level of difficulty' '\nthat is suitable for an average person', ari_scale[5]['ages'], 'years old')
elif ARI == 6:
    print('This correspond to a',ari_scale[6]['grade_level'], 'Grade level of difficulty' '\nthat is suitable for an average person', ari_scale[6]['ages'], 'years old')
elif ARI == 7:
    print('This correspond to a',ari_scale[7]['grade_level'], 'Grade level of difficulty' '\nthat is suitable for an average person', ari_scale[7]['ages'], 'years old')
elif ARI == 8:
    print('This correspond to a',ari_scale[8]['grade_level'], 'Grade level of difficulty' '\nthat is suitable for an average person', ari_scale[8]['ages'], 'years old')
elif ARI ==9:
    print('This correspond to a',ari_scale[9]['grade_level'], 'Grade level of difficulty' '\nthat is suitable for an average person', ari_scale[9]['ages'], 'years old')
elif ARI == 10:
    print('This correspond to a',ari_scale[10]['grade_level'], 'Grade level of difficulty' '\nthat is suitable for an average person', ari_scale[10]['ages'], 'years old')
elif ARI == 11:
    print('This correspond to a',ari_scale[11]['grade_level'], 'Grade level of difficulty' '\nthat is suitable for an average person', ari_scale[11]['ages'], 'years old')
elif ARI == 12:
    print('This correspond to a',ari_scale[12]['grade_level'], 'Grade level of difficulty' '\nthat is suitable for an average person', ari_scale[12]['ages'], 'years old')
elif ARI == 13:
    print('This correspond to a',ari_scale[13]['grade_level'], 'Grade level of difficulty' '\nthat is suitable for an average person', ari_scale[13]['ages'], 'years old')            
else:
    print('This correspond to a',ari_scale[14]['grade_level'], 'Grade level of difficulty' '\nthat is suitable for an average person', ari_scale[14]['ages'], 'years old')
        
           



        
    
    

