// let weather = 'https://api.openweathermap.org/data/3.0/onecall?appid='+ APIkey
    

// let lat = 0
// let lon = 0

// var button = document.querySelector('button')
// let input = document.querySelector('latitude')

var x = document.getElementById("weather");



function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else { 
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}
function showPosition(position) {
    let lat = position.coords.latitude
    let lon = position.coords.longitude
  x.innerHTML = "Latitude: " + position.coords.latitude + 
  "<br>Longitude: " + position.coords.longitude;

  axios({
    method: 'get',
    url: 'https://api.openweathermap.org/data/2.5/weather',
    params: {
        lat: lat,
        lon: lon,
        appid: 'bb6f4f2dcd78f1a75094e8c20c2a2b10',
    
    }
    }).then(response => {
        document.getElementById("weathericon").src=`http://openweathermap.org/img/wn/${response.data.weather[0].icon}@2x.png`
      console.log(response.data)
    })

   
    let unix_timestamp = 1674704816
    let datetime = new Date(unix_timestamp*10)
    console.log(datetime)
    
}
// console.log(data)


// const displaytempature = temperature =>{
// setInnerText('weathericon', data.weather[0].icon)
// console.log(temperature)

// }




// --------Dont forget to establish variables to call------



    