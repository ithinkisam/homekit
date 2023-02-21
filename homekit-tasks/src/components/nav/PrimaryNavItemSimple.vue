<script setup>
import { settings } from "../global/global.js";

const props = defineProps({
  href: {
    type: String,
    required: false,
  },
});

function clicked() {
  settings.active_menu = props.href;
}
function isActive() {
  return props.href == settings.active_menu;
}
</script>

<template>
  <li class="nav-item">
    <a
      v-if="href"
      class="nav-link link-dark"
      :class="{ active: isActive() }"
      :href="href"
      @click="clicked">
      <slot />
    </a>
    <slot v-else />
  </li>
</template>
