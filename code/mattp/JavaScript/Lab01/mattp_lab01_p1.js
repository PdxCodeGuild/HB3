// #################### Unit Converter Lab


let units_in = {
    "feet": .3048,
    "miles": 1609.34,
    "meters": 1,
    "kilometers": 1000,
    "yards": 0.9144,
    "inches": 0.0254
}

alert('\n{units}')

let units_out = {
    "feet": 1/.3048,
    "miles": 1/1609.34,
    "meters": 1,
    "kilometers": 1/1000,
    "yards": 1/.9144,
    "inches": 1/.0254
}

let distance = prompt('What is the distance: ')

console.log('distance')

let input_unit = prompt('What are the input units (feet, miles, meters, kilometers, yards, inches): ')

let output_unit = prompt('What are the output units (feet, miles, meters, kilometers, yards, inches): ')

input_switch = units[input_unit]

output_switch = units2[output_unit]


// ##################### Number to Phrase Lab

// ones = {
//     0: 'zero',
//     1: 'one',
//     2: 'two',
//     3: 'three',
//     4: 'four',
//     5: 'five',
//     6: 'six',
//     7: 'seven',
//     8: 'eight',
//     9: 'nine',
//     10: 'ten',
//     11: 'eleven',
//     12: 'twelve',
//     13: 'thirteen',
//     14: 'fourteen',
//     15: 'fifteen',
//     16: 'sixteen',
//     17: 'seventeen',
//     18: 'eighteen',
//     19: 'nineteen'
// }

// tens = {
//     2: 'twenty',
//     3: 'thirty',
//     4: 'forty',
//     5: 'fifty',
//     6: 'sixty',
//     7: 'seventy',
//     8: 'eighty',
//     9: 'ninety'
// }

// number_input = input('\n\tSelect a number (00-99): ')

// number_input = int(number_input)

// tens_digit = number_input//10
// ones_digit = number_input%10


// #print(f'\n\t{number_input} spelled out is: {small_number}')


// '''if (number_input >= 1) and (number_input <= 19):
//     small_word = ones[number_input]
//     print(f'\n\t{number_input} spelled out is: {small_word}')
    
// elif number_input >= 20:
//     tens_word = tens[tens_digit]
//     ones_word = ones[ones_digit]
    
//     print(f'\n\t{number_input} spelled out is: {tens_word} {ones_word}')'''
    
// if number_input >= 0 and number_input <= 19:
//     small_word = ones[number_input]
//     print(f'\n\t{number_input} spelled out is: {small_word}')
    
// elif number_input >= 20 and number_input <= 99:
//     tens_word = tens[tens_digit]
//     ones_word = ones[ones_digit]
//     if ones_digit == 0:
//         print(f'\n\t{number_input} spelled out is: {tens_word}')
//     else:
//         print(f'\n\t{number_input} spelled out is: {tens_word}-{ones_word}')


// // #################### Pick 6 Lab

// import random

// def pick6():
//     number_list = []   ### i had parenthesis here instead of brackets, causing issues later in the code
//     for num in range(6):
//        numbers = random.randint(1, 99) 
//        number_list.append(numbers)
//     return number_list   #### initially screwed this up because i had it apply to the winning ticket only


// def num_matches(winning, ticket):
//     match = 0
//     for num in range(6):
//         if winning[num] == ticket[num]:
//             match = match + 1

//     ###### this will account for all the matching possibilities        
            
//     if match == 0:
//         return 0
    
//     elif match == 1:
//         return 4
    
//     elif match == 2:
//         return 7
    
//     elif match == 3:
//         return 100
    
//     elif match == 4:
//         return 50000
    
//     elif match == 5:
//         return 1000000
    
//     elif match == 6:
//         return 25000000

// account_balance = 0

// winning = pick6()

// for num in range(100000):
    
//     ticket = pick6()
    
//     account_balance -= 2

//     winnings = num_matches(winning, ticket)   #####this was giving me an error because i didnt put brackeus at the top
    
//     account_balance = account_balance + winnings

// print(f'\n\tCongrats! you have won: {account_balance} dollars')


