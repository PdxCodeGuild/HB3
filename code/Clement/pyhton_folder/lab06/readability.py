
# ari_scale = {
#      1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
#      2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
#      3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
#      4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
#      5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
#      6: {'ages': '10-11', 'grade_level':    '5th Grade'},
#      7: {'ages': '11-12', 'grade_level':    '6th Grade'},
#      8: {'ages': '12-13', 'grade_level':    '7th Grade'},
#      9: {'ages': '13-14', 'grade_level':    '8th Grade'},
#     10: {'ages': '14-15', 'grade_level':    '9th Grade'},
#     11: {'ages': '15-16', 'grade_level':   '10th Grade'},
#     12: {'ages': '16-17', 'grade_level':   '11th Grade'},
#     13: {'ages': '17-18', 'grade_level':   '12th Grade'},
#     14: {'ages': '18-22', 'grade_level':      'College'}
# }




def grades_level():

    character = 0
    sentences = 0
    words = 1

    with open('file.txt', 'r') as f:
        contents = f.read()

    # count the number of characters, words and sentences in a given text
        for char in contents:
            if char.isalpha():
                character += 1

            elif char == " ":
                words += 1

            elif char == "." or char == "!" or char == "?":
                sentences +=1

    #  The Formula for Automated Readability Index
    score = 4.71 * (character/words) + 0.5 * (words/sentences) - 21.43

    if score <= 1:
        return 'Kindergarten'

    elif score == 2:
        return '1st Grade'

    elif score == 3:
        return '2nd Grade'

    elif score == 4:
        return '3rd Grade'

    elif score == 5:
        return '4th Grade'

    elif score == 6:
        return '5th Grade'

    elif score == 7:
        return '6th Grade'

    elif score == 8:
        return '7th Grade'

    elif score == 9:
        return '8th Grade'

    elif score == 10:
        return '9th Grade'

    elif score == 11:
        return '10th Grade'
    elif score == 12:
        return '11th Grade'
    elif score == 13:
        return '12th Grade'
    elif score == 14:
        return 'College'

    else:
        return round(score)

print(grades_level())



