const usernameEl = document.querySelector('#username');
const passwordEl = document.querySelector('#password');
const confirmPasswordEl = document.querySelector('#confirm-password');
const firstLastEl = document.querySelector('#first_last_name');
const emailEl = document.querySelector('#email');
const phoneNumberEl = document.querySelector('#phone');
const dobEl = document.querySelector('#dob');
const ssnEl = document.querySelector('#ssn');

const form = document.querySelector('#signup');

const checkUsername = () => {
    let valid = false;

    const min = 6,
        max = 20;

    const username = usernameEl.value.trim();

    if (!isRequired(username)) {
        showError(usernameEl, 'Username cannot be blank.');
    } else if (!isBetween(username.length, min, max)) {
        showError(usernameEl, `Username must be between ${min} and ${max} characters.`)
    } else {
        showSuccess(usernameEl);
        valid = true;
    }
    return valid;
};

const checkPassword = () => {
    let valid = false;

    const min = 6,
        max = 20;

    const password = passwordEl.value.trim();

    if (!isRequired(password)) {
        showError(passwordEl, 'Password cannot be blank.');
    } else if (!isPasswordSecure(password)) {
        showError(passwordEl, 'Password must have at least 6 characters that include at least 1 lowercase character, 1 uppercase characters, 1 number, and 1 special character in (!@#$%^&*)');
    } else if (!isBetween(password.length, min, max)) {
        showError(passwordEl, `Password must be between ${min} and ${max} characters.`)
    } else {
        showSuccess(passwordEl);
        valid = true;
    }
    return valid;
};

const checkConfirmPassword = () => {
    let valid = false;
    // check confirm password
    const confirmPassword = confirmPasswordEl.value.trim();
    const password = passwordEl.value.trim();

    if (!isRequired(confirmPassword)) {
        showError(confirmPasswordEl, 'Please enter the password again');
    } else if (password !== confirmPassword) {
        showError(confirmPasswordEl, 'The password does not match');
    } else {
        showSuccess(confirmPasswordEl);
        valid = true;
    }
    return valid;
};

const checkEmail = () => {
    let valid = false;
    const email = emailEl.value.trim();
    if (!isRequired(email)) {
        showError(emailEl, 'Email cannot be blank.');
    } else if (!isEmailValid(email)) {
        showError(emailEl, 'Email is not valid.')
    } else {
        showSuccess(emailEl);
        valid = true;
    }
    return valid;
};

const checkName = () => {
    let valid = false;
    const first_last_name = firstLastEl.value.trim();
    if (!isRequired(first_last_name)) {
        showError(firstLastEl, 'Name cannot be blank.');
    } else if (!isNameValid(first_last_name)) {
        showError(firstLastEl, 'Name is not valid.')
    } else {
        showSuccess(firstLastEl);
        valid = true;
    }
    return valid;
};

const checkPhone = () => {
    let valid = false;
    const phone = phoneNumberEl.value.trim();
    if (!isRequired(phone)) {
        showError(phoneNumberEl, 'Phone number cannot be blank.');
    } else if (!isPhoneValid(phone)) {
        showError(phoneNumberEl, 'Phone number is not valid.')
    } else {
        showSuccess(phoneNumberEl);
        valid = true;
    }
    return valid;
};

const checkDob = () => {
    let valid = false;
    const dob = dobEl.value.trim();
    if (!isRequired(dob)) {
        showError(dobEl, 'Birthdate cannot be blank.');
    } else if (!isDobValid(dob)) {
        showError(dobEl, 'Birthdate is not valid.')
    } else {
        showSuccess(dobEl);
        valid = true;
    }
    return valid;
};

const checkSSN = () => {
    let valid = false;
    const ssn = ssnEl.value.trim();
    if (!isRequired(ssn)) {
        showError(ssnEl, 'SSN cannot be blank.');
    } else if (!isSSNValid(ssn)) {
        showError(ssnEl, 'SSN is not valid.')
    } else {
        showSuccess(ssnEl);
        valid = true;
    }
    return valid;
};

const isSSNValid = (ssn) => {
    const re = /^(?!000|666)[0-8][0-9]{2}-(?!00)[0-9]{2}-(?!0000)[0-9]{4}$/;
    return re.test(ssn);
};

const isDobValid = (dob) => {
    const re = /^(0?[1-9]|1[012])\/(0?[1-9]|[12][0-9]|3[01])\/((19|20)\d\d)$/;
    return re.test(dob);
};

const isPhoneValid = (phone) => {
    const re = /^(\()?\d{3}(\))?(-|\s)?\d{3}(-|\s)\d{4}$/;
    return re.test(phone);
};

const isNameValid = (first_last_name) => {
    const re = /^[a-zA-Z]+ [a-zA-Z]+$/;
    return re.test(first_last_name);
};

const isEmailValid = (email) => {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
};

const isPasswordSecure = (password) => {
    const re = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})");
    return re.test(password);
};

const isRequired = value => value === '' ? false : true;
const isBetween = (length, min, max) => length < min || length > max ? false : true;


const showError = (input, message) => {
    // get the form-field element
    const formField = input.parentElement;
    // add the error class
    formField.classList.remove('success');
    formField.classList.add('error');

    // show the error message
    const error = formField.querySelector('small');
    error.textContent = message;
};

const showSuccess = (input) => {
    // get the form-field element
    const formField = input.parentElement;

    // remove the error class
    formField.classList.remove('error');
    formField.classList.add('success');

    // hide the error message
    const error = formField.querySelector('small');
    error.textContent = '';
}

form.addEventListener('submit', function (e) {
    // prevent the form from submitting
    e.preventDefault();

    // validate fields
    let isUsernameValid = checkUsername(),
        isPasswordValid = checkPassword(),
        isConfirmPasswordValid = checkConfirmPassword(),
        isEmailValid = checkEmail(),
        isNameValid = checkName(),
        isPhoneValid = checkPhone(),
        isDobValid = checkDob(),
        isSSNValid = checkSSN();

    let isFormValid = isUsernameValid &&
        isPasswordValid &&
        isConfirmPasswordValid &&
        isEmailValid &&
        isNameValid &&
        isPhoneValid &&
        isDobValid &&
        isSSNValid;

    // submit to the server if the form is valid
    if (isFormValid) {
    }
});

const debounce = (fn, delay = 500) => {
    let timeoutId;
    return (...args) => {
        // cancel the previous timer
        if (timeoutId) {
            clearTimeout(timeoutId);
        }
        // setup a new timer
        timeoutId = setTimeout(() => {
            fn.apply(null, args)
        }, delay);
    };
};

form.addEventListener('input', debounce(function (e) {
    switch (e.target.id) {
        case 'username':
            checkUsername();
            break;
        case 'email':
            checkEmail();
            break;
        case 'password':
            checkPassword();
            break;
        case 'confirm-password':
            checkConfirmPassword();
            break;
        case 'first_last_name':
            checkName();
            break;
        case 'phone':
            checkPhone();
            break;
        case 'dob':
            checkDob();
            break;
        case 'ssn':
            checkSSN();
            break;
    }
}));
