const form = document.querySelector("form")
const submit= document.querySelector("#btn")
console.log(form)

const email_re= /(\w+[@]\w+\.com)/
const phone_re= /(\d{3}-\d{3}-\d{4})/



const errormessage = document.getElementById("errormessage")

submit.addEventListener("click", function() {
    const errors= [];

    
    const phone = document.form.phone.value
    console.log(phone)
    // const username = document.getElementById("username")
    // const password = document.getElementById("password")
    // const email = document.getElementById("email")
    // console.log(email)
    
    // if (password.value.length < 6){
    //     errors.push("password must be at least 6 characters long")
    // }

    // if (username.value.length < 6){
    //     errors.push("Username must be at least 6 characters long")
    // }
    
    // if (!email.match(email_re)){
    //     errors.push("Format name@email.com")        
    // }

    // if (!phone.match(phone_re)){
    //     errors.push("Invalid format")        
    // }

   
    if(errors.length > 0){
        // e.preventDefault();
        errormessage.toggleAttribute('hidden');
        errormessage.innerHTML = errors.join(' , ');

    }
    
    return false
})

