<template>
  <div>
    <v-container>
      <v-layout>
        <v-flex>
          <v-toolbar color="white" class="elevation-1">
            <v-toolbar-title>{{ session }}</v-toolbar-title>
            <v-divider class="mx-3" inset vertical></v-divider>
            <v-spacer></v-spacer>
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
          </v-toolbar>

          <course-list
            v-if="session=='Cursos'"
            :items="items" :headers="headers"
            :editItem="editItem" :deleteItem="deleteItem"
          ></course-list>
          <student-list 
            v-else
            :items="items" :headers="headers"
            :editItem="editItem" :deleteItem="deleteItem"
          ></student-list>

        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import CourseList from "./CourseList";
import StudentList from "./StudentList";
import CourseFields from "./CourseFields";
import StudentFields from "./StudentFields";
export default {
  components: {
    CourseList,
    StudentList,
    CourseFields,
    StudentFields
  },
  props: ["session", "headers", "items"],
  data: () => ({
    dialog: false,
    editedIndex: -1,
    editedItem: {},
    defaultItem: {}
  }),
  created() {
    if (this.session == "Cursos") {
      this.editedItem = { code: "", name: "", hourly_load: 0 };
      this.defaultItem = { code: "", name: "", hourly_load: 0 };
    } else {
      this.editedItem = {
        code: "", name: "", cpf: "",
        email: "", phone: "",
        cep: "", address: "",
        number: "", complement: "",
        course: { name: "" }
      };
      this.defaultItem = {
        code: "", name: "", cpf: "",
        email: "", phone: "",
        cep: "", address: "",
        number: "", complement: "",
        course: { name: "" }
      };
    }
  },
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
  methods: {
    editItem(item) {
      this.editedIndex = this.items.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      const index = this.items.indexOf(item);
      confirm("Tem certeza que deseja remover este item?") &&
        this.items.splice(index, 1);
    },
    close() {
      this.dialog = false;
      setTimeout(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      }, 300);
    },
    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.items[this.editedIndex], this.editedItem);
      } else {
        this.items.push(this.editedItem);
      }
      this.close();
    }
  }
};
</script>