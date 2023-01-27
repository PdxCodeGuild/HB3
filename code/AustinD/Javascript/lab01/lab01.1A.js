<!DOCTYPE html>
<html>
<body>
<script>
//For use in step 4 of validation
const double = (x) => x*2;

//For use in step 5 of validation
const subtract_9_if_over_9 = (x) => x > 9 ? x - 9 : x;

const creditcard = () => {
    let entry = prompt("Enter a credit card number with no spaces:");
    //Converts the input string into a list of ints
    const cc = entry.split("").map(Number);
    //Slices off the last digit, assigned as check digit variable.
    const check_digit = cc[cc.length - 1];
    //Reverses the digits
    let validation_digits = cc.slice().reverse();
    //Doubles every other digit with double function
    validation_digits.forEach((val, index) => {
        if (index % 2 === 0) validation_digits[index] = double(val);
    });
    //Subtracts 9 from every number over 9 with the subtrat_9_if_over_9 function
    validation_digits = validation_digits.map(subtract_9_if_over_9);
    //Sums all values
    validation_digits = validation_digits.reduce((a,b) => a + b);
    //Checks the second digit of the sum against the check digit for invalid and valid credit card numbers
    if (check_digit !== (validation_digits % 10)) {
        return alert(false)
    } else {
        return alert(true)
    }
}

creditcard();
</script>
</body>
</html>