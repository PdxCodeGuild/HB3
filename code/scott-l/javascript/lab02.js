

// let local = document.getElementById("location")

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
        return [lat_pos,long_pos] 

    })
    

}

function functionAPI_call() {

    navigator.geolocation.getCurrentPosition((position) => {
        console.log(position.coords.latitude)
        console.log(position.coords.longitude)

        let lat_pos = position.coords.latitude
        let long_pos = position.coords.longitude

        // console.log('https://api.openweathermap.org/data/2.5/weather?lat=33.441792&lon=-94.037689& exclude=hourly,daily&appid='+ API_key)
        axios({
       
            method: 'get',
            // url: 'https://api.openweathermap.org/data/2.5/weather?lat=33.441792&lon=-94.037689& exclude=hourly,daily&appid='+ API_key
            url: 'https://api.openweathermap.org/data/2.5/weather?lat='+lat_pos+'&lon='+long_pos+'& exclude=hourly,daily&appid='+ API_key
            // url: 'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={'+API_key+'}'
            // url: 'https://api.openweathermap.org'
            // url: 'https://icanhazdadjoke.com/',
            // headers: {'accept':'application/json'}

        }).then((response) => {
            let weather = response.data
            console.log(weather)
            

            document.getElementById('location').innerText = weather.name
            // document.getElementById('long_id').innerText = long_pos

            let unix_timestamp = weather.dt
            let datetime = new Date(unix_timestamp*1000)
            console.log(datetime) // Thu Jun 18 2020 05:21:31 GMT-0700 (Pacific Daylight Time)
            document.getElementById('date_posting').innerText = datetime


            let img_src = weather.weather[0].icon
            console.log(img_src)
            console.log('http://openweathermap.org/img/wn/'+img_src+'.png')
            let image_send= 'http://openweathermap.org/img/wn/'+img_src+'.png'
            console.log(image_send)
            document.getElementById('weather_img').src= 'http://openweathermap.org/img/wn/'+img_src+'.png'

            let weather_description = weather.weather[0].description
            console.log(weather_description)
            document.getElementById('weather_description').innerText = weather_description
            
    
        })


    })
  
    
    

}


