<script setup lang="ts">
import { ref, onMounted, nextTick } from 'vue'

import HeaderV from '@/components/HeaderV.vue'
import FooterV from '@/components/FooterV.vue'
import SMILE_molstar from '@/components/SMILE_molstar.vue'
import Home_left from '@/components/Home_left.vue'
import ResultViewMain from '@/components/ResultViewMain.vue'

import { Swiper, SwiperSlide } from 'swiper/vue'
import 'swiper/css'
import 'swiper/css/pagination'
import { Pagination, Mousewheel } from 'swiper/modules'

const modules = ref([Pagination, Mousewheel])
</script>

<template>
  <v-app>
    <HeaderV />
    <v-main>
      <v-container class="fill-height">
        <swiper
          direction="vertical"
          :scrollbar="{ hide: true }"
          :mousewheel="true"
          :simulateTouch="false"
          :modules="modules"
          class="mySwiper fill-height"
        >
          <swiper-slide>
            <ResultViewMain />
          </swiper-slide>
          <swiper-slide>
            <v-row class="fill-height">
              <v-col>
                <Home_left />
              </v-col>
              <v-col>
                <SMILE_molstar />
              </v-col>
            </v-row>
          </swiper-slide>
        </swiper>
      </v-container>
    </v-main>
    <FooterV />
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
