// username must be at least 6 characters long
// let btn = document.getElementById('submit')
// btn.addEventListener('submit', function(e){
//     e.preventDefault
// })

function validationForm(){
   let user_input = document.registraion.username.value;
    console.log(user_input);
    if (user_input.length < 6){
        alert('Username must be at least 6 characters long')
    }
    return false
}