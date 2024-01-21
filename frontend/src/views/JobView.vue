<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
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
import step2ArabidopsisActive from '@/assets/step2ArabidopsisActive.svg'
import step2ArabidopsisDeactive from '@/assets/step2ArabidopsisDeactive.svg'
import step2MaizeActive from '@/assets/step2MaizeActive.svg'
import step2MaizeDeactive from '@/assets/step2MaizeDeactive.svg'
import step2RiceActive from '@/assets/step2RiceActive.svg'
import step2RiceDeactive from '@/assets/step2RiceDeactive.svg'
import step2SoybeanActive from '@/assets/step2SoybeanActive.svg'
import step2SoybeanDeactive from '@/assets/step2SoybeanDeactive.svg'

const molstarParent = ref<HTMLElement | null>(null)

const smilesInput = ref('')
const proteinList = ref('')
const mailAddress = ref('')

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

const modules = ref([Pagination, Mousewheel])
const swiperInstance = ref()

function onSwiper(swiper: any) {
  swiperInstance.value = swiper
}

const activeImages = [step1Active, step2Active, step3Active, step4Active]
const deactiveImages = [step1Deactive, step2Deactive, step3Deactive, step4Deactive]
const stepImages = ref(deactiveImages.slice())
const toggleStep = (index: number) => {
  const allIndices = [0, 1, 2, 3]
  const otherIndices = allIndices.filter((idx) => idx !== index)
  stepImages.value[index] = activeImages[index]
  otherIndices.forEach((idx) => {
    stepImages.value[idx] = deactiveImages[idx]
  })
  swiperInstance.value.slideTo(index)
}

const proteinListTemplates = {
  arabidopsis: 'A0A140JWM8\nA0A178U7J2\nA0A178US29\nA0A178W3E8\nA0A1I9LME3',
  maize: 'A0A060CVD8\nA0A060CVG2\nA0A060CVM9\nA0A060CY61\nA0A060D7B7',
  rice: 'A0A0N7KC78\nA0A0N7KCX9\nA0A0N7KDF7\nA0A0N7KEY5\nA0A0N7KF53',
  soybean: 'A0A075W8S1\nA0A0B5EA67\nA0A0R0E2H8\nA0A0R0E2W3\nA0A0R0E3W6'
}
const step2PlantsList = ['arabidopsis', 'maize', 'rice', 'soybean']
const step2Plant = ref('')
const activePlants = [step2ArabidopsisActive, step2MaizeActive, step2RiceActive, step2SoybeanActive]
const deactivePlants = [
  step2ArabidopsisDeactive,
  step2MaizeDeactive,
  step2RiceDeactive,
  step2SoybeanDeactive
]
const step2PlantsImg = ref(deactivePlants.slice())
const togglePlants = (index: number) => {
  const allIndices = [0, 1, 2, 3]
  const otherIndices = allIndices.filter((idx) => idx !== index)
  step2Plant.value = step2PlantsList[index]
  proteinList.value = proteinListTemplates[step2Plant.value as keyof typeof proteinListTemplates]
  step2PlantsImg.value[index] = activePlants[index]
  otherIndices.forEach((idx) => {
    step2PlantsImg.value[idx] = deactivePlants[idx]
  })
}

const rows = ref(5)
const calculateRows = () => {
  const singleRowHeight = 25
  const viewportHeight = window.innerHeight
  const desiredHeightVH = 35
  const totalHeightPX = (viewportHeight * desiredHeightVH) / 100
  rows.value = Math.floor(totalHeightPX / singleRowHeight)
}
onMounted(calculateRows)
watch(() => window.innerHeight, calculateRows)

const checkInputs = () => {
  if (!smilesInput.value) {
    alert('Molecular in SMILE format is currently empty. :(')
    return
  }
  if (step2Plant.value === '') {
    alert('Plants is currently not selected. :(')
    return
  }
  if (!proteinList.value) {
    alert('Protein list is currently empty. :(')
    return
  }
  if (!mailAddress.value) {
    alert('Email Address is currently empty. :(')
    return
  }
  console.log(smilesInput.value, proteinList.value, mailAddress.value)
}
</script>

