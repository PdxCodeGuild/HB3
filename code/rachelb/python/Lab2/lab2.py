#Modulus is the %
num_list = { 
    0:'zero',
    1:'one', 
    2:'two', 
    3:'three', 
    4:'four', 
    5:'five', 
    6:'six', 
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten', 
    11:'eleven',
    12:'twelve', 
    13:'thirteen',
    14:'fourteen',
    15:'fifteen', 
    16:'sixteen', 
    17:'seventeen', 
    18:'eighteen', 
    19:'nineteen', 
    20:'twenty', 30:'thirty', 40:'fourty', 50:'fifty', 
    60:'sixty', 70:'seventy',
    80:'eighty', 90:'ninety'} 


hundreds = {100:'one hundred', 
    200:'two hundred',
    300:'three hundred',
    400:'four hundred',
    500:'five hundred',
    600:'six hundred',
    700:'seven hundred',
    800:'eight hundred',
    900:'nine hundred',
    1000:'one thousand'}

# you can use modulus to extract the ones and tens digit.
# use the digit as an index to look up a string in a list.
# Handle numbers from 100-999.

# user = input('Enter number:')


def num_to_word(num):
    if type(num) != int:
        return 'this is not a number'
    elif num <= 19:
        return num_list[num]
    elif num >= 20 and num <= 99:
        if num % 10 == 0:
            return num_list[(num // 10) * 10]
        return num_list[(num // 10) * 10] + ' ' + num_list[num % 10]
    elif num > 99:
        if (num % 100) >= 11 and (num % 100) <= 19:
            firstnumber = (num // 100) * 100
            specialnum = (num % 100)
            return hundreds[firstnumber] + ' ' + num_list[specialnum] 
        elif (num % 100) == 0:
            return hundreds[num // 100 * 100]
        elif (num % 100) % 10 == 0:
            firstnumber = (num // 100) * 100
            secondnumber = (num % 100) // 10 * 10
            return hundreds[firstnumber] + ' ' + num_list[secondnumber]
        firstnumber = (num // 100) * 100
        secondnumber = (num % 100) // 10 * 10
        thirdnumber = (num % 100) % 10
        # print(thirdnumber) 
        return hundreds[firstnumber] + num_list[secondnumber] + ' ' +  num_list[thirdnumber]
   

print(num_to_word(120))

# for num in user:
#     if int(num) in list:
#         (list[int(num)])
#     elif int(num) < 20:
#         print (int((list)[user]))
#     elif int(num) >= 19:
#         if int(num) % 10 == 0:
#             print (list)[(int(num) // 10) * 10]
#         print(list[int(num // 10) * 10])
# if 1 in list:
#     print( 1 + int(list['one']))