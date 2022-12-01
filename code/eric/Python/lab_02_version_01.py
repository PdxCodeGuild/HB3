# Convert a given number into its english representation.

#v.1 0-99
num_word = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
    30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'
}

number = int(input('Input a number (0-99): '))
tens_digit = (number//10)
ones_digit = (number % 10)

if number <= 20:
    print(num_word[number])
elif number < 100:
    if (number % 10) == 0: print(num_word[number])
    else: print(num_word[number // 10 * 10] + '-' + num_word[number % 10])