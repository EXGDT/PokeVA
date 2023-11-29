<script setup lang="ts">
import { ref, onMounted, nextTick } from 'vue'

import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import HeaderV from '@/components/HeaderV.vue'
import FooterV from '@/components/FooterV.vue'
import Plants_select from '@/components/Plants_select.vue'
import Cytokinins_select from '@/components/Cytokinins_select.vue'
import SMILE_molstar from '@/components/SMILE_molstar.vue'
import Home_left from '@/components/Home_left.vue'

const smileMolstar = ref<HTMLElement | null>(null)
const fullpageOptions = {
  anchors: ['firstPage', 'secondPage']
}
</script>

<template>
  <v-app>
    <HeaderV />
    <v-main class="container">
      <div class="row h-100">
        <div class="col-6 h-100">
          <Home_left />
        </div>
        <div class="col-6 h-100" ref="smileMolstar">
          <SMILE_molstar />
        </div>
      </div>
    </v-main>
    <FooterV />
  </v-app>
</template>
