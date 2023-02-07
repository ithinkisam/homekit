<script setup>
import PrimaryNavItemSimple from "./PrimaryNavItemSimple.vue";
import BDropdown from "../bootstrap/BDropdown.vue";
</script>

<template>
  <nav class="navbar mb-3">
    <div class="container">
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="offcanvas"
        data-bs-target="#offcanvasNavbar"
        aria-controls="offcanvasNavbar">
        <font-awesome-icon icon="fa-solid fa-bars" size="xl" />
      </button>

      <a class="navbar-brand" href="/">
        <img src="images/logo_icon_small.png" alt="ithinkisam" height="50" />
      </a>
      <div
        class="offcanvas offcanvas-start"
        data-bs-scroll="true"
        tabindex="-1"
        id="offcanvasNavbar"
        aria-labelledby="offcanvasNavbarLabel">
        <div class="offcanvas-header">
          <h5 class="offcanvas-title" id="offcanvasNavbarLabel">
            <img
              id="navbar-logo"
              src="images/logo_full_dark.png"
              alt="ithinkisam"
              height="80" />
          </h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="offcanvas"
            aria-label="Close"></button>
        </div>
        <div class="offcanvas-body">
          <ul class="navbar-nav justify-content-start flex-grow-1 pe-3">
            <PrimaryNavItemSimple href="#/" class="h3">Homekit</PrimaryNavItemSimple>
            <PrimaryNavItemSimple href="#/tasks">Tasks</PrimaryNavItemSimple>
            <PrimaryNavItemSimple href="#/spend">Spend</PrimaryNavItemSimple>
            <PrimaryNavItemSimple href="#/menu">Menu</PrimaryNavItemSimple>
            <PrimaryNavItemSimple href="#/inventory">Inventory</PrimaryNavItemSimple>
          </ul>
          <div class="h-100">
            <BDropdown label="Color mode">
              <li>
                <a class="dropdown-item" data-bs-theme-value="light" href="#">
                  <font-awesome-icon
                    icon="fa-regular fa-sun"
                    fixed-width></font-awesome-icon
                  >Light</a
                >
              </li>
              <li>
                <a class="dropdown-item" data-bs-theme-value="dark" href="#">
                  <font-awesome-icon
                    icon="fa-regular fa-moon"
                    fixed-width></font-awesome-icon
                  >Dark</a
                >
              </li>
              <li>
                <a class="dropdown-item" data-bs-theme-value="auto" href="#">
                  <font-awesome-icon
                    icon="fa-solid fa-circle-half-stroke"
                    fixed-width />Auto</a
                >
              </li>
            </BDropdown>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>
