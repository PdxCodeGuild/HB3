<template>
    <nav>
      <div class="container">
        <router-link to="/"><h1>Pokedex</h1></router-link>
        <div class="menu_items">
          sort by:
          <select name="sort_by" id="sortby" class="sort">
            <option value="name">name</option>
            <option value="name">number</option>
          </select>
          <router-link to="/about">About</router-link>
        </div>
      </div>
    </nav>
</template>

<script>
export default {
  name: 'NavBar',

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  font-family: Arial, Helvetica, sans-serif;
}

.container {
  width: 90%;
}
</style>
