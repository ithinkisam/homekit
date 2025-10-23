<template>
  <form @submit.prevent="onSubmit" class="add-form">
    <div class="form-control">
      <label>Task</label>
      <input type="text" v-model="text" name="text" placeholder="Add text" />
    </div>
    <div class="form-control">
      <label>Day & time</label>
      <input
        type="text"
        v-model="day"
        name="day"
        placeholder="Add Day & time"
      />
    </div>
    <div class="form-control form-control-check">
      <label>Set reminder</label>
      <input type="checkbox" v-model="reminder" name="reminder" />
    </div>

    <input type="submit" value="Save Task" class="btn btn-block" />
  </form>
</template>

<script setup>
import { ref, defineEmits } from "vue";

const text = ref("");
const day = ref("");
const reminder = ref(false);

const emit = defineEmits(["add-task"]);

const onSubmit = () => {
  if (!text.value) {
    alert("Please add a task");
    return;
  }
  const newTask = {
    text: text.value,
    day: day.value,
    reminder: reminder.value,
  };

  emit("add-task", newTask);

  text.value = "";
  day.value = "";
  reminder.value = false;
};
</script>

<style scoped>
.add-form {
  margin-bottom: 40px;
}

.form-control {
  margin: 20px 0;
}

.form-control label {
  display: block;
}

.form-control input {
  width: 100%;
  height: 40px;
  margin: 5px;
  padding: 3px 7px;
  font-size: 17px;
}

.form-control-check {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.form-control-check label {
  flex: 1;
}

.form-control-check input {
  flex: 2;
  height: 20px;
}
</style>
