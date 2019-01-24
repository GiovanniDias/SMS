<template>
  <v-dialog v-model="dialog" max-width="600px">
    <v-btn slot="activator" color="primary" dark class="mb-2">Adicionar</v-btn>
    <v-card>
      <v-card-title>
        <span class="headline">{{ formTitle }}</span>
      </v-card-title>

      <v-card-text>
        <course-fields v-if="session=='Cursos'" :item="editedItem"></course-fields>
        <student-fields v-else :item="editedItem"></student-fields>
      </v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="error" outline @click.native="close">Cancelar</v-btn>
        <v-btn color="success" outline @click.native="save">Salvar</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import CourseFields from "./CourseFields";
import StudentFields from "./StudentFields";
export default {
  props: ["session", "save", "editedItem"],
  components: { CourseFields, StudentFields },

  computed: {
    formTitle() {
      if (this.session == "Cursos") {
        return this.editedIndex === -1 ? "Novo Curso" : "Editar Curso";
      }
      if (this.session == "Alunos") {
        return this.editedIndex === -1 ? "Novo Aluno" : "Editar Aluno";
      }
    }
  },
  watch: {
    dialog(val) {
      val || this.close();
    }
  },
  methods:{
    close() {
      this.dialog = false;
      setTimeout(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      }, 300);
    },
  }
};
</script>