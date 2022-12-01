

#def find_ari(text) :
import math

text = ("""All day long we seemed to dawdle through a country which was 
full of beauty of every kind. Sometimes we saw little towns or castles on 
the top of steep hills such as we see in old missals; sometimes we ran by
rivers and streams which seemed from the wide stony margin on each side
of them to be subject to great floods. It takes a lot of water, and
running strong, to sweep the outside edge of a river clear. At every
station there were groups of people, sometimes crowds, and in all sorts
of attire. Some of them were just like the peasants at home or those I
saw coming through France and Germany, with short jackets and round hats
and home-made trousers; but others were very picturesque. The women
looked pretty, except when you got near them, but they were very clumsy
about the waist. They had all full white sleeves of some kind or other,
and most of them had big belts with a lot of strips of something
fluttering from them like the dresses in a ballet, but of course there
were petticoats under them. The strangest figures we saw were the
Slovaks, who were more barbarian than the rest, with their big cow-boy
hats, great baggy dirty-white trousers, white linen shirts, and enormous
heavy leather belts, nearly a foot wide, all studded over with brass
nails. They wore high boots, with their trousers tucked into them, and
had long black hair and heavy black moustaches. They are very
picturesque, but do not look prepossessing. On the stage they would be
set down at once as some old Oriental band of brigands. They are,
however, I am told, very harmless and rather wanting in natural
self-assertion.""")

characters = len(text)
print(characters)


word_list = text.split(' ')
words = len(word_list)# find words by calculating how many whitespaces are in the text
print(word_list)
print(words)

sentence_list = text.split('.')
print(sentence_list)
sentences = len(sentence_list)
    
print(sentences)

ari = math.ceil((4.71 * (characters/words)) + (0.5 * (words/sentences)) - 21.43)
for ari in range(ari) :
    if ari > 14 :
        ari = 14
    else :
        ari = ari
        



print(ari)



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

final_ari = ari_scale[ari]
print(final_ari)
#answer = {ari_scale[gettysburg_address]}
#print(answer)


