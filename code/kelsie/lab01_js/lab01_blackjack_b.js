

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


function Score() {
    card_a = document.getElementById('card_a').value;
    card_b = document.getElementById('card_b').value;
    card_c = document.getElementById('card_c').value;
    total = (blackjack_dict[card_a] + blackjack_dict[card_c] + blackjack_dict[card_b]);

    if (card_a === "A" && total<=11) {
        total = total + 9
    }

    if (card_b === "A" && total<=11) {
        total = total + 9
    }

    if (card_c === "A" && total<=11) {
        total = total + 9
    }

    if (total === 21) {
        result = ("Your total is " + total + ", You Win!")
    }

    if (total > 21) {
        result = ("Your total is " + total + ", Bust!")
    }

    if (total < 21 && total >=17) {
        result = ("Your total is " + total + ", Stay!")
    }

    if (total < 17) {
        result = ("Your total is " + total + ", Hit!")
    }


    document.getElementById("result").innerHTML = result

}



