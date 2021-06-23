<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import home from "./views/Home.vue";
export default {
  name: "app",
  components: {
    home,
  },
};
</script>

<style>
@import "./assets/css/normalize.css";
</style>
