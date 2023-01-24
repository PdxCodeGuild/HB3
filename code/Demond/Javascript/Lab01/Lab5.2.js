console.log('Unit Converter 2');

//This is my prompt and will store the values for the unit converter
let distanceToConvert = prompt("What Is The Distance? Enter a Whole Number Below ⬇️"); 
let unitsToConvert = prompt("What Are The Units? Enter Ft or Mi or Km ⬇️");

//I have used the if and else statments for the actual conversion 
if (unitsToConvert == 'ft' || 'FT') {
    let units = 0.3048
    let tester = `${distanceToConvert} ${unitsToConvert} is ${distanceToConvert * units} meters`;
   alert(`${distanceToConvert} ${unitsToConvert} is ${distanceToConvert * units} meters`);
 } else 
 if (unitsToConvert == 'mi' || 'MI') {
    let units = 1609.34
   alert(`${distanceToConvert} ${unitsToConvert} is ${distanceToConvert * units} meters`);;
}
 else 
 if (unitsToConvert == 'km' || 'KM') {
    let units = 1000
    alert(`${distanceToConvert} ${unitsToConvert} is ${distanceToConvert * units} meters`);;
};