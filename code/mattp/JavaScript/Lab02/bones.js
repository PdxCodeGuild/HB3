console.log(Weather_API)

window.addEventListener("load", function(){
    let lat = 0
    let lon = 0
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position => {
            console.log(position.coords.latitude)
            console.log(position.coords.longitude)
           
            lat = position.coords.latitude;
            lon = position.coords.longitude;
            let weatherURL = `https://api.openweathermap.org/data/2.5/forecast?units=imperial&lat=${lat}&lon=${lon}&appid=${Weather_API}`; 
            return weatherURL
        })
    }
}) 

console.log(weatherURL)

// async function getWeatherData() {
//     let position = await new
// }



