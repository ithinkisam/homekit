<template>
  <button
    :style="{ background: color }"
    @click="$emit('btn-click')"
    class="btn"
  >
    {{ text }}
  </button>
</template>

<script setup>
import { defineProps, defineEmits } from "vue";

defineProps({
  text: String,
  color: String,
});
defineEmits(["btn-click"]);
</script>
