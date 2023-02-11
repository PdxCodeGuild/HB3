axios({
  method: 'get',
  url: 'https://geo.ipify.org/api/v2/country,city?apiKey=at_0ysqPFL6xBJJySmNt5IZnM6DpsIdn&ipAddress=8.8.8.8'
}).then((response) => {
  console.log(response.data)
})

navigator.geolocation.getCurrentPosition(position => {
  console.log(position.coords.latitude)
  console.log(position.coords.longitude)
  axios({
    method: 'get',
    url: 'https://api.openweathermap.org/data/2.5/weather',
    // There was a question mark in the orginal url, after weather, after that I removed the question mark and replaced the "=" to ":" for the parameters
    params:{
      lat: position.coords.latitude,
      lon: position.coords.longitude,
      // exclude: hourly,
      appid: ,
      // I have moved my api key to the secret.js.gitignore file
    }
  
  }).then((response) => {
    console.log(response.data)
  })
  
  console.log({"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"})
  
  let unix_timestamp = 1592482891
  let datetime = new Date(unix_timestamp*1000)
  console.log(datetime) // Thu Jun 18 2020 05:21:31 GMT-0700 (Pacific Daylight Time)
})