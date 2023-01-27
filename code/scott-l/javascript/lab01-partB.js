
//  *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
//  Project: Lab 1 - Javascript Pick 3
//  Author: Scott Lefgren
//  Email: scojlefg@gmail.com
//  Date: January 17, 2023
// ___________________          _-_
// \==============_=_/ ____.---'---`---.____
//        \_ \    \----._________.----/
//          \ \   /  /    `-_-'
//      __,--`.`-'..'-_
//     /____          ||
//          `--.____,-'

// *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*

// Pick 3 Python labs and re-do them in JavaScript. 
// You should first try to write them using JavaScript's prompt 
// and alert in place of Python's input and print.

// Part B

// Once you have that working, use input and button elements, 
// with events. You can read the docs on DOM Manipulation and Events. 
// You can view a demo here. Please save these as separate files 
// from your part A.

// ----------------------------------------------------
// PICK 1

// Ask the user for the number of feet, and print out the equivalent 
// distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output 
// in meters by multiplying the input distance by 0.3048.

// Below is some sample input/output.
// > what is the distance in feet? 12
// > 12 ft is 3.6576 m


function myFunction() {

    let feet_input = document.querySelector('#feet_input');
    let feet_value = feet_input.value;
    console.log(feet_value);

    let ft_unit_convert = 0.3048;  // Unit conversion (1 ft = 0.3048)
    let a = feet_value;
    let b = ft_unit_convert;
    //define simple multiply function
    function multiplyFunction(a,b) {
         return a * b;
     }
     console.log(multiplyFunction(a,b));
    //end function multiply

    document.getElementById('output_meters').innerHTML= 
    feet_value + " ft is " + multiplyFunction(a,b) + " meters";
}

function myFunction2() {

    //  Create a dictionary of playing cards
    // playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)
    let playing_cards = {  // playing card name: points
        A: 1,   // Ace
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        J: 10,   // Jack
        Q: 10,   // Queen
        K: 10    // King
    }
    
    // figure out the point value of each card individually
    let first_card = document.querySelector('#first_card');
    let first_card_val = playing_cards[first_card.value];
    console.log("First Card Points: " + first_card_val);
    let second_card = document.querySelector('#second_card');
    let second_card_val = playing_cards[second_card.value];
    console.log("Second Card Points: " + second_card_val);
    let third_card = document.querySelector('#third_card');
    let third_card_val = playing_cards[third_card.value];
    console.log("Third Card Points: " + third_card_val);

    let card_sum = first_card_val + second_card_val + third_card_val;
    
    //  Less than 17, advise to "Hit"
    //  Greater than or equal to 17, but less than 21, advise to "Stay"
    //  Exactly 21, advise "Blackjack!"
    //  Over 21, advise "Already Busted"
    if (card_sum < 17) {
    console.log("Advise: " + card_sum + " Hit");
    document.getElementById('blackjack_output').innerHTML="Advise: " + card_sum + " Hit";
    } else if (card_sum > 17 && card_sum < 21) {
    console.log("Advise: " + card_sum + " Stay");
    document.getElementById('blackjack_output').innerHTML="Advise: " + card_sum + " Stay";
    } else if (card_sum == 21){
        console.log("Advise: "+ card_sum + " BlackJack!");
        document.getElementById('blackjack_output').innerHTML="Advise: "+ card_sum + " BlackJack!";
    } else {
        console.log("Advise: "+ card_sum + " Already Busted");
        document.getElementById('blackjack_output').innerHTML="Advise: "+ card_sum + " Already Busted";
    }
    // end if
   
}


function myFunction3() {
        
    axios({
     method: 'get',
     url: 'https://icanhazdadjoke.com/',
     headers: {'accept':'application/json'}

    }).then((response) => {
     let dad = response.data
     console.log(dad)
     document.getElementById('dadjoke_output').innerText = dad.joke
    })


 }

// -------------------------------------------------------