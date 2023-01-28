

let btn = document.getElementById("submit")
console.log(btn)


let validateFormFunction = function(event)  {
    event.preventDefault()

    let firstName=document.inputFormParams.first_name.value
    console.log(document.inputFormParams.first_name.value)
    if (firstName.length == "") {
        // alert("First Name must be entered")
        document.getElementById('first_name_check').innerHTML="First Name must be filled out"
    } else {
        document.getElementById('first_name_check').innerHTML="Working Fine"
    }

    let lastName=document.inputFormParams.last_name.value
    console.log(document.inputFormParams.last_name.value)
    if (lastName.length == "") {
        // alert("Last Name must be entered")
        document.getElementById('last_name_check').innerHTML="Last Name must be filled out"
    } else {
        document.getElementById('last_name_check').innerHTML="Working Fine"
    }
    
    let inputEmail=document.inputFormParams.inputEmail.value
    const emailPattern = /\S+@\S+\.\S+/;
    console.log(document.inputFormParams.inputEmail.value)
    if (emailPattern.test(inputEmail)) {
        // alert("Must provide a valid email with @")
        document.getElementById('email_check').innerHTML="Working Fine"
    } else {
        document.getElementById('email_check').innerHTML="Must provide a valid email"
    }


    let phoneNumber = document.inputFormParams.phone_number.value
    const pattern = /^\d{3}?[- ]?\d{3}[- ]?\d{4}$/;
    // const pattern = /[0-9]e/;
    console.log(document.inputFormParams.phone_number.value)
    if (pattern.test(phoneNumber)) {
        // alert("Must provide a valid Phone number")
        document.getElementById('phone_number_check').innerHTML="Working Fine"
    } else {
        document.getElementById('phone_number_check').innerHTML="Must provide a valid Phone Number"
        //NOTE: how do I clear the form for this ?
        
    }

    let birthDate=document.inputFormParams.birth_date.value
    const birthdayPattern = /^\d{2}?[/]?\d{2}[/]?\d{4}$/;
    console.log(document.inputFormParams.birth_date.value)
    if (birthdayPattern.test(birthDate)) {
        // alert("Must provide a valid birth date")
        document.getElementById('birth_date_check').innerHTML="Working Fine"
    } else {
        document.getElementById('birth_date_check').innerHTML="Birthdate not entered in correct format"
    }

    let socialSecurity=document.inputFormParams.social_security.value
    const socialSecurityPattern = /^\d{3}?[- ]?\d{2}[- ]?\d{4}$/;
    console.log(document.inputFormParams.social_security.value)
    if (socialSecurityPattern.test(socialSecurity)) {
        // alert("Must provide a valid social security")
        document.getElementById('social_security_check').innerHTML="Working Fine"
    } else {
        document.getElementById('social_security_check').innerHTML="Social Security number not entered correctly"
    }

    let userName=document.inputFormParams.username.value
    console.log(document.inputFormParams.username.value)
    if (userName.length < 6) {
        // alert("Must provide a valid username")
        document.getElementById('username_check').innerHTML="Username must be at least 6 characters long"
    } else {
        document.getElementById('username_check').innerHTML="Working Fine"
    }

    let inputPassword=document.inputFormParams.inputPassword.value
    console.log(document.inputFormParams.inputPassword.value)
    if (inputPassword.length < 6) {
        // alert("Must provide a valid password")
        document.getElementById('password_check').innerHTML="Password must be at least 6 characters long"
    } else {
        document.getElementById('password_check').innerHTML="Working Fine"
    }

    let test = 'Hello World'
    console.log('Hello World')


}

let formObjectInformation = document.getElementById("info_form")
console.log(formObjectInformation)
formObjectInformation.addEventListener("submit",validateFormFunction)

