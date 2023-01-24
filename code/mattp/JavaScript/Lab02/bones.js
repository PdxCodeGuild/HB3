

console.log(Weather_API)

// window.addEventListener("load", function(){
//     let lat = 0
//     let lon = 0
//     if (navigator.geolocation) {
//         navigator.geolocation.getCurrentPosition(position => {
//             console.log(position.coords.latitude)
//             console.log(position.coords.longitude)
           
//             lat = position.coords.latitude;
//             lon = position.coords.longitude;
//             let weatherURL = `https://api.openweathermap.org/data/2.5/forecast?units=imperial&lat=${lat}&lon=${lon}&appid=${Weather_API}`; 
//             return weatherURL
//         })
//     }
// }) 



// async function getWeatherData() {
//     let position = await new
// }


window.addEventListener("load", () => {
    let lat = 0;
    let lon = 0;
    let units = "imperial"
  
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition((position) => {
        lat = position.coords.latitude;
        lon = position.coords.longitude;
  
            console.log(lat);
            console.log(lon);
        let Weather_URL =
          `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&exclude=hourly,daily&appid=${Weather_API}&units=${units}`;

        console.log(Weather_URL)

        axios(Weather_URL)
          .then((response) => {

            console.log("temp")
            document.getElementById('weather').innerText = "Current weather:  " + response.data.weather[0].description
            document.getElementById('temp').innerHTML = "Current temp (F):  " + response.data.main.temp
            document.getElementById('visibility').innerHTML = "Current visibility (ft):  " + response.data.visibility
            document.getElementById('wind').innerHTML = "Current wind (mph):  " + response.data.wind.speed
            document.getElementById('clouds').innerHTML = "Current cloud coverage (%):  " + response.data.main.pressure
            document.getElementById('humidity').innerHTML = "Current humidity (rel %):  " + response.data.main.humidity
            document.getElementById('feels_like').innerHTML = "Currently feels like (F):  " + response.data.main.feels_like
            
            document.getElementById('sunrise').innerHTML = "Current Sunrise (sec):  " + response.data.sys.sunrise
                let sunrise_time = response.data.sys.sunrise 
                let datetime = new Date(sunrise_time*1000)
                console.log(datetime) // Thu Jun 18 2020 05:21:31 GMT-0700 (Pacific Daylight Time)
            // console.log(temp)
            document.getElementById('datetime').innerHTML = "Sunrise:  " + datetime

            document.getElementById('icon').innerHTML = "Weather Icon Code:  " + response.data.weather[0].icon
              let icon = response.data.weather[0].icon
              let icon_image = `http://openweathermap.org/img/wn/${icon}.png`
              document.getElementById('icon_image').innerHTML = `<img src="http://openweathermap.org/img/wn/${icon}.png"/>`
                console.log(icon)
            
          });
        });
      }
    });

