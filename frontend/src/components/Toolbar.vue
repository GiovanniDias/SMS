<template>
  <v-toolbar dense dark>
    <a route :to="{name: 'Home'}">Sistema de Gerenciamento de Alunos</a>
    <v-spacer></v-spacer>
    <v-toolbar-items>
      <my-menu
        v-for="(title, i) in menu_titles" :key="i"
        :menuTitle="title"
      ></my-menu>

      <div style="width:50px"></div>
      <!-- <v-btn flat>Exportar</v-btn> -->
      <v-btn flat>Sair</v-btn>
    </v-toolbar-items>
  </v-toolbar>
</template>

<script>
import myMenu from './Menu'
export default {
  components: {myMenu},
  data(){
    return{
      // menu_titles: ['Cursos', 'Alunos']
      menu_titles: ['Menu1', 'Menu2']
    }
  }
}
</script>
