let firstQuestion = prompt('What is your first card? ')
let secondQuestion = prompt('What is you second card? ')
let thirdQuestion = prompt('what is your third card? ')

let card_value = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}
let firstPick = card_value[firstQuestion]
let secondPick = card_value[secondQuestion]
let thirdPick = card_value[thirdQuestion]
let totalPick = firstPick + secondPick + thirdPick

if (totalPick < 17) {
    console.log(totalPick, 'Hit')
} else if (21 > totalPick >= 17) {
    console.log(totalPick, 'Stay')
} else if (totalPick === 21) {
    console.log(totalPick, 'Blackjack')
} else {
    console.log('Already Busted')
}





