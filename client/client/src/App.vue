<script setup>

  import { ref, onBeforeMount } from 'vue';
  import axios from 'axios';
  import Cookies from 'js-cookie';

  let counter = ref();

  onBeforeMount(async () => {
    await loadCounter();
  });

  async function loadCounter() {
    const r = await axios.get("/api/get/");
    counter.value = r.data.value;
  }

  async function plusClick() {
    const r = await axios.get("/api/plus/");
    counter.value = r.data.value;
  }

  async function quatroClick() {
    const r = await axios.get("/api/quatro/");
    counter.value = r.data.value;
  }

  async function resetClick() {
    const r = await axios.get("/api/reset/");
    counter.value = r.data.value;
  }

</script>

<template>
  <h1>Текущее значение: {{ counter }}</h1>

  <div class="container">
    <button @click="plusClick()" class="btn">Увеличить на 1</button>
    <button @click="quatroClick()" class="btn">Возвести в квадрат</button>
    <button @click="resetClick()" class="btn">Приравнять к 0</button>
  </div>
</template>

<style scoped>
.container{
  display: flex;
  flex-direction: row;
  justify-content: space-between;

  width: 50%;
}

.btn{
  padding: 10px;
  background-color: rgb(104, 226, 151);
  border: 1px solid rgb(68, 148, 99);

  border-radius: 5px;

  font-size: 15px;
}
</style>
