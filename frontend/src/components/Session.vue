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
import axios from 'axios';
export default {
  name: "Session",
  components: { CrudList },
  data() {
    return {
      headers: [],
      items: [
        { code: 'A01', name: 'Pedro', cpf: 12345678910, course: 'Administração' },
        { code: 'A02', name: 'Amanda', cpf: 12345678912, course: 'Direito' },
        { code: 'A03', name: 'Fernando', cpf: 12345678911, course: 'Medicina' },
        { code: 'A04', name: 'Maria', cpf: 12345678906, course: 'Administração' },
        { code: 'A05', name: 'João', cpf: 12345678917, course: 'Direito' },
        { code: 'A06', name: 'José', cpf: 12345678915, course: 'Administração' },
        { code: 'A07', name: 'Francisca', cpf: 12345678665, course: 'Administração' },
      ],
    };
  },
  created: function(){
    var route = this.$route.name;
    if(route == 'Courses'){
      this.session = 'Cursos';
      this.headers = [
        { text: 'Código', value: 'code', align: 'left' },
        { text: 'Nome', value: 'name' },
        { text: 'Carga Horária', value: 'hourly_load' },
        { text: 'Data de Cadastro', value: 'register_date' },
        { text: 'Ações', value: 'actions', sortable: false, align: 'left' }
      ];
      this.getCourses();
    }
    else if(route == 'Students'){
      this.session = 'Alunos';
      this.headers = [
        { text: 'Código', value: 'code', align: 'left' },
        { text: 'Nome', value: 'name' },
        { text: 'CPF', value: 'cpf' },
        { text: 'Curso', value: 'course' },
        { text: 'Ações', value: 'actions', sortable: false, align: 'left' }
      ];
      this.getStudents();
    }
  },
  methods: {
    getCourses(){
      axios({
        method:'get',
        url:'http://localhost:8000/api/courses/',
      }).then(function(response){
        console.log(response.data);
      })
    },
    getStudents(){

    }
  }
};
</script>
