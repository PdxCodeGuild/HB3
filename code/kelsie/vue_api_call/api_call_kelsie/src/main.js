import { createApp } from 'vue'
import App from './App.vue'

import './assets/main.css'

createApp(App).mount('#app')
console.log("hello")

let request = new XMLHttpRequest();
request.open("GET", "https://api.nasa.gov/planetary/apod?api_key=p8hRjmprXgS5dFGTD2HMmCEiMq1rAXcBCzCaqhLM");
request.send();
request.onload = () => {
    console.log(request);
    if (request.status === 200) {
        message = (JSON.parse(request.response));
        return message;
    } else {
        return ('error')
    }
}

