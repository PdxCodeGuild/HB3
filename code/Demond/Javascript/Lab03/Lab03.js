function validateForm() {
    let userPass = document.getElementById("usernameandpass").value;
    if (userPass.length < 5) {
        alert("username and password must be at least 6 characters long.");
    }
    let name = document.getElementById("fullName").value;
    if (name. == false) {
        alert(" first name must contain one or more letters, space, one or more letters")
    }
    return true
};


// if (email == /^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$/);
// return { "email recieved"};