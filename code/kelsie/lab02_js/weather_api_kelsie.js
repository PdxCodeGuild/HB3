
    

lat = navigator.geolocation.getCurrentPosition(position => {
    console.log(position.coords.latitude);
 })
long = navigator.geolocation.getCurrentPosition(position => {
    console.log(position.coords.longitude);
 })



    


 let request = new XMLHttpRequest();  
 request.open("GET", 'https://api.openweathermap.org/data/2.5/weather?lat='+lat+'&lon='+long+'& exclude=hourly,daily&appid=a6f0df8a96cd8ffba804f42ffdf0f855');
 request.send();
 request.onload = ()=>{
     console.log(JSON.parse(request.response));
  
 }