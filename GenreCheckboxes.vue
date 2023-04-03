<template>
  <div>
    <div v-for="genre in genres" :key="genre.id">
      <input type="checkbox" :id="genre.id" :value="genre.id" v-model="selectedGenres">
      <label :for="genre.id">{{ genre.name }}</label>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    genres: Array
  },
  data() {
    return {
      selectedGenres: []
    }
  }
}
</script>