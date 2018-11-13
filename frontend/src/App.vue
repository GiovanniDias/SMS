<template>
  <div id="app">
    <v-app>
      <my-toolbar app></my-toolbar>
      <router-view/>
      <v-footer app fixed dark>Copyright 2018</v-footer>
    </v-app>
  </div>
</template>

<script>
import myToolbar from "./components/Toolbar";
export default {
  name: "App",
  components: { myToolbar }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
