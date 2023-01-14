

function num_to_phrase() {
    let choice = document.getElementById("user_input").submit();
    alert(choice)

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


