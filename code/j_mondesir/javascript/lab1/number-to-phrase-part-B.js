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
let submitButton = document.getElementById('trans_btn');
console.log(submitButton);
let numValue = []
submitButton.addEventListener('click', function () {
    let input = document.getElementById('user_num');
    numValue.push(input.value);
    input.value = ''
    document.getElementById('display').innerText = numValue
    if (numValue < 20) {
        result = oneTo10[numValue]
    } else if (numValue in tenNumber) {
        result = tenNumber[numValue]
    } else {
        let firstDigit = Math.trunc(numValue / 10) * 10;
        let secondDigit = numValue % 10
        result = tenNumber[firstDigit] + '-' + oneTo10[secondDigit]
    }
    document.getElementById('result').innerText = result
    numValue.length = 0
})