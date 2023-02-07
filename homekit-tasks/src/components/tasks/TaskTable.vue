<script setup>
defineProps({
  data: {
    type: Array,
    required: true,
  },
});
</script>

<template>
  <table class="table">
    <thead>
      <th>#</th>
      <th>Description</th>
    </thead>
    <tbody>
      <tr v-for="task in data" :key="task.id">
        <td>{{ task.id }}</td>
        <td>{{ task.description }}</td>
      </tr>
    </tbody>
  </table>
</template>
