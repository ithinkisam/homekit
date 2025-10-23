<template>
  <Header />
  <div class="container">
    <Balance :total="+total" />
    <IncomeExpenses :income="+income" :expense="+expense" />
    <TransactionList
      @delete-transaction="handleDeleteTransaction"
      :transactions="transactions"
    />
    <AddTransaction @transaction-submitted="handleTransactionSubmitted" />
  </div>
</template>

<script setup>
import Header from "./components/Header.vue";
import Balance from "./components/Balance.vue";
import IncomeExpenses from "./components/IncomeExpenses.vue";
import TransactionList from "./components/TransactionList.vue";
import AddTransaction from "./components/AddTransaction.vue";

import { useToast } from "vue-toastification";
const toast = useToast();

import { ref, computed, onMounted } from "vue";

const transactions = ref([]);

onMounted(() => {
  const savedTransactions = JSON.parse(localStorage.getItem("transactions"));
  if (savedTransactions) {
    transactions.value = savedTransactions;
  }
});

const total = computed(() => {
  return transactions.value.reduce((acc, transaction) => {
    return acc + transaction.amount;
  }, 0);
});
const income = computed(() => {
  return transactions.value
    .filter((transaction) => transaction.amount > 0)
    .reduce((acc, transaction) => {
      return acc + transaction.amount;
    }, 0)
    .toFixed(2);
});
const expense = computed(() => {
  return transactions.value
    .filter((transaction) => transaction.amount < 0)
    .reduce((acc, transaction) => {
      return acc + Math.abs(transaction.amount);
    }, 0)
    .toFixed(2);
});

const handleTransactionSubmitted = (transaction) => {
  transactions.value.push({
    id: generateUniqueId(),
    ...transaction,
  });
  saveTransactionsToLocalStorage();
  toast.success("Transaction added!");
};

const handleDeleteTransaction = (id) => {
  console.log(id);
  transactions.value = transactions.value.filter(
    (transaction) => transaction.id !== id
  );
  saveTransactionsToLocalStorage();
  toast.success("Transaction deleted");
};

const generateUniqueId = () => {
  return Math.floor(Math.random() * 1000000);
};

// Save to localStorage
const saveTransactionsToLocalStorage = () => {
  localStorage.setItem("transactions", JSON.stringify(transactions.value));
};
</script>
