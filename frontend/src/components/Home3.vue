<template>
  <div>
    <v-layout>
      <v-flex >
        <list :headers="course_headers" :items="courses"></list>
      </v-flex>
      <v-flex>
        <list :headers="student_headers" :items="students"></list>
      </v-flex>
    </v-layout>
    
  </div>
</template>

<script>
import List from "./Course/List";
export default {
  name: "Home",
  components: { List },
  data() {
    return {
      course_headers: [
          { text: 'Código', value: 'code', align: 'left' },
          { text: 'Nome', value: 'name' },
          { text: 'Carga Horária', value: 'hourly_load' },
          { text: 'Data de Cadastro', value: 'register_date' },
        ],
      courses: [
        { code: 'C01', name: 'ADM', hourly_load: 120, register_date: '20/10/2008' },
        { code: 'C02', name: 'DIR', hourly_load: 160, register_date: '20/10/2009' },
        { code: 'C03', name: 'MED', hourly_load: 240, register_date: '20/10/2006' },
      ],
      student_headers: [
        { text: 'Código', value: 'code', align: 'left' },
        { text: 'Nome', value: 'name' },
        { text: 'CPF', value: 'cpf' },
        { text: 'Curso', value: 'course' },
        ],
      students: [
        { code: 'A01', name: 'Pedro', cpf: 12345678910, course: 'Administração' },
        { code: 'A02', name: 'Amanda', cpf: 12345678912, course: 'Direito' },
        { code: 'A03', name: 'Fernando', cpf: 12345678911, course: 'Medicina' },
        { code: 'A04', name: 'Maria', cpf: 12345678906, course: 'Administração' },
        { code: 'A05', name: 'João', cpf: 12345678917, course: 'Direito' },
        { code: 'A06', name: 'José', cpf: 12345678915, course: 'Administração' },
        { code: 'A07', name: 'Francisca', cpf: 12345678665, course: 'Administração' },
      ],
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
