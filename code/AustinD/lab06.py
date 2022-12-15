import requests

#Acquires book through url, establishes grading and age appropriate scale, runs through other functions.
def main():
    url = input('Provide a url:')
    content = pull_content(url)
    ari = calculate_ari(content)
    #Constrains ari score to dict index
    if ari > 14:
        ari = 14

    scale = {
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

    (ages, grade_level) = get_reading_level(ari, scale)
    #Returns final prompt 
    return f"The ARI score of the text is: {ari}\nThe appropriate age range of this text is: {ages}\n The grade elevel of this text is: {grade_level}"

#Grabs written content and returns it
def pull_content(url):
    response = requests.get(url)
    return response.text

#Collects variables for input then spits out ari score
def calculate_ari(content):
    num_chars = len(content)
    num_words = len(content.split())
    num_sentences = (content.count(".") + content.count("!") + content.count("?"))

    ari = (4.71 * (num_chars / num_words)) + (0.5 * (num_words / num_sentences)) - 21.43
    ari = round(ari)
    return ari

#Grabs ari from scale dict
def get_reading_level(ari, scale):
    ages = scale[ari]['ages']
    grade_level = scale[ari]['grade_level']

    return ages, grade_level

print(main())