// let unit = 23
// const units= "meter"
// var input= true

/* Const you can declare variable once but never change its value
    ex: const units = "meter"
        const math = "meter"   Will throw error

*/


// const title_element = document.querySelector("h1")
// console.log (title_element)

// document is everything found in other hmtl file
// queryselector allows you to specific element

// Ex #01 this is the cleanest way to write
// title_element.innerText = `Hello, ${units}`


//     innertext allows your to insert text and Innerhtml inters html 
// EX #02
 //   title_element.innerHTML = `<strong>Hello, ${name}</stong>`
// - ` ` backticks next to 1


// title_element.innerText = `Hello, ` + units

//Function is like def a function in python


// let name = ""
// when a let variable is left empty you can change it in funtion
// With a const on the other hand you could NOT change this

function SetTitle (name) {

    const title_element = document.querySelector("h1")
    title_element.innerText = `Hello, ${name}`
}
// If you stop here nothing will change on page 

// SetTitle("rachel") 
// You must call the function and ADD your input in

// You can select a specific elements 
// const button_el = document.querySelector("button")

// ADVANCE : Go to Html and add id to the element --- This helps if you have multi-btns
// const button_el = document.querySelector("#name")
//console.log(button_el)  ---Dont FORGET consol.log means run

// Note: You can have more than 1 param 

button_el.addEventListener("click", function () {
    SetTitle("rachel")
} )
// Above we are setting a function that will change soemthing on the pages
// the event happens


// Theres another way to do this.... use arrow 
// button_el.addEventListener("click", () => {
//     SetTitle("Rachel")
// } )

// An even simpler way is... get rid of parenthesis
// button_el.addEventListener("click", () => SetTitle("Bambi"))

// You can make longer actions... like below 
button_el.addEventListener("click", () => {
    SetTitle("Bambi")
    console.log("Buttonclicked")
})

// This is using innerhtml and also specifing a DIV

