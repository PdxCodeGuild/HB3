# Create 2 dic one 0 - 19 and 20 - 99
one_19 = {0: 'zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
ten_num = {20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety'}
hundred_num = {100: 'Hundred', 200:'Two-hundred', 300:'Three-hundred', 400:'Four-hundred', 500:'Five-hundred', \
                 600:'Six-hundred', 700:'Seven-hundred', 800:'Eight-hundred', 900:'Nine-hundred'}

# ask user to enter number
x = int(input('Enter a number between 0 - 99: '))

# use if and elif statement to give answer
if x < 20:
    alph = one_19[x]
    print(alph)
elif x in ten_num:
    alph1 = ten_num[x]
    print(alph1)
elif x <= 99:
    alph2 = (x // 10)*10
    alph3 = x % 10
    print(ten_num[alph2], one_19[alph3], sep='-')
elif x in hundred_num:
    alph8 = hundred_num[x]
    print(alph8)
elif x > 100:       # elif statement for number over hundred
    alph9 = x//100
    alph10 = x%100
    alph6 = (alph10//10)*10
    aplh7 = alph10%10
    z = {**one_19, **ten_num} # merge two dict to make it easy to grab the english equivalent
    if alph10 <=20:
        print(one_19[alph9],'hundred', z[alph10]) # create a if and else statement to choose what to print
    elif alph10 > 20:
        print(one_19[alph9], 'hundred', ten_num[alph6],one_19[aplh7])
        
    
        
