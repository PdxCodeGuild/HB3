console.log('Blackjack');

//Here I have defined my variables
let faceCards = {'Q':10, 'J':10, 'K':10, 'A':1}
let firstChoice = prompt("What Is The first card? ⬇️ "); 
let secondChoice = prompt("What Is The Second Card? ⬇️");
let thirdChoice = prompt("What Is The third card? ⬇️ "); 

//Here I have used the if statements to first locate the appropriate card and second change my variable if it matches
if (firstChoice in faceCards) {
    firstChoice = faceCards[firstChoice];
 } 
 if (secondChoice in faceCards) {
    secondChoice = faceCards[secondChoice];
}
 if (thirdChoice in faceCards) {
    thirdChoice = faceCards[thirdChoice];
};

let totalAmount = parseInt(firstChoice) + parseInt(secondChoice) + parseInt(thirdChoice)

//I have used this console log solely for testing/validation purposes
console.log(totalAmount)

//This will output whether the user should "Hit", Has "Busted", or recieved "Black Jack"
if (totalAmount < 17) {
    alert(totalAmount + " Hit!");
}//Note to self: the spaces after the quotations are helpful as the provide spacing once the alert appears on the screen
 if (totalAmount == 21 ) {
    alert(totalAmount + " Black Jack!");
}
 if (totalAmount > 22 ) {
    alert(totalAmount + " Busted :(");
};