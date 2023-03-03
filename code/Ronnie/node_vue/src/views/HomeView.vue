<template>
  <div class="home">
    <NavBar></NavBar>
    <main>
      <div v-for="pokemon in pokedex" :key="pokemon.number"><img :src="pokemon.img_url"><h2>{{ pokemon.name }}</h2></div>
    </main>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import Pokemon from '@/assets/pokemon.json'
import NavBar from '@/components/NavBar.vue'

export default {
  name: 'HomeView',
  components: {
    NavBar
  },
  data(){
    return {
      pokedex: [],
      sortby: "name",
      search: "",
    }
  },

  created(){
    let value = Pokemon.pokemon
    for(let i=0; i < value.length; ++i){
      this.pokedex.push({
        number: value[i].number,
        img_url: value[i].image_front,
        name: value[i].name,
      })
    }
  }
}
</script>
