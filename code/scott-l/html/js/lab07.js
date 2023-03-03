function myFunction() {
    var xNav = document.getElementById("myTopnav");
    if (xNav.className === "topnav") {
      xNav.className += " responsive";
    } else {
      xNav.className = "topnav";
    }
  }


