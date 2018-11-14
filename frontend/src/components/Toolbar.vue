<template>
  <div>
    <v-toolbar dark>
      <v-spacer></v-spacer>
      <v-toolbar-title class="white--text">
        <a @click="goHome" class="nolink">Sistema de Gerenciamento de Alunos</a>
      </v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>
  </div>
</template>

<script>
export default {
  data() {
    return {
      outfit1: false,
      menu_titles: ['Cursos', 'Alunos']
    };
  },
  methods:{
    goHome(){
      this.$router.push({name: 'Home'})
    }
  }
};
</script>

<style>
.nolink {
  text-decoration-color: white;
}
</style>