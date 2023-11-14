<script setup lang="ts">
import logo from '@/assets/logo.png'
</script>

<template>
  <div class="container">
    <header class="d-flex flex-wrap justify-content-center border-bottom">
      <a href="/" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto link-body-emphasis text-decoration-none">
        <img :src="logo" alt="Logo" class="me-3">
        <span class="fs-4">PokeVA</span>
      </a>

      <ul class="nav nav-pills align-items-center">
        <li class="nav-item align-items-center"><a href="#" class="nav-link active" aria-current="page">Home</a></li>
        <li class="nav-item align-items-center"><a href="#" class="nav-link">Help</a></li>
        <li class="nav-item align-items-center"><a href="#" class="nav-link">About</a></li>
      </ul>
    </header>
  </div>
</template>

<style scoped>
img {
  width: 7.5vh;
  height: 7.5vh;
}

header {
  position: sticky;
  top: 0;
  height: 10vh;
}

</style>
