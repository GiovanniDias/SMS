<template>
  <div id="app">
    <my-toolbar></my-toolbar>
    <router-view/>
  </div>
</template>

<script>
import myToolbar from './components/Toolbar'
export default {
  name: 'App',
  components: {myToolbar},
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
