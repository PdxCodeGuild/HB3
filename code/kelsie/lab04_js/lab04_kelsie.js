function verify() {

    const username = document.forms.myForm.username.value;
    const password = document.forms.myForm.password.value;
    const firstlast = document.forms.myForm.firstlast.value;
    const email = document.forms.myForm.email.value;
    const phone = document.forms.myForm.phone.value;
    const dob = document.forms.myForm.dob.value;
    const ssn = document.forms.myForm.ssn.value;
    
    var regPhone=/^((\(\d{3}\) ?)|(\d{3}-))?\d{3}-\d{4}$/;
    var regEmail=/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/g
    var regDOB =/^(0[1-9]|1[012])[-/.](0[1-9]|[12][0-9]|3[01])[- /.](19|20)\d\d/;
    var regFirstLast = /^[A-Za-z][A-Za-z\'\-]+[ ]+([\A-Za-z][A-Za-z\'\-]+)*/;
    var regSSN = /^\d{3}-\d{2}-\d{4}$/

    console.log(username, password, firstlast, email, phone, dob, ssn)

    if (username == "" || username.length<6) {
        alert('Username must be at least 6 characters')
    }

    if (password == "" || password.length<6) {
        alert("Password must be at least 6 characters")
    }

    if (firstlast == "" || !regFirstLast.test(firstlast)) {
        alert("Please enter your first and last name")
    }

    if (email == "" || !regEmail.test(email)) {
        alert("Please enter a valid email")
    }
    
    if (phone == "" || !regPhone.test(phone)) {
        alert("Please enter a valid phone number")
    }

    if (dob == "" || !regDOB.test(dob)) {
        alert("Please enter a valid date of birth")
    }

    if (ssn == "" || !regSSN.test(ssn)) {
        alert("Please enter a valid Social Security Number")
    }

}
