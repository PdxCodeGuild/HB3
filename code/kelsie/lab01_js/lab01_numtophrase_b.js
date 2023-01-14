

function num_to_phrase() {
    let choice = document.getElementById("user_input").value;
    alert(choice)

    let tens_digit = Math.floor(choice/10)
    let ones_digit = choice%10

    tens_list = {
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

    ones_list = [
         "",
         "one",
         "two",
         "three",
         "four",
         "five",
         "six",
         "seven",
         "eight",
         "nine",
         "ten",
         "eleven",
         "twelve",
         "thirteen",
         "fourteen",
         "fifteen",
         "sixteen",
         "seventeen",
         "eighteen",
         "nineteen"
    ]
    

    if (choice < 20) {
        alert(ones_list[choice])
    }

    else if (choice >= 20) {
        alert(tens_list[tens_digit] + '-' + (ones_list[ones_digit]))
    }

}

