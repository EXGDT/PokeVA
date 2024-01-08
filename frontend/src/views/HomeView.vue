<script setup lang="ts">
import { ref, onMounted } from 'vue'

import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import SMILE_molstar from '@/components/SMILE_molstar.vue'
import Home_left from '@/components/Home_left.vue'
import ResultViewMain from '@/components/ResultViewMain.vue'
import Home_cover from '@/components/Home_cover.vue'

import { Swiper, SwiperSlide, useSwiper } from 'swiper/vue'
import 'swiper/css'
import 'swiper/css/pagination'
import { Pagination, Mousewheel } from 'swiper/modules'
import type { SwiperEvents } from 'swiper/types'

const modules = ref([Pagination, Mousewheel])

const swiperInstance = ref()

function onSwiper(swiper: any) {
  swiperInstance.value = swiper
}

function goToNextSlide() {
  swiperInstance.value.slideNext()
}
</script>

<template>
  <v-app>
    <Header />
    <Footer />
    <v-main style="background-color: #d5e4e4">
      <v-container fluid class="fill-height">
        <swiper
          direction="vertical"
          :scrollbar="{ hide: true }"
          :mousewheel="true"
          :simulateTouch="false"
          :modules="modules"
          class="mySwiper fill-height"
          @swiper="onSwiper"
        >
          <swiper-slide>
            <Home_cover @arrowClicked="goToNextSlide" />
          </swiper-slide>
          <swiper-slide>
            <v-row class="fill-height">
              <v-col class="fill-height">
                <Home_left />
              </v-col>
              <v-col class="mt-5">
                <SMILE_molstar />
              </v-col>
            </v-row>
          </swiper-slide>
        </swiper>
      </v-container>
    </v-main>
  </v-app>
</template>

<style>
.mySwiper {
  height: 100%;
  width: 100%; /* 确保 Swiper 容器宽度为 100% */
}

.swiper-slide {
  width: 100%; /* 确保每个幻灯片宽度为 100% */
}
</style>
