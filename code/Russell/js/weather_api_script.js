const timeEl = document.getElementById('time');
const dateEl = document.getElementById('date');
const currentWeatherItemsEl = document.getElementById('current-weather-items');
const locationEl = document.getElementById('location');
const countryEl = document.getElementById('country');
const currentTempEl = document.getElementById('current-temp');


const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


getWeather()
function getWeather() {
    navigator.geolocation.getCurrentPosition((success) => {
        console.log(success);

        let {latitude, longitude} = success.coords;

        fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&appid=${Weather_API}&units=imperial`).then(res => res.json()).then(data => {

        console.log(data)
        showWeatherData(data);
        })
    })
}


function showWeatherData(data) {
    let {humidity, pressure, temp_max, temp_min, feels_like} = data.main;
    let {lat, lon} = data.coord;
    let {country} = data.sys;
    let unix_timestamp = data.dt;
    let datetime = new Date(unix_timestamp*1000);
    console.log(datetime);
    
    const minutes = datetime.getMinutes();
    console.log(minutes)
    const hour = datetime.getHours();
    console.log(hour)
    const day = datetime.getDay();
    console.log(day)
    const date = datetime.getDate();
    console.log(date)
    const month = datetime.getMonth();
    
    timeEl.innerHTML = (hour < 10? '0' + hour: hour >=13? hour%12 : hour) + ':' + (minutes < 10? '0' + minutes: minutes) + ' ' + '<span id="am-pm">PM</span>'
    
    dateEl.innerHTML = days[day] + ', ' + date + ' ' + months[month]
    
    
    locationEl.innerHTML = data.name + ', ' + country;
    countryEl.innerHTML = lat + 'N' + ', ' + lon + 'E';
    currentTempEl.innerHTML = 
    `<img
    src="http://openweathermap.org/img/wn/${data.weather[0].icon}@2x.png"
    alt="weather icon"
    class="w-icon"
  />
  <div class="others">
    <div id="title">Current Temp</div>
    <div id="attribute">${feels_like}&#176; F</div>
  </div>`;

    currentWeatherItemsEl.innerHTML =
    `<div class="weather-item">
    <div>Humidity</div>
    <div>${humidity}</div>
  </div>

  <div class="weather-item">
    <div>Pressure</div>
    <div>${pressure}</div>
  </div>

  <div class="weather-item">
    <div>Hi</div>
    <div>${temp_max}</div>
  </div>
  
  <div class="weather-item">
    <div>Lo</div>
    <div>${temp_min}</div>
  </div>

  `;
}