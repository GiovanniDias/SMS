<template>
  <v-container grid-list-md>
    <v-layout wrap>
      <v-flex xs12 sm2>
        <v-text-field v-model="item.code" label="Código"></v-text-field>
      </v-flex>
      <v-flex xs12 sm7>
        <v-text-field v-model="item.name" label="Nome do Curso"></v-text-field>
      </v-flex>
      <v-flex xs12 sm3>
        <v-text-field v-model="item.hourly_load" label="Carga Horária"></v-text-field>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  props: ['item']
}
</script>
