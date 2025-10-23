<template>
  <header>
    <h1>{{ title }}</h1>
    <AppButton
      v-show="homePage"
      @btn-click="$emit('toggle-add-task')"
      :text="showAddTask ? 'Close' : 'Add Task'"
      :color="showAddTask ? 'red' : 'green'"
    />
  </header>
</template>

<script setup>
import { computed, defineProps, defineEmits } from "vue";
import { useRoute } from "vue-router";
import AppButton from "./AppButton";

const route = useRoute();

defineProps({
  title: String,
  showAddTask: Boolean,
});

const homePage = computed(() => {
  return route.path === "/";
});

defineEmits(["toggle-add-task"]);
</script>

<style scoped>
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}
</style>
