

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

        let lat_pos = position.coords.latitude
        let long_pos = position.coords.longitude

        document.getElementById('lat_id').innerText = lat_pos
        document.getElementById('long_id').innerText = long_pos
    })

}

function functionAPI_call() {
    
    // console.log('https://api.openweathermap.org/data/2.5/weather?lat=33.441792&lon=-94.037689& exclude=hourly,daily&appid='+ API_key)
    axios({
        method: 'get',
        url: 'https://api.openweathermap.org/data/2.5/weather?lat=33.441792&lon=-94.037689& exclude=hourly,daily&appid='+ API_key
        // url: 'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={'+API_key+'}'
        // url: 'https://api.openweathermap.org'
        // url: 'https://icanhazdadjoke.com/',
        // headers: {'accept':'application/json'}

    }).then((response) => {
        let weather = response.data
        console.log(weather)
        document.getElementById('weather_output').innerText = weather


        document.getElementById('imgTEST').src = 'http://openweathermap.org/img/wn/04d.png'

    })

}

// function showPosition(position) {
//     local.innerHTML = position.coords.latitude;
// }
