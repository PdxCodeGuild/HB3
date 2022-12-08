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

def grades_level():
    character = 0
    sentences = 0
    words = 1

    with open('file.txt', 'r') as f:
        contents = f.read()

    # count the number of characters,
    #  words and sentences in a given text
        for char in contents:
            if char.isalpha():
                character += 1
            elif char == " ":
                words += 1
            elif char == "." or char == "!" or char == "?":
                sentences +=1
    
    # The Formula for Automated Readability Index
    score = 4.71 * (character/words) + 0.5 * (words/sentences) - 21.43
    return round(score)


print("=========================================================================\n")
print(f"The ARI for Hemingway-file.txt readability index score is {grades_level()}\nThis corresponds to a {ari_scale[grades_level()]['grade_level']} level of difficulty\nAnd that is suitable for an average person {ari_scale[grades_level()]['ages']} years old.")
print("\n=========================================================================")





