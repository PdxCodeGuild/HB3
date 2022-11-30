# Create 2 dic one 0 - 19 and 20 - 99
one_19 = {0: 'zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
ten_num = {20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety'}
# ask user to enter number
x = int(input('Enter a number between 0 - 99: '))

# use if and elif statement to give answer
if x < 20:
    alph = one_19[x]
    print(alph)
elif x in ten_num:
    alph1 = ten_num[x]
    print(alph1)
else:
    alph2 = (x // 10)*10
    alph3 = x % 10
    print(ten_num[alph2], one_19[alph3], sep='-')