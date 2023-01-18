

// #################### Pick 6 Lab

alert('Blackjack Advice Lab in Javascript')

let card_values = {
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
    'K': 10,
}   
    
alert('This is a card game. You can select the value of card: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q or K).')

let card_1_input = alert('What is your first card: ')
let card_2_input = alert('What is your second card: ')
let card_3_input = alert('What is your third card: ')

let card_1 = card_values[card_1_input]
let card_2 = card_values[card_2_input]
let card_3 = card_values[card_3_input]

alert(card_1, card_2, card_3)

let card_count = card_1 + card_2 + card_3

if (card_count < 17) {
    alert(card_count + ' that is low: Hit!')
} else if (17 <= card_count < 21) {
    alert(card_count + " is good: Stay!")
} else if (card_count == 21) {
    alert(card_count + " Blackjack!")
}else {
    alert(card_count + " Already Busted...bummer")}