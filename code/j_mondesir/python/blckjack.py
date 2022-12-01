
question_1 = input('What is your first card? ')
question_2 = input('What is your second card? ')
question_3 = input('What is your third card? ')
card_value = {'A' : 1, 
              '2' : 2, 
              '3' : 3, 
              '4' : 4,  
              '5': 5,
              '6' : 6,
              '7' : 7,
              '8' : 8,
              '9' : 9,
              '10' : 10,
              'J' : 10,
              'Q' : 10,
              'K' : 10
              }
def your_hand(x,y,z) :
    x = card_value[question_1]
    y = card_value[question_2]
    z = card_value[question_3]
    w = x+y+z
    if w < 17:
        return (f'{w} Hit')
    elif 21 > w >= 17:
        return (f'{w} Stay')
    elif w == 21:
        return (f'{w} Blackjack')
    else:
        return 'Already Busted'
        
result = your_hand(question_1,question_2,question_3)  
        
print(result)