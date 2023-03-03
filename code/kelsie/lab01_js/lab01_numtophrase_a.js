let choice = prompt("Pick a number from 1 - 99: ")
let num = parseInt(choice)


let tens_digit = Math.floor(num/10)
let ones_digit = num%10


let tens_list = {
    0: "", 
    1: "teen", 
    2: "twenty", 
    3: "thirty", 
    4: "forty", 
    5: "fifty", 
    6: "sixty", 
    7: "seventy", 
    8: "eighty", 
    9: "ninety"
}

let ones_list = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}



if (tens_digit == 1) {
    if (ones_digit == 0) {
        alert("ten")
    }
    else if (ones_digit == 1) {
        alert("eleven")
    }
    else if (ones_digit == 2) {
            alert("twelve")
    }
    else if (ones_digit == 3) {
        alert("thirteen")
    }
    else if (ones_digit == 5) {
        alert("fifteen")
    }
    else if (ones_digit == 8) {
        alert("eighteen")
    }
    else {
        alert(ones_list[ones_digit] + tens_list[tens_digit])
    }
}
    
if (tens_digit != 1) {
    if (ones_digit == 0) {
        alert(tens_list[tens_digit])
    }
    else {
        alert(tens_list[tens_digit] + '-' + ones_list[ones_digit])
    }
}
