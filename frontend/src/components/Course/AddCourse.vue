<template>
  <v-app>
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-card class="elevation-12">
              <v-toolbar dark color="primary">
                <v-toolbar-title>Adicionar Curso</v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <form>
                  <v-text-field
                      v-model="code"
                      :error-messages="codeErrors"
                      :counter="10"
                      label="Código"
                      required
                      @input="$v.code.$touch()"
                      @blur="$v.code.$touch()"
                  ></v-text-field>
                  <v-text-field
                      v-model="name"
                      :error-messages="nameErrors"
                      :counter="50"
                      label="Nome"
                      required
                      @input="$v.name.$touch()"
                      @blur="$v.name.$touch()"
                  ></v-text-field>
                  <v-text-field
                      v-model="hourly_load"
                      :error-messages="hoursErrors"
                      label="Carga Horária"
                      required
                      @input="$v.hourly_load.$touch()"
                      @blur="$v.hourly_load.$touch()"
                  ></v-text-field>

                  <v-btn color="success" @click="submit">Adicionar</v-btn>
                  <v-btn color="error" dark @click="clear">Limpar</v-btn>
                </form>
              </v-card-text>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
  import { validationMixin } from 'vuelidate'
  import { required, maxLength, email } from 'vuelidate/lib/validators'

  export default {
    mixins: [validationMixin],

    validations: {
      code: { required, maxLength: maxLength(10) },
      name: { required, maxLength: maxLength(50) },
      hourly_load: { required },
    },

    data: () => ({
      code: '',
      name: '',
      hourly_load: '',
    }),

    computed: {
      nameErrors () {
        const errors = []
        if (!this.$v.name.$dirty) return errors
        !this.$v.name.maxLength && errors.push('Name must be at most 10 characters long')
        !this.$v.name.required && errors.push('Name is required.')
        return errors
      },
      codeErrors () {
        const errors = []
        if (!this.$v.code.$dirty) return errors
        !this.$v.code.code && errors.push('Must be valid code')
        !this.$v.code.required && errors.push('Code is required')
        return errors
      },
      hoursErrors () {
        const errors = []
        if (!this.$v.hourly_load.$dirty) return errors
        !this.$v.hourly_load.hourly_load && errors.push('Must be valid value')
        !this.$v.hourly_load.required && errors.push('Hours is required')
        return errors
      }
    },

    methods: {
      submit () {
        this.$v.$touch()
      },
      clear () {
        this.$v.$reset()
        this.name = ''
        this.email = ''
        this.select = null
        this.checkbox = false
      }
    }
  }
</script>