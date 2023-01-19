
//  *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
//  Project: Lab 1 - Javascript Pick 3
//  Author: Scott Lefgren
//  Email: scojlefg@gmail.com
//  Date: January 17, 2023
// ___________________          _-_
// \==============_=_/ ____.---'---`---.____
//        \_ \    \----._________.----/
//          \ \   /  /    `-_-'
//      __,--`.`-'..'-_
//     /____          ||
//          `--.____,-'

// *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*

// Pick 3 Python labs and re-do them in JavaScript. 
// You should first try to write them using JavaScript's prompt 
// and alert in place of Python's input and print.

// Part B

// Once you have that working, use input and button elements, 
// with events. You can read the docs on DOM Manipulation and Events. 
// You can view a demo here. Please save these as separate files 
// from your part A.

// ----------------------------------------------------
// PICK 1

// Ask the user for the number of feet, and print out the equivalent 
// distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output 
// in meters by multiplying the input distance by 0.3048.

// Below is some sample input/output.
// > what is the distance in feet? 12
// > 12 ft is 3.6576 m


function myFunction() {

    let feet_input = document.querySelector('#feet_input');
    let feet_value = feet_input.value;
    console.log(feet_value);

    let ft_unit_convert = 0.3048;  // Unit conversion (1 ft = 0.3048)
    let a = feet_value;
    let b = ft_unit_convert;
    //define simple multiply function
    function multiplyFunction(a,b) {
         return a * b;
     }
     console.log(multiplyFunction(a,b));
    //end function multiply

    document.getElementById("output_meters").innerHTML = multiplyFunction(a,b) + " meters";


}


// -------------------------------------------------------