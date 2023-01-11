alert("ok")
let inPut = document.getElementById('inPut')
let reSult = document.getElementById('reSult')
let inputType= document.getElementById('inputType')
let resultType = document.getElementById('resultType')
var inputTypeValue, resultTypeValue;


distance.addEventListener("keyup", myOutcome);
resultOutput.addEventListener("change", myOutcome);
resultType.addEventListener("change", myOutcome);


function myOutcome(){
    
    reSult.value = inPut.value

}




