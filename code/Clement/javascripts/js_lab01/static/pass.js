var btn = document.getElementById("button");

btn.addEventListener("click", function () {
  createPass();
});

function createPass() {
  var char =
    "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()/><;{}[]=+-`.'|";
  var pw_Lenght = 30;
  var password = "";

  for (var i = 0; i < pw_Lenght; i++) {
    var randomChar = Math.floor(Math.random() * char.length);
    password += char.substring(randomChar, randomChar + 1);
  }
  document.getElementById("password").value = password;
}