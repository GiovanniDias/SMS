<template>
  <div>
    <v-content>
      <v-container mt-5>
        <div class="grey lighten-3 board">
          <v-card>
            <v-container fluid grid-list-lg>
              <v-layout row wrap>
                <v-flex xs12 sm6 v-for="(item, index) in items" :key="index">
                  <v-card :color="item.color" class="white--text">
                    <v-card-title primary-title>
                      <div class="headline">{{ item.title }}</div>
                      <div class="text-xs-left">{{ item.text }}</div>
                    </v-card-title>
                    <v-layout>
                      <v-flex text-xs-right>
                        <v-btn dark :to="item.route">Acessar</v-btn>
                      </v-flex>
                    </v-layout>
                  </v-card>
                </v-flex>
              </v-layout>
            </v-container>
          </v-card>
        </div>
      </v-container>
    </v-content>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [
        {
          title: "Cursos",
          text: "Acesse para gerenciar todas as informações sobre os cursos.",
          color: "blue darken-3",
          route: {name: "Courses"}
        },
        {
          title: "Alunos",
          text: "Acesse para gerenciar as informações sobre os alunos matriculados.",
          color: "red darken-2",
          route: {name: "Students"}
        },
      ]
    };
  }
};
</script>

<style>
.board {
  max-width: 800px;
  margin: auto;
}
</style>