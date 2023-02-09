<script>
  export default{
    data() {
    return {
      userPick: '',
      cpuPick: '',
      outcome: '',
    };
  },

    methods: { 
      // Call variables for CPU User and Outcome 
      options(choice){
        // Use the data() to determine what obj needs to be called
        this.userPick = choice;
        
        this.cpuPick = this.getcpuPick();
        this.outcome = this.getoutcome();
  },



// computer random choices
  getcpuPick(){
    const choices = ['rock', 'paper','scissors'];
    const random = [Math.floor(Math.random() * 3)]
    return choices[random];
  },
// Outcome of rounds
  getoutcome(){
    if (this.userPick === 'rock' && this.cpuPick === 'scissor'){
      return "User wins!"
    }; 
    if (this.userPick === "scissors" && this.cpuPick === "paper"){
      return "User wins!"
    };
    if (this.userPick === 'paper' && this.cpuPick === 'rock'){
      return "CPU is the LOSER!!"
    }
    if (this.userPick === this.cpuPick) 
    return 'Tie!';
  }
    }
};

</script>


<template>
  <main>
    <div class="game">
      
     <div class = "options">
      <button @click="options ('rock')">Rock</button>
      <button @click="options ('paper')">Paper</button>
      <button @click="options('scissors')">Scissors</button>
     </div>
     
     <div class = "outcome">
      <p> User picked: {{ userPick }}</p>
      <p> Computer picked: {{ cpuPick }}</p>
      <p> Outcome: {{ outcome }}</p>
     </div>
        
      
    </div>
  </main>
</template>



<style scoped>
  main {
    width: 100vw;
    height: 100vh;
    background-color: rgb(48, 48, 48);
    display: flex;
    align-items: center;
    justify-content: center;
  }

  div .game {
    width: 400px;
    height: 200px;
    border-radius: 15px;
    text-align: center;
    background-color: rgba(9, 9, 9, 0.489);
    padding: 20px;
  }

  p{
    padding: 5px;
  }
</style>