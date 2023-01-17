<!DOCTYPE html>
<html>
<body>
<input id="input1" type="text">
<input id="input2" type="text">
<input id="input3" type="text">
<button id="submit" onclick="draw_cards()">Submit</button>
<div id="output"></div>
<script>
function draw_cards() {
    let x = document.getElementById("input1").value;
    let y = document.getElementById("input2").value;
    let z = document.getElementById("input3").value;
    let drawn_cards = [x, y, z];
    document.getElementById("output").innerHTML = advice(drawn_cards);
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

</script>
</body>
</html>