nums_list = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eightteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'fourty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninty',
}

def nums_to_words(num):
    if type(num) != int:
        return 'this is not a number'

    elif num < 20:
        return nums_list[num]

    elif num > 19:
        if num % 10 == 0:
            return nums_list[(num // 10) * 10]            
        return nums_list[num // 10 * 10] + ' - ' + nums_list[num % 10]

print(nums_to_words(58))