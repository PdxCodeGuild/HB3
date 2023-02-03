import { createApp } from 'vue'
import App from './App.vue'
import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
       posts: [],
     },
   })
   
import './assets/main.css'

createApp(App).mount('#app')
console.log("hello")


    let request = new XMLHttpRequest();
    request.open("GET", "https://api.nasa.gov/planetary/apod?api_key=p8hRjmprXgS5dFGTD2HMmCEiMq1rAXcBCzCaqhLM");
    request.send();
    request.onload = () => {
    if (request.status === 200) {
        let Message = (JSON.parse(request.response));
        console.log(Message);
        
    } else {
        return ('error')
    }
}



