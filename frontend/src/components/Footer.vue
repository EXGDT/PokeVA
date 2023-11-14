<script setup lang="ts">
import logo from '@/assets/logo.png'
</script>

<!-- <template>
  <footer class="container justify-content-between align-items-center">
    <div class="col-4 d-flex align-items-center">
      <a href="/" class="mb-3 me-2 mb-md-0 text-body-secondary text-decoration-none lh-1">
        <img :src="logo" alt="Logo" width="40" height="40" class="me-3" />
      </a>
      <span class="mb-3 mb-md-0 text-body-secondary">&copy; 2023 Yixiong-Guo, Xindong-Xu</span>
    </div>
  </footer>
</template> -->

<template>
<footer class="container d-flex align-items-end">
    <img :src="logo" alt="logo" class="me-3"/>
    <span class="align-self-center">&copy; 2023 Yisiong-Guo, Xindong-Xu</span>
</footer>    
</template>

<style scoped>
footer {
  position: sticky;
  bottom: 0;
  min-height: 5vh;
}

img {
  width: 5vh;
  height: 5vh;
}
</style>
