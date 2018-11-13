<template>
  <v-container>
    <v-layout>
      <v-flex>
        <v-data-table
          :headers="headers"
          :items="items"
          class="elevation-2"
        >
          <template slot="items" slot-scope="props">
            
            <td class="text-xs-left"
              v-for="(attribute, a) of props.item" :key="a"
            > {{ attribute }} </td>

          </template>
        </v-data-table>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  export default {
    name: 'List',
    props: ['headers', 'items'],
  }
</script>