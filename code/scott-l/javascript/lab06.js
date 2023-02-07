//lab06.js file


// # Rock Paper Scissors
// """
// Let's play rock-paper-scissors with the computer.
//    1. Greet the user and use a for loop to display their possible choices.
// Welcome to Rock, Paper, Scissors!
// Your options are:

// - Rock
// - Paper
// - Scissors

// Enter your selection:  

//    2. The computer will ask the user for their choice (rock, paper, scissors).
//    3. The computer will randomly choose rock, paper or scissors.
//    4. Compare the players' choices and determine who won and tell the user.

// NOTE: Do not use index positions during the lab to target any values
// """
// #-------------------------------------------------------------------------#


let app = new Vue({
    el: '#app',
    data: {
        message1: 'Rock',
        message2: 'Paper',
        message3: 'Scissors',
        game_inputs: [],
        options: ["Rock", "Paper", "Scissors"],
        computer_choose_options: [],
        },

    methods: {
        
        Button1: function() {
            // console.log(this.message1)
            let user_input = document.querySelector("#game_input").value;
            console.log(user_input)
            
            if (!user_input) {
                return
            }

            // Computer will randomly choose rock, paper, or scissors to initialize a variable
            let numberChoice = Math.floor(Math.random()*3);
            console.log(numberChoice)

            let computer_choice = this.options[numberChoice]
            let winner = ""

            if ( user_input == 'Rock' && computer_choice == 'Rock') {
                // # If both the Human and Computer choose Rock it is a Tie 
                winner = "TIE"
                
    
            } else if ( user_input == 'Paper' && computer_choice == 'Paper'){
                // # If both the Human and Computer choose Paper it is a Tie
                winner = "TIE"
                
            
            } else if ( user_input == 'Scissors' && computer_choice == 'Scissors'){
                // # If both the Human and Computer choose Scissors it is a Tie
                winner=  "TIE"
                
    
            } else if ( user_input == 'Rock' && computer_choice == 'Paper'){
                // # If Human choose Rock and Computer choose paper Computer is Winner
                winner  = "Computer -Paper covers Rock!"
                
    
            } else if ( user_input == 'Rock' && computer_choice == 'Scissors'){
                // # If Human choose Rock and Computer choose Scissors Human is Winner           
                 winner= "Human  -Rock smashes Scissors!"
                
                
            } else if ( user_input == 'Paper' && computer_choice == 'Rock'){
                // # If Human choose Paper and Computer choose Rock Human is Winner
                winner="Human  -Paper covers Rock!"
                
                
            } else if ( user_input == 'Paper' && computer_choice == 'Scissors'){
                // # If Human choose Paper and Computer choose Scissors Computer is Winner
                winner="Computer -Scissors cut Paper!"
                
                
            } else if ( user_input == 'Scissors' && computer_choice == 'Rock'){
                // # If Human choose Scissors and Computer choose Rock Computer is Winner
                winner= "Computer -Rock smashes Scissors!"
                
        
            } else if ( user_input == 'Scissors' && computer_choice == 'Paper'){
                // # If Human choose Scissors and Computer choose Paper Human is Winner
                winner = "Human --Scissors cut Paper!"
                
            }
            // # end if

            this.game_inputs.push({
                id: Date.now(),
                human_results: user_input,
                computer_choice_results: computer_choice,
                winner_results: winner,  
            })
           
            console.log(this.game_inputs)
            document.querySelector("#game_input").value = ""
            
        },
 
    },
    
})

