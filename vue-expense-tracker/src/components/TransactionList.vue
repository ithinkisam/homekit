<template>
  <h3>History</h3>
  <ul id="list" class="list">
    <li
      :key="transaction.id"
      v-for="transaction in transactions"
      :class="transaction.amount < 0 ? 'minus' : 'plus'"
    >
      {{ transaction.text }} <span>{{ transaction.amount }}</span>
      <button @click="deleteTransaction(transaction.id)" class="delete-btn">
        x
      </button>
    </li>
  </ul>
</template>

<script setup>
import { defineProps } from "vue";

const emit = defineEmits(["delete-transaction"]);

const props = defineProps({
  transactions: {
    type: Array,
    required: true,
  },
});

const deleteTransaction = (id) => {
  emit("delete-transaction", id);
};
</script>
