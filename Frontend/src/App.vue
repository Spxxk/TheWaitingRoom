<template>
  <div>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.3/css/bulma.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@900&display=swap" rel="stylesheet">
    <Header></Header>
    <div id="app">
      <div class="main-layout">
        <main class="content">
          <RouterView />
        </main>
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>

<script setup>
import { RouterView } from 'vue-router';
import Header from './components/Navbar.vue';
import Footer from './components/Footer.vue';
</script>

<style scoped>
#app {
  display: flex;
  flex-direction: column;
  font-family: 'Raleway', sans-serif;
}

.content {
  flex: 1;
}

.main-layout {
  display: flex;
  flex: 1;
}

header {
  background-color: #42b883;
  color: white;
  text-align: center;
}
</style>
