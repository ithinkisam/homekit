<script setup>
defineProps({
  label: {
    type: String,
    required: true,
  },
});
</script>

<template>
  <div class="dropdown">
    <a
      href="#"
      class="d-flex align-items-center link-dark text-decoration-none dropdown-toggle"
      data-bs-toggle="dropdown"
      aria-expanded="false">
      {{ label }}
    </a>
    <ul class="dropdown-menu text-small shadow">
      <slot />
    </ul>
  </div>
</template>
