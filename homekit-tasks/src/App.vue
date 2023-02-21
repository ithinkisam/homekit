<script setup>
import { ref, computed } from "vue";
import PrimaryNav from "./components/nav/PrimaryNav.vue";
import Home from "./components/Home.vue";
import Tasks from "./components/tasks/Tasks.vue";
import Spend from "./components/Spend.vue";
import Menu from "./components/Menu.vue";
import Inventory from "./components/Inventory.vue";
import NotFound from "./components/NotFound.vue";

const routes = {
  "/": Home,
  "/tasks": Tasks,
  "/spend": Spend,
  "/menu": Menu,
  "/inventory": Inventory,
};

const currentPath = ref(window.location.hash);

window.addEventListener("hashchange", () => {
  currentPath.value = window.location.hash;
});

const currentView = computed(() => {
  return routes[currentPath.value.slice(1) || "/"] || NotFound;
});
</script>

<template>
  <div>
    <div class="container-fluid">
      <div class="row flex-nowrap">
        <PrimaryNav />
        <div class="col py-3">
          <component :is="currentView" />
        </div>
      </div>
    </div>
  </div>
</template>

<style>
#app {
  font-family: Roboto, Helvetica, Arial, sans-serif;
}
</style>
