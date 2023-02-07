<script setup>
defineProps({
  href: {
    type: String,
    required: false,
  },
});

function closeNav() {
  document.getElementsByClassName("navbar-toggler")[0].click();
}
</script>

<template>
  <li class="nav-item">
    <a v-if="href" class="nav-link" @click="closeNav" :href="href"><slot /></a>
    <slot v-if="!href" />
  </li>
</template>
