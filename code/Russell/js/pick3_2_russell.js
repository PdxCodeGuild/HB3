numeral = parseInt(prompt("Enter number to be converted to text "))


let ones_digit = numeral % 10
let tens_digit = Math.floor(numeral / 10) % 10
let hundreds_digit = Math.floor(numeral / 100) % 10


let alpha_hundreds = ['', 'one hundred ', 'two hundred ', 'three hundred ', 'four hundred ', 
'five hundred ', 'six hundred ', 'seven hundred ', 'eight hundred ', 'nine hundred ']

let alpha_tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

let alpha_ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

let alpha_teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

if (numeral > 99)
    if (numeral % 100 >= 10 && numeral % 100 <= 19)
        alert(alpha_hundreds[hundreds_digit] + alpha_teens[(numeral % 100)%10])
    
    else
        if(ones_digit == 0)
           alert(alpha_hundreds[hundreds_digit] + alpha_tens[tens_digit])
        
        else if(tens_digit == 0)
            alert(alpha_hundreds[hundreds_digit] + alpha_tens[tens_digit] + alpha_ones[ones_digit])

        else
            alert(alpha_hundreds[hundreds_digit] + alpha_tens[tens_digit] + '-' + alpha_ones[ones_digit])
    
else

    if (numeral >= 10 && numeral <= 19)
        alert(alpha_teens[(numeral % 100)%10])

    else

        if (ones_digit == 0 && numeral > 0)
           alert(alpha_tens[tens_digit])
        
        else if (tens_digit == 0)
            alert(alpha_tens[tens_digit] + alpha_ones[ones_digit])

        else 
            alert(alpha_tens[tens_digit] + '-' + alpha_ones[ones_digit])