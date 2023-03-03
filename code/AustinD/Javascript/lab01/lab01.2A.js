<!DOCTYPE html>
<html>
<body>
<script>
function draw_cards() {
    alert('When prompted, enter your card as a number or as the first letter of your named card, capitalized.');
    let x = prompt("What's your first card?");
    let y = prompt("What's your second card?");
    let z = prompt("What's your third card?");
    let drawn_cards = [x, y, z];
    return drawn_cards;
}

function advice(x) {
    const deck = {
    'A':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10,
    'J':10,
    'Q':10,
    'K':10,
    };

    let cardone = deck[x[0]];
    let cardtwo = deck[x[1]];
    let cardthree = deck[x[2]];
    let n = cardone+cardtwo+cardthree;

    if (n > 21) {
        return n + " Already Busted";
    }
    if (n == 21) {
        return n + " Blackjack!";
    }
    if (n > 17 || n == 17) {
        return n + " Stay";
    }
    if (n < 17) {
        return n + " Hit";
    }
}

alert(advice(draw_cards()));

</script>
</body>
</html>