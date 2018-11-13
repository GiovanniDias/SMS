<template>
  <v-toolbar>

    <v-spacer></v-spacer>

    <v-toolbar-items>
      <my-menu :menuTitle="Cursos"></my-menu>
      <my-menu :menuTitle="Alunos"></my-menu>
      <v-btn flat>Exportar</v-btn>
    </v-toolbar-items>
  </v-toolbar>
</template>

<script>
import myMenu from './Menu'
export default {
  components: {myMenu}
}
</script>
