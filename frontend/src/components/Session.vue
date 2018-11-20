<template>
  <div>
    <v-layout>
      <v-flex >
        <crud-list :session="session" :headers="headers" :items="items"></crud-list>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import CrudList from "./CrudList";
import axios from "axios";
export default {
  name: "Session",
  components: { CrudList },
  data() {
    return {
      headers: [],
      items: [],
      session: ""
    };
  },
  created: function() {
    var route = this.$route.name;
    if (route == "Courses") {
      this.session = "Cursos";
      this.headers = [
        { text: "Código", value: "code", align: "left" },
        { text: "Nome", value: "name" },
        { text: "Carga Horária", value: "hourly_load" },
        { text: "Data de Cadastro", value: "register_date" },
        { text: "Ações", value: "actions", sortable: false, align: "left" }
      ];
      this.getCourses();
    } else if (route == "Students") {
      this.session = "Alunos";
      this.headers = [
        { text: "Código", value: "code", align: "left" },
        { text: "Nome", value: "name" },
        { text: "CPF", value: "cpf" },
        { text: "Curso", value: "course" },
        { text: "Ações", value: "actions", sortable: false, align: "left" }
      ];
      this.getStudents();
    }
  },
  methods: {
    getCourses() {
      var self = this;
      axios({
        method: "get",
        url: "http://localhost:8000/api/courses/"
      }).then(function(response) {
        console.log(response.data);
        self.items = response.data;
      });
    },
    getStudents() {
      var self = this;
      axios({
        method: "get",
        url: "http://localhost:8000/api/students/"
      }).then(function(response) {
        console.log(response.data);
        self.items = response.data;
      });
    }
  }
};
</script>
