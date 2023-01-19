// const re = 

function validateForm() {
    let x = document.registration.username.value;
    console.log(x)
    if (x.length < 6) {
      alert("Username must be at least 6 characters long");
      return false;
    }
  }