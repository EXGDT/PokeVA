<script setup lang="ts">
import { ref, onMounted, nextTick} from 'vue'

import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import Plants_select from '@/components/Plants_select.vue'
import Cytokinins_select from '@/components/Cytokinins_select.vue'
import SMILE_molstar from '@/components/SMILE_molstar.vue'
import Home_left from '@/components/Home_left.vue'

const smileMolstar = ref<HTMLElement | null>(null);;

</script>

<template>
  <Header />
  <main class="container" style="min-height: 80vh">
    <div class="row h-100">
      <div class="col-6 h-100">
        <Home_left />
      </div>
      <div class="col-6 h-100" ref="smileMolstar">
        <SMILE_molstar />
      </div>
    </div>
  </main>
  <Footer />
</template>

