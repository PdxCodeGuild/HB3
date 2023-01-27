

let btn = document.getElementById("submit")
console.log(btn)


let validateFormFunction = function(event)  {
    event.preventDefault()

    let firstName=document.inputFormParams.first_name.value
    console.log(document.inputFormParams.first_name.value)
    if (firstName.length < 2) {
        // alert("First Name must be entered")
        document.getElementById('first_name_check').innerHTML="First Name must be entered"
    }

    let lastName=document.inputFormParams.last_name.value
    console.log(document.inputFormParams.last_name.value)
    if (lastName.length < 2) {
        // alert("Last Name must be entered")
        document.getElementById('last_name_check').innerHTML="Last Name must be entered"
    }
    
    let inputEmail=document.inputFormParams.inputEmail.value
    console.log(document.inputFormParams.inputEmail.value)
    if (inputEmail.length < 2) {
        // alert("Must provide a valid email with @")
        document.getElementById('email_check').innerHTML="Must provide a valid email with @"
    }


    let phoneNumber = document.inputFormParams.phone_number.value
    console.log(document.inputFormParams.phone_number.value)
    if (phoneNumber.length < 12) {
        // alert("Must provide a valid Phone number")
        document.getElementById('phone_number_check').innerHTML="Must provide a valid Phone Number"
    }

    let birthDate=document.inputFormParams.birth_date.value
    console.log(document.inputFormParams.birth_date.value)
    if (birthDate.length < 9) {
        // alert("Must provide a valid birth date")
        document.getElementById('birth_date_check').innerHTML="Birthdate not entered in correct format"
    }

    let socialSecurity=document.inputFormParams.social_security.value
    console.log(document.inputFormParams.social_security.value)
    if (socialSecurity.length < 11) {
        // alert("Must provide a valid social security")
        document.getElementById('social_security_check').innerHTML="Social Security number not entered in correct format"
    }

    let userName=document.inputFormParams.username.value
    console.log(document.inputFormParams.username.value)
    if (userName.length < 6) {
        // alert("Must provide a valid username")
        document.getElementById('username_check').innerHTML="Username must be at least 6 characters long"
    }

    let inputPassword=document.inputFormParams.inputPassword.value
    console.log(document.inputFormParams.inputPassword.value)
    if (inputPassword.length < 6) {
        // alert("Must provide a valid password")
        document.getElementById('password_check').innerHTML="Password must be at least 6 characters long"
    }

    let test = 'Hello World'
    console.log('Hello World')


}

let formObjectInformation = document.getElementById("info_form")
console.log(formObjectInformation)
formObjectInformation.addEventListener("submit",validateFormFunction)

