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
    <button
      class="btn btn-secondary dropdown-toggle"
      type="button"
      data-bs-toggle="dropdown"
      aria-expanded="false">
      {{ label }}
    </button>
    <ul class="dropdown-menu">
      <slot />
    </ul>
  </div>
</template>
