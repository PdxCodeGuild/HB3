
const form = document.getElementById("form");
const userName = document.getElementById("userName");
const passWord = document.getElementById("passWord");
const firstName = document.getElementById("firstName");
const lastName = document.getElementById("lastName");
const emailAddress = document.getElementById("emailAddress");
const phoneNumber = document.getElementById("phoneNumber");
const socialSecurity = document.getElementById("socialSecurity");
const dateofBirth = document.getElementById("dateofBirth");



form.addEventListener('submit', e => {
    e.preventDefault();

    validateInputs();

});
const setError = (element, message) => {
    const inputControl= element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');
    errorDisplay.innerText = message;
    inputControl.classList.add('error');
    inputControl.classList.remove('success');

};

const setSuccess = element =>{
    const inputControl= element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');
    errorDisplay.innerText = '';
    inputControl.classList.add('success');
    inputControl.classList.remove('error');

};


const validateInputs = ()=>{
    const usernameValue = userName.value.trim();
    const passWordvalue = passWord.value.trim();
    const firstNamevalue = firstName.value.trim();
    const lastNamevalue = lastName.value.trim();
    const emailAddressvalue = emailAddress.value.trim();
    const phonenumbervalue = phoneNumber.value.trim();
    const socialSecurityvalue = socialSecurity.value.trim();
    const dateofBirthvalue = dateofBirth.value.trim();

    


    if(usernameValue === ''){
        setError(userName, 'Username is required');
    }else if (usernameValue.length < 6){
        setError(userName, 'Username must be at least 6 character long.');
    }else{
        setSuccess(userName);
    }

    if(passWordvalue === ''){
        setError(passWord, 'Password is required');
    }else if (passWordvalue.length < 6){
        setError(passWord, 'Password must be at least 6 character long.');
    }else{
        setSuccess(passWord);
    }
    if(firstNamevalue === ''){
        setError(firstName, 'First name required');
    }else{
        setSuccess(firstName);
    }
    if(lastNamevalue === ''){
        setError(lastName, 'Last name required');
    }else{
        setSuccess(lastName);
    }
    if(emailAddressvalue === ''){
        setError(emailAddress, 'email address required');
    }else{
        setSuccess(emailAddress);
    }
    if(phonenumbervalue === ''){
        setError(phoneNumber, 'Phonenumber required');
    }else{
        setSuccess(phoneNumber);
    }
    if(socialSecurityvalue === ''){
        setError(socialSecurity, 'SSN required');
    }else{
        setSuccess(socialSecurity);
    }
    if(dateofBirthvalue === ''){
        setError(dateofBirth, 'Date required');
    }else{
        setSuccess(dateofBirth);
    }
}




