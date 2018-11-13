<template>
  <v-menu transition="slide-y-transition" bottom>
    <v-btn flat slot="activator" color="primary">
      {{ menuTitle }}
    </v-btn>
    <v-list>
      <v-list-tile v-for="(item, i) in items" :key="i">
        <v-list-tile-title>{{ item.title }}</v-list-tile-title>
      </v-list-tile>
    </v-list>
  </v-menu>
</template>

<script>
  export default {
    props: ['menuTitle'],
    data(){
      return {
        items: [
          { title: 'Click Me' },
          { title: 'Click Me' },
          { title: 'Click Me' },
          { title: 'Click Me 2' }
        ]
      }
    },
  }
</script>