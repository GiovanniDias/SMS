<template>
  <v-data-table
    :headers="headers"
    :items="items"
    class="elevation-2"
  >
    <template slot="items" slot-scope="props">
      <td class="text-xs-left"> {{ props.item.code }} </td>
      <td class="text-xs-left"> {{ props.item.name }} </td>
      <td class="text-xs-left"> {{ props.item.cpf }} </td>
      <td class="text-xs-left"> {{ props.item.email }} </td>
      <td class="text-xs-left"> {{ props.item.phone }} </td>
      <td class="text-xs-left"> {{ props.item.course.name }} </td>
      <td class="text-xs-left">
        <v-icon small class="mr-2" @click="editItem(props.item)">edit</v-icon>
        <v-icon small @click="deleteItem(props.item)">delete</v-icon>
      </td>
    </template>
  </v-data-table>
</template>

<script>
export default {
  name: "StudentList",
  props: ["headers", "items", "editItem", "deleteItem"]
};
</script>
