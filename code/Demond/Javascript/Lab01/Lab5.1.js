console.log('Unit Converter 1');

let dictionary = {'meters': 3048}
let numberToConvert = prompt("how many ft?") 
// prompt is similar to using "input" from python
let base = dictionary.meters
let x = `${numberToConvert} ft is ${numberToConvert * dictionary.meters} meters`; 
console.log(x);
alert(x)
// Note To Self: use the `` backtics as "fstrings in Java" similar to fstrings in python