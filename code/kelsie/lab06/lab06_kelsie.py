
import math


def find_ari(f) :   
    f = open(f)
    text = f.read()
    new_text = text.replace(" " , "")
    
    # count how many characters there are
    characters = len(new_text)
    print(characters)
    
    

    # find words by calculating how many whitespaces are in the text
    word_list = text.split(' ')     
    words = len(word_list)
    

    # find sentences by calculating how many sentence-ending punctuation marks are present
    sentences = (text.split('.') + text.split('!') + text.split('!'))   
    sentence_num = len(sentences)
    f.close()

    # calculate the ari with the given formula, round up for decimals and return 14 for any number greater than 14
    ari = math.ceil((4.71 * (characters/words)) + (0.5 * (words/sentence_num)) - 21.43) 
    for ari in range(ari) :
        if ari > 14 :
            ari = 14
        else :
            ari = ari

    

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

   
    print(f"""The ARI for {'{}'.format(f.name)} is {ari}.
This corresponds to a {ari_scale[ari]['grade_level']} level of difficulty.
This is suitable for an average person of {ari_scale[ari]['ages']} years old.""")

find_ari('book_1.txt')

