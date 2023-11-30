<script setup lang="ts">
import { ref } from 'vue'
import logo from '@/assets/logo.png'
import fontLogo from '@/assets/fontLogo.svg'
</script>

<template>
  <v-app-bar app color="#428587">
    <v-app-bar-title>
      <img :src="fontLogo" alt="fontLogo" class="ms-6 mt-2" />
    </v-app-bar-title>
    <v-spacer></v-spacer>
    <v-btn variant="text" class="btn-font">Home</v-btn>
    <v-btn variant="text" class="btn-font">Datasets</v-btn>
    <v-btn variant="text" class="btn-font">Job Submition</v-btn>
    <v-btn variant="text" class="btn-font">Download</v-btn>
    <v-btn variant="text" class="btn-font">Help</v-btn>
  </v-app-bar>
</template>

<style scoped>
.v-app-bar-title img {
  width: 12vw
}

.btn-font {
  color: #EBBE8B;
  font-size: 0.9vw;
  font-family: Arial, sans-serif;
  font-weight: bold;
}
</style>
