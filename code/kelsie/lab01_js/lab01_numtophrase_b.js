

function num_to_phrase() {
    let choice = document.getElementById("user_input").value;
    alert(choice)

    let tens_digit = Math.floor(choice/10)
    let ones_digit = choice%10

    tens_list = {
        0: "", 
        1: "teen", 
        2: "Twenty", 
        3: "Thirty", 
        4: "Forty", 
        5: "Fifty", 
        6: "Sixty", 
        7: "Seventy", 
        8: "Eighty", 
        9: "Ninety"
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
        result = ones_list[choice]
    }

    else if (choice >= 20) {
        result = tens_list[tens_digit] + '-' + ones_list[ones_digit]
    }

    document.getElementById("result").innerHTML = result;

}

