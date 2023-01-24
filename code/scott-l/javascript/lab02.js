

// myFunction()= document.querySelector('bt')


// buttonTest.addEventListener('click', myFunction(){
//   alert('clicked');
// }

// document.getElementById("btn").innerHTML = myFunction();

function myFunction () {
    console.log(API_key)
}


let local = document.getElementById("location")

function getLocation () {

    // console.log("Location Button")
    // navigator.geolocation.getCurrentPosition(showPosition);

    navigator.geolocation.getCurrentPosition((position) => {
        console.log(position.coords.latitude)
        console.log(position.coords.longitude)
    })

    
}

function functionAPI_call() {
    
    axios({
        method: 'get',
        url: 'https://api.openweathermap.org/data/2.5/weather?lat=33.441792&lon=-94.037689& exclude=hourly,daily&appid={'+ API_key +'}'
        // url: 'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={'+API_key+'}'

    }).then((response) =>{
        let weather = response.data
        console.log(weather)

    })

}

// function showPosition(position) {
//     local.innerHTML = position.coords.latitude;
// }
