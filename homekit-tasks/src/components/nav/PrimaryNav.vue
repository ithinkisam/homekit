<script setup>
import PrimaryNavItemSimple from "./PrimaryNavItemSimple.vue";
</script>

<template>
  <div
    class="d-flex flex-column flex-shrink-0 p-3 bg-light min-vh-100"
    style="width: 200px">
    <a href="/" class="d-flex align-items-center mb-3 link-dark text-decoration-none">
      <img id="navbar-logo" src="images/logo_full.png" alt="ithinkisam" height="50" />
    </a>
    <ul class="nav nav-pills flex-column mb-auto">
      <PrimaryNavItemSimple name="Homekit" href="#/">
        <font-awesome-icon icon="fa-solid fa-house" fixed-width class="pe-2" size="lg" />
        Homekit
      </PrimaryNavItemSimple>
      <PrimaryNavItemSimple href="#/tasks">
        <font-awesome-icon
          icon="fa-solid fa-list-check"
          fixed-width
          class="pe-2"
          size="lg" />
        Tasks
      </PrimaryNavItemSimple>
      <PrimaryNavItemSimple href="#/spend">
        <font-awesome-icon
          icon="fa-solid fa-comments-dollar"
          fixed-width
          class="pe-2"
          size="lg" />
        Spend
      </PrimaryNavItemSimple>
      <PrimaryNavItemSimple href="#/menu">
        <font-awesome-icon
          icon="fa-solid fa-utensils"
          fixed-width
          class="pe-2"
          size="lg" />
        Menu
      </PrimaryNavItemSimple>
      <PrimaryNavItemSimple href="#/inventory">
        <font-awesome-icon
          icon="fa-solid fa-boxes-stacked"
          fixed-width
          class="pe-2"
          size="lg" />
        Inventory
      </PrimaryNavItemSimple>
    </ul>

    <!-- <hr />
    <BDropdown label="Color mode" class="pb-5">
      <li>
        <a class="dropdown-item" data-bs-theme-value="light" href="#">
          <font-awesome-icon icon="fa-regular fa-sun" fixed-width></font-awesome-icon
          >Light</a
        >
      </li>
      <li>
        <a class="dropdown-item" data-bs-theme-value="dark" href="#">
          <font-awesome-icon icon="fa-regular fa-moon" fixed-width></font-awesome-icon
          >Dark</a
        >
      </li>
      <li>
        <a class="dropdown-item" data-bs-theme-value="auto" href="#">
          <font-awesome-icon icon="fa-solid fa-circle-half-stroke" fixed-width />Auto</a
        >
      </li>
    </BDropdown> -->
  </div>
</template>
