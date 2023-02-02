const form = document.querySelector("form")
const username = document.getElementById("username")
const password = document.getElementById("password")
const email = document.getElementById("email")
const phone = document.getElementById("phone")
const dob = document.getElementById("dob")
const ssn = document.getElementById("ssn")
const email_re= /(\w+[@]\w+\.com)/
const phone_re= /(\d{3}-\d{3}-\d{4})/
const dob_re= /(\d{2}\/\d{2}\/\d{4})/
const ssn_re = /(\d{3}-\d{2}-\d{4})/
const errormessage = document.getElementById("errormessage")

form.addEventListener("submit", e => {
    e.preventDefault();
    const errors= [];

    if (password.value.length < 6){
        errors.push("password must be at least 6 characters long")
        console.log(password.value)
    }
    if (username.value.length < 6){
        errors.push("Username must be at least 6 characters long")
        console.log(username.value)
        console.log(email.value)
    }
    if (!email.value.match(email_re)){
        errors.push("Format name@email.com")        
    }

    if (!phone.value.match(phone_re)){
        errors.push("Invalid phonenumber")        
    }

    if (!dob.value.match(dob_re)){
        errors.push("Format mm/dd/yyyy")        
    }

    if (!ssn.value.match(ssn_re)){
        errors.push("Invalid SSN")        
    }

    
    if(errors.length > 0){
        errormessage.toggleAttribute('hidden');
        errormessage.innerHTML = errors.join(' , ');
    }
    
    console.log(errormessage)
    
})