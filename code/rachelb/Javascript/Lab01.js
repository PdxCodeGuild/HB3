// input--> take input and muliply by 0.3048 
// let distance = (prompt("what is the distance in feet?" ))
// let meters = 0.3048*distance
// alert(meters)
// console.log(meters)

//Second lab
// let cards ={ "A": 1, "2": 2,
// "3": 3, "4": 4, 
// "5": 5, "6": 6, 
// "7": 7, "8": 8,
// "9": 9, "10":10,
// "J":10, "Q": 10, 
// "K":10,
// "j":10,
// "q":10,
// "k":10}

// let card01 = prompt("What's your first card? " )
// let card02 = prompt("What's your second card? " )
// let card03 = prompt("What's your third card? " )
// console.log(card01, card02, card03)
// const total = cards[card01] + cards[card02] + cards[card03]
// // //  logical operators: &&, ||, and !, stand for and, or, and not
// console.log(total)
// if (total < 17) {
//     alert('Hit')
// } else if (total >= 17 && total < 21) {
//     alert("Stay")
// } else if (total == 21) {
//     alert("Blackjack!!")
// } else if (total > 21) {
//     alert("Already Busted")
// }
// console.log(total)

// Third Lab

let cc = [4,5,5,6,7,3,7,5,8,6,8,9,9,8,5,5]

function cardvalidation(){
    num = []
    let user_input = prompt("Enter a card number ") 
    console.log(user_input)
    let newcc = cc.slice(0,-1)
    newcc.reverse()
    console.log(newcc)
    for (numbers in user_input){
        num.push(user_input[numbers])
    }
    num.reverse()
    // console.log(num)
    for (let x = 0; x < cc.length; ++x){
        if (cc[x]%2 == 0){
            continue
        }
        if (cc[x] > 9){
            cc[x] - 9 
        } 
    console.log(cc[x]*2)}

    let total = 0
    for (num in cc){
        total += num}
        console.log(total)
        let remainder = total % 10
    {
        console.log(remainder)
    } 
    
        if (newcc == remainder){
            return true
        } else  {
            return false
        }       
   
}

cardvalidation()