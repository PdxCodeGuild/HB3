function validateForm() {
    let user = document.getElementById("username").value;
    if (user.length < 6 ) {
        alert("Username must be at least 6 characters long.");
    } 
    let pass = document.getElementById("password").value;
    if (pass.length < 6) {
        alert("Password must be at least 6 characters long.");
    }
    let name = document.getElementById("fullName").value;
    let name_regex = /(\w+ \w+)/
    if (!name.match(name_regex)){
        alert("first name must contain one or more letters, space, one or more letters")
    }
    let emails = document.getElementById("email").value;
    let email_regex = /(\w+[@]\w+\.com)/
    if (!emails.match(email_regex)){
        alert("email requires one or more numbers/letters, @, one or more numbers/letters, ., one or more numbers/letters")
    }
    let phonen = document.getElementById("phone").value;
    let phone_regex = /(^\d{3}-\d{3}-\d{4}$)/
    if (!phonen.match(phone_regex)){
        alert("Phone number should be in this format e.g. 293-213-5555")
    }
    let dob = document.getElementById("birth").value;
    let dob_regex = /(^\d{2}\/\d{2}\/\d{4}$)/
    if (!phonen.match(dob_regex)){
        alert("Birth date should be in this format e.g. 2/13/2627")
    }
    let sss = document.getElementById("social").value;
    let sss_regex = /(^\d{3}-\d{2}-\d{4}$)/
    if (!sss.match(sss_regex)){
        alert("Social should be in this format e.g. 415-25-2627")
    };
    return false;
};