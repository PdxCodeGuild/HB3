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
  
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition((position) => {
        lat = position.coords.latitude;
        lon = position.coords.longitude;
  
            console.log(lat);
            console.log(lon);
        let Weather_URL =
          `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&exclude=hourly,daily&appid=${Weather_API}`;

        console.log(Weather_URL)

        axios({Weather_URL})
          .then((response) => {
            document.getElementById('main').innerText = response.data.name;
            document.getElementById('temp').innerHTML = response.data.main.temp
            document.getElementById('visibility').innerHTML = response.data.visibility
            document.getElementById('wind').innerHTML = response.data.wind.speed
            document.getElementById('clouds').innerHTML = response.data.main.pressure
            document.getElementById('humidity').innerHTML = response.data.main.humidity
            document.getElementById('feels_like').innerHTML = response.data.main.feels_like
            
            document.getElementById('sunrise').innerHTML = response.data.sys.sunrise
                    let unix_timestamp = sunrise
                    let datetime = new Date(sunrise*1000)
                    console.log(datetime) // Thu Jun 18 2020 05:21:31 GMT-0700 (Pacific Daylight Time)
            console.log(temp)
    
          });
        });
      }
    });

