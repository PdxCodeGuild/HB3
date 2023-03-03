
let card_1 = prompt("What's your first card? ")
let card_2 = prompt("What's your second card? ")
let card_3 = prompt("What's your third card? ")
alert(card_1 + card_2 +card_3)

let blackjack_dict = {
    "A" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10
}


let total = (blackjack_dict[card_1] + blackjack_dict[card_2] + blackjack_dict[card_3])


if (card_1 = "A") {
    if (total + 10 <= 21) {
        total = total + 10
    }
}  
else if (card_2 = "A") {
    if (total + 10 <= 21) {
        total = total + 10
    }
} 
else if (card_3 = "A") {
    if (total + 10 <= 21) {
        total = total + 10
    }
} 
else {
    total = total
}



if (total < 17) {
    alert(total + " Hit") 
}  
else if (total == 21) {
    alert(total + " Blackjack!")
    }
else if (total < 21) {
    if (total >= 17) {
        alert(total + " Stay")
    }
}
else {
    alert(total + " Hit")
}