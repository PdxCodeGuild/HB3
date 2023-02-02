<script>
import ToDoItem from "./components/ToDoItem.vue";


export default {
  name: "app",
  components: {
    ToDoItem,
  },
};


</script>

<template>
  <div id="app">
    <h1>To-Do List</h1>
    <ul>
      <li>
        <to-do-item label=" My ToDo Item" :done="true"></to-do-item>
        <span>{{message}}</span>
      </li>
    </ul>
  </div>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
