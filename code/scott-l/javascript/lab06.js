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
// #-----------------------------------------------------------------------#


let app = new Vue({
    el: '#app',
    data: {
        message: 'hello world!',
        message1: 'Rock',
        message2: 'Paper',
        message3: 'Scissors',
        image_url: 'https://placekitten.com/200/200',
        game_inputs: []

        },

    methods: {
        sayHello: function() {
            console.log(this.message)
        },
        Button1: function() {
            // console.log(this.message1)
            let user_input = document.querySelector("#game_input").value;
            console.log(user_input)
            if (!user_input) {
                return
            }
            this.game_inputs.push({
                id: Date.now(),
                title: user_input,
                complete: true
            })
            console.log(this.game_inputs)
            document.querySelector("#game_input").value = ""

        },
        games_complete: function(){
            this.game_inputs.complete = !this.game_inputs.complete
            console.log(game_inputs.title)
        },

        Button2: function() {
            console.log(this.message2)
        },
        Button3: function() {
            console.log(this.message3)
        }
    },
    
    created: function() {
        console.log(this.message)
    }
})