<template>
  <v-app>
    <Header />
    <Footer />

    <v-main>
      <v-container fluid class="ps-0 pe-0">
        <v-row style="height: 8vh">
          <v-col cols="10" offset="1" class="d-flex justify-space-between">
            <img
              :src="stepImages[0]"
              @click="toggleStep(0)"
              style="max-width: 14vw; max-height: 8vh"
            />
            <img :src="stepImages[1]" style="max-width: 14vw; max-height: 8vh" />
            <img
              :src="stepImages[2]"
              @click="toggleStep(2)"
              style="max-width: 14vw; max-height: 8vh"
            />
            <img
              :src="stepImages[3]"
              @click="toggleStep(3)"
              style="max-width: 14vw; max-height: 8vh"
            />
          </v-col>
          <v-col cols="1"></v-col>
        </v-row>
      </v-container>

      <swiper
        :scrollbar="{ hide: false }"
        :mousewheel="false"
        :simulateTouch="false"
        :modules="modules"
        @swiper="onSwiper"
      >
        <swiper-slide
          ><v-container>
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
                  :hide-details="true"
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
                  style="color: #ecbf8e; font-size: 1.5em; font-family: Arial Bold"
                  @click="toggleStep(1)"
                >
                  Next Step
                </v-btn>
              </v-col>
              <v-col cols="1"></v-col>
            </v-row>
          </v-container>
        </swiper-slide>
        <swiper-slide
          ><v-container class="ps-0 pe-0">
            <v-row style="height: 30vh">
              <v-col class="d-flex justify-space-between">
                <img
                  :src="step2PlantsImg[0]"
                  @click="togglePlants(0)"
                  style="max-width: 14vw; max-height: 30vh"
                />
                <img
                  :src="step2PlantsImg[1]"
                  @click="togglePlants(1)"
                  style="max-width: 14vw; max-height: 30vh"
                />
                <img
                  :src="step2PlantsImg[2]"
                  @click="togglePlants(2)"
                  style="max-width: 14vw; max-height: 30vh"
                />
                <img
                  :src="step2PlantsImg[3]"
                  @click="togglePlants(3)"
                  style="max-width: 14vw; max-height: 30vh"
                />
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-textarea
                  clearable
                  clear-icon="mdi-close-circle"
                  label="Custom protein list"
                  variant="solo-inverted"
                  rounded="4"
                  :hide-details="true"
                  :rows="rows"
                  v-model="proteinList"
                  placeholder="If you have some prior knowledge or relevant clues, we highly recommend selectively choosing a subset of proteins from the plant proteome for targeted reverse virtual screening. This approach can greatly expedite the task execution time. 
Please provide the Uniprot IDs of the proteins you have selected in a list format here, or alternatively, you can upload your list file. For example:
A0A024FLK4
A0A075DNI2
A0A0N7KC65
A0A0N7KC78
A0A0N7KC94"
                ></v-textarea>
              </v-col>
            </v-row>
            <v-row justify="space-around">
              <v-col cols="9">
                <v-text-field
                  type="email"
                  variant="solo"
                  label="Please Provied Your .edu Email Address"
                  rounded="4"
                  density="compact"
                  :hide-details="true"
                  v-model="mailAddress"
                >
                </v-text-field>
              </v-col>
              <v-col>
                <v-btn
                  color="#267779"
                  height="100%"
                  rounded="4"
                  variant="flat"
                  style="color: #ecbf8e; font-size: 1.5em; font-family: Arial Bold"
                  @click="checkInputs"
                  >Docking</v-btn
                >
              </v-col>
            </v-row>
          </v-container>
        </swiper-slide>
      </swiper>
    </v-main>
  </v-app>
</template>

<style scoped>
.v-text-field__slot {
  background: #eaeaea;
}
</style>
