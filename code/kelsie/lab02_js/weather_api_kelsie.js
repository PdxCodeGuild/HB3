

let request = new XMLHttpRequest();  
request.open("GET", 'https://api.openweathermap.org/data/2.5/weather?lat=33.441792&lon=-94.037689& exclude=hourly,daily&appid=a6f0df8a96cd8ffba804f42ffdf0f855');
request.responseType = 'json'
request.send();
request.onload = ()=>{
    info = (request.response)
    x = JSON.parse(info)
    document.body.innerHTML = x['weather']
}