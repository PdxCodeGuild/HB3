<script setup>
defineProps({
  msg: {
    type: String,
    required: true,
  },
})
</script>

<template>
  <div class="hello">
    Hello World
    <button @click="fetchData">Click Me!</button>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
  methods: {
    getData() {
      let request = new XMLHttpRequest();
      request.open("GET", "https://api.nasa.gov/planetary/apod?api_key=p8hRjmprXgS5dFGTD2HMmCEiMq1rAXcBCzCaqhLM");
      request.send();
      request.onload = () => {
      if (request.status === 200) {
        let Message = (JSON.parse(request.response));
        this.msg = Message;
        
    } else {
        return ('error')
    }
    }
  }
};
</script>

<style scoped>
button {
	padding: 20px 60px;
	font-size: 18px;
}
</style>
    