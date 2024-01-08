<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

import { createPluginUI } from 'molstar/lib/mol-plugin-ui'
import { DefaultPluginUISpec } from 'molstar/lib/mol-plugin-ui/spec'
import { PluginSpec } from 'molstar/lib/mol-plugin/spec'
import { PluginConfig } from 'molstar/lib/mol-plugin/config'
import { PluginUIContext } from 'molstar/lib/mol-plugin-ui/context'
import 'molstar/lib/mol-plugin-ui/skin/light.scss'

import { Swiper, SwiperSlide, useSwiper } from 'swiper/vue'
import 'swiper/css'
import 'swiper/css/pagination'
import { Pagination, Mousewheel } from 'swiper/modules'
import type { SwiperEvents } from 'swiper/types'

import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

import step1Active from '@/assets/step1Active.svg'
import step2Active from '@/assets/step2Active.svg'
import step3Active from '@/assets/step3Active.svg'
import step4Active from '@/assets/step4Active.svg'
import step1Deactive from '@/assets/step1Deactive.svg'
import step2Deactive from '@/assets/step2Deactive.svg'
import step3Deactive from '@/assets/step3Deactive.svg'
import step4Deactive from '@/assets/step4Deactive.svg'

const molstarParent = ref<HTMLElement | null>(null)

declare global {
  interface Window {
    molstar?: PluginUIContext
  }
}

onMounted(async () => {
  if (molstarParent.value !== null) {
    const MySpec: PluginSpec = {
      ...DefaultPluginUISpec(),
      config: [
        [PluginConfig.VolumeStreaming.Enabled, false],
        [PluginConfig.Viewport.ShowExpand, true],
        [PluginConfig.Viewport.ShowControls, false],
        [PluginConfig.Viewport.ShowSettings, false],
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
      // { url: 'https://files.rcsb.org/download/3PTB.pdb' },
      // { url: 'https://files.rcsb.org/ligands/view/H35.cif' },
      { url: 'https://files.rcsb.org/ligands/6/605/605.cif' },
      { state: { isGhost: true } }
    )

    const trajectory = await window.molstar.builders.structure.parseTrajectory(data, 'mmcif')
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

const smilesInput = ref('')
const handleInputChange = async () => {
  const response = await axios.post('/PokeVA_api/smile2pdb/', {
    smile: smilesInput.value
  })
  const pdbData = response.data.pdb
  const blob = new Blob([pdbData], { type: 'chemical/x-pdb' })
  const blobUrl = URL.createObjectURL(blob)
  if (window.molstar) {
    await window.molstar.clear()
    const data = await window.molstar.builders.data.download(
      { url: blobUrl },
      { state: { isGhost: true } }
    )
    const trajectory = await window.molstar.builders.structure.parseTrajectory(data, 'pdb')
    await window.molstar.builders.structure.hierarchy.applyPreset(trajectory, 'default')
  }
  URL.revokeObjectURL(blobUrl)
}
const route = useRoute()
const router = useRouter()
</script>

<template>
  <v-app>
    <Header />
    <Footer />

    <v-main>
      <v-container fluid>
        <v-row>
          <v-col cols="10" offset="1" class="d-flex justify-space-between">
            <img :src="step1Active" style="height: 6vh" />
            <img :src="step2Deactive" style="height: 6vh" />
            <img :src="step3Deactive" style="height: 6vh" />
            <img :src="step4Deactive" style="height: 6vh" />
          </v-col>
        </v-row>
        <v-row>
          <v-col offset="1" cols="10">
            <v-text-field
              label="You can paste the SMILE text here. For example: C1=COC(=C1)CNC2=NC=NC3=C2NC=N3."
              placeholder="C=C(c1ccccc1)c2ccccc2"
              v-model="smilesInput"
              @input="handleInputChange"
              rounded
              density="compact"
              bg-color="#FBFCF9"
              variant="solo"
            >
            </v-text-field
          ></v-col>
        </v-row>
        <v-row>
          <v-col cols="10" offset="1">
            <div ref="molstarParent" style="position: relative; height: 60vh"></div>
          </v-col>
        </v-row>
        <v-row justify="end">
          <v-col class="d-flex justify-end">
            <v-btn
              color="#267779"
              rounded="4"
              variant="flat"
              style="color:#ECBF8E; font-size: 1.5em; font-family: Arial Bold;"
            >
              Next Step
            </v-btn>
          </v-col>
          <v-col cols="1"></v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<style scoped>
</style>
