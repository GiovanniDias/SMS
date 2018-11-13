<template>
  <div v-if="outfit1">
    <v-toolbar dense dark>
      <v-btn flat :to="{ name: 'Home' }">Sistema de Gerenciamento de Alunos</v-btn>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <my-menu
          v-for="(title, i) in menu_titles" :key="i"
          :menuTitle="title"
        ></my-menu>

        <div style="width:50px"></div>
        <v-btn flat>Exportar</v-btn>
      </v-toolbar-items>
    </v-toolbar>
  </div>
  <div v-else>
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
import myMenu from "./Menu";
export default {
  components: { myMenu },
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
  text-decoration: none;
}
</style>