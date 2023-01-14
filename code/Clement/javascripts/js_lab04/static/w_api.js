function titleCase(str) {
  word_list = str.toLowerCase().split(' ')
  for(let i = 0; i < word_list.length; ++i){
      word_list[i] = word_list[i].charAt(0).toUpperCase() + word_list[i].slice(1)
  }
  return word_list.join(' ')
}

window.addEventListener("load", () => {
  let lon;
  let lat;

  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition((position) => {
      lat = position.coords.latitude;
      lon = position.coords.longitude;

        // console.log(lat);
        // console.log(long);
      const url =
        `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${Weather_API}&units=metric`;

      axios.get(url)
      .then((response) => {
        document.getElementById('location').innerText = response.data.name;
        document.getElementById('time').innerHTML = response.data.timezone;
        document.getElementById('visibility').innerHTML = "<p>" + response.data.visibility + "<span>%</span></p>";
        document.getElementById('wind').innerHTML = "<p>" + response.data.wind.speed+ "<span>mph</span></p>";
        document.getElementById('pressure').innerHTML = "<p>" + response.data.main.pressure + "<span>in</span></p>";
        document.getElementById('humidity').innerHTML = "<p>" +response.data.main.humidity+ "<span>mi</span></p>";

        document.getElementById('feels_like').innerHTML = "<p>" + response.data.main.feels_like + "<span>&#176C</span></p>";


        document.getElementById('temp').innerHTML = "<p>" + response.data.main.temp + "<span>&#176C</span></p>";
        document.getElementById('Latitude').innerText = response.data.coord.lat;
        document.getElementById('Longitude').innerText = response.data.coord.lon;
        document.getElementById('climate').innerHTML = titleCase(response.data.weather[0].description);


      });
    });
  }
});


