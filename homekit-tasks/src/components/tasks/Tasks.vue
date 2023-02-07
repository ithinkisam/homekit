<script setup>
import { tasks } from "../../data/tasks.json";
import TaskTable from "./TaskTable.vue";
</script>

<template>
  <div class="card">
    <div class="card-body">
      <h3>To-do list</h3>
      <TaskTable :data="tasks" />
    </div>
  </div>
</template>
