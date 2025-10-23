<template>
  <div class="container">
    <AppHeader
      @toggle-add-task="toggleAddTask"
      :showAddTask="showAddTask"
      title="Task Tracker"
    />
    <router-view :showAddTask="showAddTask"></router-view>
    <AppFooter />
  </div>
</template>

<script setup>
import { ref } from "vue";
import AppHeader from "./components/AppHeader";
import AppFooter from "./components/AppFooter";

const showAddTask = ref(false);
const toggleAddTask = () => {
  showAddTask.value = !showAddTask.value;
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;400&display=swap");

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: "Poppins", sans-serif;
}

.container {
  max-width: 500px;
  margin: 30px auto;
  overflow: auto;
  min-height: 300px;
  border: 1px solid steelblue;
  padding: 30px;
  border-radius: 5px;
}

.btn {
  display: inline-block;
  background: #000;
  color: #fff;
  border: none;
  padding: 10px 20px;
  margin: 5px;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
  font-size: 15px;
  font-family: inherit;
}

.btn:focus {
  outline: none;
}

.btn:active {
  transform: scale(0.98);
}

.btn-block {
  display: block;
  width: 100%;
}
</style>
