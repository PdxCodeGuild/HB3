
 let years = 0;
 let jackalopes = [0, 0];
 let living_jacks =[]

function GenerateJacks() {
    while (living_jacks.length < 1000) { 
     
        for (index in jackalopes) {
            jackalopes[index] += 1;
            if (jackalopes[index] >3 && jackalopes[index] <9) {
            jackalopes.push(0);
        }
            living_jacks = jackalopes.filter(checkAge)
     
    }
       
    years += 1
    }
document.getElementById("result").innerHTML = ("It took " + years + " years to grow the population to 1000!")

}

function checkAge(jack) {
    return jack <= 10; 
}