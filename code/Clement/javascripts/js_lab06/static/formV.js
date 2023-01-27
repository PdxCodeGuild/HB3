const form = document.getElementById("form");
const lastName = document.getElementById("lastName");
const userName = document.getElementById("userName");
const passWord = document.getElementById("passWord");
const firstName = document.getElementById("firstName");
const dateofBirth = document.getElementById("dateofBirth");
const phoneNumber = document.getElementById("phoneNumber");
const emailAddress = document.getElementById("emailAddress");
const socialSecurity = document.getElementById("socialSecurity");
const togglePassword = document.getElementById("togglePassword");
const passwordToggle = document.getElementById("passwordToggle");


function formatPhoneNumber(value) {
  if (value === false) return value;
  const phoneNumber = value.replace(/[^\d]/g, "");
  const phoneNumberLength = phoneNumber.length;
  if (phoneNumberLength < 4) return phoneNumber;
  if (phoneNumberLength < 7) {
    return `(${phoneNumber.slice(0, 3)}) ${phoneNumber.slice(3)}`;
  }
  return `(${phoneNumber.slice(0, 3)}) ${phoneNumber.slice(
    3, 6)}-${phoneNumber.slice(6, 9)}`;
}


function formatSocialsecurity(value) {
  if (!value) return value;
  const socialSecurity = value.replace(/[^\d]/g, "");
  const socialSecurityLength = socialSecurity.length;
  if (socialSecurityLength < 4) return socialSecurity;
  if (socialSecurityLength < 7) {
    return `(${socialSecurity.slice(0, 3)}) ${socialSecurity.slice(3)}`;
  }
  return `(${socialSecurity.slice(0, 3)}) ${socialSecurity.slice(
    2, 4)}-${socialSecurity.slice(4, 7)}`;
}

function phoneNumberFormatter() {
  const phoneNumber = document.getElementById("phoneNumber");
  const formattedInputValue = formatPhoneNumber(phoneNumber.value);
  phoneNumber.value = formattedInputValue;
}

function socialSecurityFormatter() {
  const socialSecurity = document.getElementById("socialSecurity");
  const formatInputValue = formatSocialsecurity(socialSecurity.value);
  socialSecurity.value = formatInputValue;
}

form.addEventListener("submit", (e) => {
  e.preventDefault();

  validateInputs();
});


passwordToggle.addEventListener("click", function () {
  this.classList.toggle("fa-eye-slash");
  const type =
    socialSecurity.getAttribute("type") === "password" ? "type" : "password";
  socialSecurity.setAttribute("type", type);
});


togglePassword.addEventListener("click", function () {
  this.classList.toggle("fa-eye-slash");
  const type =
    passWord.getAttribute("type") === "password" ? "type" : "password";
  passWord.setAttribute("type", type);
});


const setError = (element, message) => {
  const inputControl = element.parentElement;
  const errorDisplay = inputControl.querySelector(".error");
  errorDisplay.innerText = message;
  inputControl.classList.add("error");
  inputControl.classList.remove("success");
};


const setSuccess = (element) => {
  const inputControl = element.parentElement;
  const errorDisplay = inputControl.querySelector(".error");
  errorDisplay.innerText = "";
  inputControl.classList.add("success");
  inputControl.classList.remove("error");
};


const validateInputs = () => {
  const usernameValue = userName.value.trim();
  const passWordvalue = passWord.value.trim();
  const firstNamevalue = firstName.value.trim();
  const lastNamevalue = lastName.value.trim();
  const emailAddressvalue = emailAddress.value.trim();
  const phonenumbervalue = phoneNumber.value.trim();
  const socialSecurityvalue = socialSecurity.value.trim();
  const dateofBirthvalue = dateofBirth.value.trim();



  // Conditional statements to check for Username validations
  if (usernameValue === "") {
    setError(userName, "Field is required");
  } else if (usernameValue.length < 6) {
    setError(userName, "Username must be at least 6 character long.");
  } else {
    setSuccess(userName);
  }

  // Conditional statements to check for Password validations
  if (passWordvalue === "") {
    setError(passWord, "Field is required");
  } else if (passWordvalue.length < 6) {
    setError(passWord, "Password must be at least 6 character long.");
  } else {
    setSuccess(passWord);
  }


  // Conditional statements to check errors field input validations
  if (firstNamevalue === "") {
    setError(firstName, "Field is required");
  } else {
    setSuccess(firstName);
  }
  if (lastNamevalue === "") {
    setError(lastName, "Field is required");
  } else {
    setSuccess(lastName);
  }


  if (emailAddressvalue === "") {
    setError(emailAddress, "Field is required");
  } else {
    setSuccess(emailAddress);
  }
  if (phonenumbervalue === "") {
    setError(phoneNumber, "Field is required");
  } else {
    setSuccess(phoneNumber);
  }


  if (socialSecurityvalue === "") {
    setError(socialSecurity, "Field is required");
  } else {
    setSuccess(socialSecurity);
  }
  if (dateofBirthvalue === "") {
    setError(dateofBirth, "Field is required");
  } else {
    setSuccess(dateofBirth);
  }
};
