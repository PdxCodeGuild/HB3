function formVal() {
    //get data from user input
    var username = document.registration.username.value;
    console.log(username);
    var password = document.registration.password.value;
    var flname = document.registration.flname.value;
    var email = document.registration.email.value;
    var phnum = document.registration.phnum.value;
    var dob = document.registration.dob.value;
    var ssnum = document.registration.ssnum.value;

    // username must be at least 6 characters long
    var regUsername = /^[a-zA-Z!@#$%^&+=\d]{6,}$/;
    // password must be at least 6 characters long
    var regPassword = /^[a-zA-Z!@#$%^&+=\d]{6,}$/;
    // name must contain letters, a space, then more letters
    var regFlName = /^[a-zA-Z]+\s[a-zA-Z]+$/;
    // email must contain characters, followed by an @ symbol, followed by alphanumeric characters, followed by a ., followed by alphanumeric characters
    var regEmail =
      /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    // phone number must contain 10 digits
    var regPhNum = /^\d{10}$/;
    // date of birth must contain only number, and must be in mm/dd/yyyy format
    var regDoB =
      /^(0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])[- /.](19|20)\d\d$/;
    // ssn must not begin with 666, 000, or anything from 900-999, and must be in xxx-xx-xxxx format
    var regSSNum =
      /^(?!666|000|9\\d{2})\\d{3}-(?!00)\\d{2}-(?!0{4})\\d{4}$/;

    if (!regUsername.test(username)) {
      alert("Username must be at least 6 characters long");
    }

    if (!regPassword.test(password)) {
      alert("Password must be at least 6 characters long");
    }

    if (!regFlName.test(flname)) {
      alert("Please enter your first and last name");
    }

    if (!regEmail.test(email)) {
      alert("Please enter a valid email address");
    }

    if (!regPhNum.test(phnum)) {
      alert("Please enter your 10-digit phone number (no spaces/dashes)");
    }

    if (!regDoB.test(dob)) {
      alert("Enter DoB in mm/dd/yyyy format");
    }

    if (!regSSNum.test(ssnum)) {
      alert("Please enter a valid SSN");
    }
    return false;
  }