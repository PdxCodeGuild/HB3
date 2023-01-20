function ccNumChecker(cardNumber) {

    console.log(cardNumber)
    let ccNum = Array.from(String(cardNumber), Number);
    checkDigit = ccNum.pop();
    console.log(ccNum)
    console.log(checkDigit)
    let reverseNum = ccNum.reverse();
    console.log(reverseNum)

    for (let i=0; i<reverseNum.length; i++) {
        if (i % 2 ===0) {
            reverseNum[i] = reverseNum[i] * 2
        }
    }
    console.log(reverseNum)

    for (let i=0; i<reverseNum.length; i++) {
        if (reverseNum[i] > 9) {
            reverseNum[i] = reverseNum[i] - 9
        }
    }
    console.log(reverseNum)
   
    // console.log(ccNum)
    // let check_digit = cardNumber.pop()
    // console.log(check_digit)
}

ccNumChecker(1234567898765432)