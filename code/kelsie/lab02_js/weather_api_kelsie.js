


    import $ from 'jquery';

    navigator.geolocation.getCurrentPosition(position => {
        lat =(position.coords.latitude)
        long = (position.coords.longitude)
    })
    
    
    let request = new XMLHttpRequest();
    const url = 'https://api.openweathermap.org/data/2.5/weather?lat='+lat+'&lon='+long+'& exclude=hourly,daily&appid={a6f0df8a96cd8ffba804f42ffdf0f855}'
    
    request.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            const response = JSON.parse(this.responseText);
            getElements(response);
        }
    };
    
    request.open("GET", url, true);
    request.send();
    
    function getElements(response) {
      $('.showHumidity').text('The humidity is ${response.main.humidity}%');
    }
    



