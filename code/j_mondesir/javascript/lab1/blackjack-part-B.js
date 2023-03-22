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

let submitButton = document.querySelector("button")
console.log(submitButton)
let cards = []
submitButton.addEventListener("click", function () {
    let userValue = document.getElementById("num")
    cards.push(userValue.value)
    userValue.value = ''
    document.getElementById("solution").innerText = cards
    let sum = 0
    if (cards.length < 3) {
    } else {
        for (let i = 0; i < cards.length; i++) {
            sum += card_value[cards[i]]
            console.log(card_value[cards[i]])
        }
        if (sum < 17) {
            result = (sum, 'Hit')
        } else if (21 > sum >= 17) {
            result = (sum, 'Stay')
        } else if (sum === 21) {
            result = (sum, 'Blackjack')
        } else {
            result = 'Busted'
        }
        document.getElementById('result').innerText = result
    }
})