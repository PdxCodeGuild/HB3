
let app = new Vue({
    el: '#grocery_list_app'
    data: {
        list: []
    },

    methods: {
        add_grocery_item: function () {
            const add_grocery_item = document.querySelector('#grocery_item').value;
            console.log(add_grocery_item)
            if (!add_grocery_item) {
                return
            }
            this.list.push({
                id: Date.now(),
                title: add_grocery_item
            })
            document.querySelector("grocery_item").value = ''
        }
    },

})
