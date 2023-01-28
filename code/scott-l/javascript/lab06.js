//lab06.js file


let app = new Vue({
    el: '#app',
    data: {
        message: 'hello world!'
        image_url: 'https://placekitten.com/200/200'
    },

    methods: {
        sayHello: function() {
            console.log(this.message)
        }
    },
    
    created: function() {
        console.log(this.message)
    }
})

