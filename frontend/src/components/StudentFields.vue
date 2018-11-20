<template>
  <v-container grid-list-md>
    <v-layout wrap>
      <v-flex xs12 sm3>
        <v-text-field v-model="item.code" label="Código"></v-text-field>
      </v-flex>
      <v-flex xs12 sm9>
        <v-text-field v-model="item.name" label="Nome Completo"></v-text-field>
      </v-flex>
      <v-flex xs12 sm5>
        <v-text-field v-model="item.cpf" label="CPF"></v-text-field>
      </v-flex>
      <v-flex xs12 sm7>
        <v-select :items="courses" label="Curso"></v-select>
      </v-flex>
      <v-flex xs12 sm7>
        <v-text-field v-model="item.email" label="E-mail"></v-text-field>
      </v-flex>
      <v-flex xs12 sm5>
        <v-text-field v-model="item.phone" label="Telefone"></v-text-field>
      </v-flex>
      <v-flex xs12 sm3>
        <v-text-field v-model="item.cep" label="CEP"></v-text-field>
      </v-flex>
      <v-flex xs12 sm9>
        <v-text-field v-model="item.address" label="Endereço"></v-text-field>
      </v-flex>
      <v-flex xs12 sm2>
        <v-text-field v-model="item.number" label="Nº"></v-text-field>
      </v-flex>
      <v-flex xs12 sm10>
        <v-text-field v-model="item.complement" label="Complemento"></v-text-field>
      </v-flex>
      
      

    </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios'
export default {
  props: ["item"],
  data() {
    return{
      courses: [
        'ADM', 'DIR'
      ]
    }
  },
  watch: {
    'item.cep': function(){
      this.searchCep();
    }
  },
  methods:{
    searchCep() {
      var self = this;
      if (/^[0-9]{5}-[0-9]{3}$/.test(this.item.cep)) {
      axios({
        method: 'get',
        url: "https://viacep.com.br/ws/" + this.item.cep + "/json/",
      }).then(response => {
          var address = response.data;
          try{
            self.item.address = `${address.logradouro}, ${address.bairro}, ${address.localidade}-${address.uf}`;
          }catch(e){
            console.log(e);
          }
        });
      }
    },
  }
};
</script>