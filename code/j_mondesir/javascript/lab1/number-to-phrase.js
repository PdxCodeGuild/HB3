
let oneTo10 = {
    0: 'zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
    6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
    11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
    15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'
}

let tenNumber = {
    20: 'Twenty', 30: 'Thirty', 40: 'Forty',
    50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
    90: 'Ninety'
}

let userInput = prompt('Enter a number between 0 - 99: ')


if (userInput < 20) {
    console.log(oneTo10[userInput])

} else if (userInput in tenNumber) {
    console.log(tenNumber[userInput])
} else {
    let firstDigit = Math.trunc(userInput / 10) * 10;
    let secondDigit = userInput % 10
    console.log(tenNumber[firstDigit], oneTo10[secondDigit])
}










