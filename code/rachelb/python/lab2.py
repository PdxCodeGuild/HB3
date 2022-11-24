#Modulus is the %
list = { 
    0:'',
    1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven',
8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen',
14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 
19:'nineteen', 20:'twenty', 30:'thirty', 40:'fourty', 50:'fifty', 60:'sixty', 70:'seventy',
80:'eighty', 90:'ninety', 100:'hundred'}

user = input('Enter number:')

for num in user:
    # print(num)
    if int(num) in list:
        print(list[int(num)])
# if 1 in list:
#     print( 1 + int(list['one']))