<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import { createPluginUI } from 'molstar/lib/mol-plugin-ui'
import { DefaultPluginUISpec } from 'molstar/lib/mol-plugin-ui/spec'
import { PluginSpec } from 'molstar/lib/mol-plugin/spec'
import { PluginConfig } from 'molstar/lib/mol-plugin/config'
import { PluginUIContext } from 'molstar/lib/mol-plugin-ui/context'
import 'molstar/lib/mol-plugin-ui/skin/light.scss'

import { Swiper, SwiperSlide } from 'swiper/vue'
import 'swiper/css'
import 'swiper/css/pagination'
import { Pagination, Mousewheel } from 'swiper/modules'
const modules = ref([Pagination, Mousewheel])

import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

const route = useRoute()

const molstarParent = ref<HTMLElement | null>(null)

declare global {
  interface Window {
    molstar?: PluginUIContext
  }
}

onMounted(async () => {
  const cyto = route.query.cyto
  const plant = route.query.plant
  const pocket_id = route.query.pocket_id

  const response = await axios.get(`http://172.21.66.13:8877/searchPDBQT/`, {
    params: { cyto, plant, pocket_id }
  })

  const pdbqtData = response.data.pdbqt_content
  const blob = new Blob([pdbqtData], { type: 'chemical/x-pdb' })
  const blobUrl = URL.createObjectURL(blob)
  if (molstarParent.value !== null) {
    const MySpec: PluginSpec = {
      ...DefaultPluginUISpec(),
      config: [
        [PluginConfig.VolumeStreaming.Enabled, false],
        [PluginConfig.Viewport.ShowExpand, true],
        [PluginConfig.Viewport.ShowControls, true],
        [PluginConfig.Viewport.ShowSettings, true],
        [PluginConfig.Viewport.ShowAnimation, false]
      ],
      layout: {
        initial: {
          isExpanded: false,
          regionState: { top: 'hidden', left: 'hidden', right: 'hidden', bottom: 'hidden' }
        }
      }
    }

    window.molstar = await createPluginUI(molstarParent.value, MySpec)

    const data = await window.molstar.builders.data.download(
      { url: blobUrl },
      { state: { isGhost: true } }
    )

    const trajectory = await window.molstar.builders.structure.parseTrajectory(data, 'pdbqt')
    await window.molstar.builders.structure.hierarchy.applyPreset(trajectory, 'default')

    molstarParent.value.addEventListener(
      'wheel',
      (event) => {
        event.stopPropagation()
      },
      { passive: false }
    )
  }
})
</script>

<template>
  <v-app>
    <Header />
    <v-main>
      <v-container fluid class="fill-height">
        <swiper
          direction="vertical"
          :scrollbar="{ hide: true }"
          :mousewheel="true"
          :simulateTouch="false"
          :modules="modules"
          class="mySwiper fill-height"
        >
          <swiper-slide>
            <v-row fluid class="fill-height">
              <v-col class="fill-height">
                <div ref="molstarParent" class="h-100" style="position: relative"></div>
              </v-col>
              <v-col> </v-col>
            </v-row>
          </swiper-slide>
          <swiper-slide>
            <swiper
              :scrollbar="{ hide: false }"
              :pagination="{
                clickable: true
              }"
              :simulateTouch="true"
              :modules="modules"
              class="mySwiper fill-height"
            >
              <swiper-slide>
                <v-card text="MMseqs2 Uniprot90" variant="tonal"></v-card>
              </swiper-slide>
              <swiper-slide>
                <v-card text="Foldseek PDB100 Hits" variant="tonal"></v-card>
              </swiper-slide>
            </swiper>
          </swiper-slide>
        </swiper>
      </v-container>
    </v-main>
    <Footer />
  </v-app>
</template>

<style>
.text-ellipsis {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  display: block;
  max-width: 150px;
}

.mySwiper {
  height: 100%;
  width: 100%; /* 确保 Swiper 容器宽度为 100% */
}

.swiper-slide {
  width: 100%; /* 确保每个幻灯片宽度为 100% */
}
</style>
