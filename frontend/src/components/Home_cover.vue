<script setup lang="ts">
import { defineEmits } from 'vue'
import bg_image from '@/assets/Home_cover_left.svg'

const emit = defineEmits(['arrowClicked'])

const onArrowClick = () => {
  emit('arrowClicked')
}
</script>

<template>
  <v-container fluid class="h-100 p-0">
    <v-row class="fill-height">
      <v-col class="fill-height d-flex justify-center">
        <v-img :src="bg_image" class="justify-center align-center">
          <v-card
            max-width="90%"
            variant="flat"
            class="align-self-center"
            style="background-color: transparent"
          >
            <v-card-item>
              <v-card-title class="text-h4"> Introduction </v-card-title>
            </v-card-item>

            <v-card-text class="text--primary" style="font-size: 1rem; font-family: arial;">
              Welcome to PHIPRD, the premier resource for exploring the dynamic world of plant
              hormones and their interacting proteins. Our platform harnesses the power of reverse
              docking to illuminate the intricate interactions of nine essential plant
              hormones—auxins, cytokinins, ethylene, gibberellin, jasmonic acid, salicylic acid,
              strigolactones, abscisic acid, and brassinosteroids—across four pivotal plant species:
              Arabidopsis, rice, maize, and soybean. <br />
              <br />
              With PHIPRD, researchers gain unparalleled access to a treasure trove of AlphaFold
              predicted protein structures, with a respective count of 27434, 43649, 39299, and
              55799 for each species, alongside a select compilation from the PDB database. Our
              comprehensive 3D database and visualization tools offer insights into the binding
              energies and molecular interactions at the heart of plant growth, development, and
              stress response mechanisms. <br />
              <br />
              Our robust suite of functionalities enables users to: <br />
              <ul>
                <li>
                  Query and browse through 3D representations of the binding energies between plant
                  hormones and their corresponding protein structures predicted by AlphaFold.<br />
                </li>
                <li>
                  Delve into the PDB database for a refined selection of protein structures and
                  examine their interaction with plant hormones. <br />
                </li>
                <li>
                  Submit custom small molecule structures and choose the most relevant protein
                  databases for precise reverse docking analyses. <br />
                </li>
                <li>
                  Investigate pocket information on both AlphaFold predicted and experimentally
                  determined proteins, identified by p2rank.<br />
                </li>
              </ul>
              Visualize complex molecular structures with MolStar and perform docking simulations
              using AutoDock Vina.
              <br />PHIPRD stands as the first comprehensive database dedicated to the synthesis,
              transport, sensory detection, and metabolism of plant hormones. Our mission is to
              empower the scientific community with a sophisticated platform that catalyzes
              groundbreaking research in plant hormone interactions. Explore the potential within
              PHIPRD and unlock new dimensions in plant biology research.
            </v-card-text>
          </v-card>
        </v-img>
      </v-col>
      <v-col class="fill-height d-flex justify-center">
        <img src="@/assets/Home_cover_right.svg" style="max-height: 100%; max-width: 100%" />
      </v-col>
    </v-row>
  </v-container>
  <!-- <img src="@/assets/Home_cover_nobg.svg" style="height: 100%; width: 100%" /> -->
  <img src="@/assets/arrow.svg" class="arrow" @click="onArrowClick" />
</template>

<style>
.v-responsive__content {
  width: 100%;   /* 调整为所需宽度 */
  height: auto;  /* 调整为所需高度 */
}
.arrow {
  position: absolute;
  height: 10%;
  width: 10%;
  left: 50%;
  bottom: 2vh;
  transform: translateX(-50%);
  animation: bounce 1.5s infinite;
}

@keyframes bounce {
  0%,
  20%,
  50%,
  80%,
  100% {
    transform: translateX(-50%) translateY(0);
  }
  40% {
    transform: translateX(-50%) translateY(1vh);
  }
  60% {
    transform: translateX(-50%) translateY(0.5vh);
  }
}
</style>
