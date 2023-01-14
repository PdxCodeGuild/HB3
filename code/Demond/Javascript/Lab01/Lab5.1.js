console.log('hello world');

let dictionary = {'meters': 3048}
let numberToConvert = prompt("please enter number to convert") 
// prompt is similar to using "input" from python
let base = dictionary.meters
let x = `${numberToConvert} ft is ${numberToConvert * dictionary.meters} meters`; 
console.log(x);
alert(x)
// use the `` backtics as "fstrings in Java"


// this is my second lab