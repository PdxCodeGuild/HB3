
// get info from form box and put a limit of 6 characters only use function
// do the same for password

const form = document.querySelector("form");


form.addEventListener("submit", event => {
    event.preventDefault();

    const form = document.getElementById('form');
    const password = document.getElementById('password');
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const DOB = document.getElementById('DOB').value;
    
    console.log(DOB)
    console.log(email)
    console.log(username)
    let errors = [];

    
    if (username){
        let maxLength = 6;
        if (username.length == maxLength) {
        return 
    }

    if (!email) {
    errors.push("Email is required");
    } else if (!/\S+@\S+/.test(email)) {
    errors.push("Email is invalid");
    }
    if (!password) {
    errors.push("Password is required");{
    } if (password.length == maxLength){
    return
    }}
    
    if (!DOB) {
    errors.push("Date of birth is required");
    }
    
    

    // if (errors.length) {
    // } else {
    // form.submit();
    // }
    }});

   