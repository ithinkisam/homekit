<template>
  <div v-for="task in tasks" :key="task.id">
    <AppTask
      @toggle-reminder="$emit('toggle-reminder', task.id)"
      @delete-task="$emit('delete-task', task.id)"
      :task="task"
    />
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from "vue";
import AppTask from "./AppTask";

defineProps({
  tasks: Array,
});
defineEmits(["toggle-reminder", "delete-task"]);
</script>
