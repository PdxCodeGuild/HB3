num_phrase = {
    0:"zero",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"nineteen",
    20:"twenty",
    40:"forty",
    30:"thirty",
    50:"fifty",
    60:"sixty",
    70:"seventy",
    80:"eighty",
    90:"ninety",
    100:"Hundred", 

}

num_enter = input('enter number 0-999: ')
while num_enter:
    try:
        num_enter = int(num_enter)
        if num_enter >= 0 and num_enter < 100:
            if num_enter in num_phrase:
                print(num_phrase[num_enter])
                num_enter = input('enter number 0-999: ')
            elif num_enter//10*10 in num_phrase and num_enter%10 in num_phrase:
                print(num_phrase[num_enter//10*10]+'-'+num_phrase[num_enter%10])
                num_enter = input('enter number 0-999: ')
        elif num_enter >= 100 and (num_enter%100) == 0:
            print(num_phrase[(num_enter//100)] + ' hundred')
            num_enter = input('enter number 0-999: ')
        elif num_enter > 100 and num_enter%100 in num_phrase:
            print(num_phrase[(num_enter//100)] + ' hundred' + ' ' + num_phrase[num_enter%100] )
            num_enter = input('enter number 0-999: ')
        elif num_enter > 100:
            print(num_phrase[(num_enter//100)] + ' hundred' + ' ' + num_phrase[(num_enter//10%10*10)] + '-' + num_phrase[num_enter%10])
            num_enter = input('enter number 0-999: ')
    except:
        if num_enter.lower() == 'done':
            print('thanks for playing')
            num_enter = False
        else:
            num_enter = input('not a valid entry, enter number 0-999: ')

        
    

        
    
