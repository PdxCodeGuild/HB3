let btn = document.querySelector("button")
console.log(btn)
let cards = []

btn.addEventListener("click", function(){
    let value = parseInt(document.getElementById("num").value)
    cards.push(value)
    document.getElementById("solution").innerText = cards
    if(cards.length > 2){
        sum = cards[0] + cards[1] + cards[2]
        console.log(sum)
    }
})
