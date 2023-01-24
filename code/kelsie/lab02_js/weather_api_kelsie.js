
function getWeather(){
            
    navigator.geolocation.getCurrentPosition(position => {
        console.log(position.coords.latitude)
        console.log(position.coords.longitude)
        let url = 'https://api.openweathermap.org/data/2.5/weather?lat='+position.coords.latitude+'&lon='+position.coords.longitude+'&units=imperial& exclude=hourly,daily&appid='+key
        
        fetch(url, {
        method: 'GET', 
        headers: {
 
        },
           
        }).then(response => {
        if (!response.ok) {
            throw response; 
        }
        
        return response.json(); 

        }).then(response => {
        
        console.log(response)
        processWeatherData(response);

        }).catch((errorResponse) => {
        if (errorResponse.text) { 
            errorResponse.text().then( errorMessage => {
                errorResponse.text()
            })
        } else {

        } 
        });

    function processWeatherData(response) {
  
        var location=response.name;
        var weather=response.weather[0].main;
        var humidity=response.main.humidity
        var temp=response.main.temp;
        var feels_like=response.main.feels_like;
        var max=response.main.temp_max
        var min=response.main.temp_min
        var clouds=response.clouds.all
        var wind=response.wind.speed
        var icon_id = response.weather[0].icon
        var description=response.weather[0].description
        var timestamp=response.dt;
        let date= new Date(timestamp*1000)
        datetime =date.toDateString()
        document.getElementById('icon').src = 'http://openweathermap.org/img/wn/'+icon_id+'.png'

        document.getElementById("location").innerHTML = ("In "+location+":")
        document.getElementById("temp").innerHTML = ("The tempurature is "+temp+" degrees Fahrenheit with a low of "+min+" and a high of "+max)
        document.getElementById("datetime").innerHTML = ("It is currently "+datetime)
        document.getElementById("weather").innerHTML = ("The weather today is "+weather+" ("+description+")")
        document.getElementById("feels_like").innerHTML = ("The tempurature feels like "+feels_like+" degrees Fahrenheit")
        document.getElementById("clouds").innerHTML = ("Cloud cover is "+clouds+"%")
        document.getElementById("humidity").innerHTML = ("The humidity is "+humidity+"%")
        document.getElementById("wind").innerHTML = ("Wind is "+wind+" mph")
        document.getElementById("description").innerHTML = (description)
        
      }
    })}
