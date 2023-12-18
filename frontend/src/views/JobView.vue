<script setup lang="ts">
import { ref, computed, reactive } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

const route = useRoute()
const router = useRouter()

const valid = ref(false);
const form = reactive({
  species: '',
  hormone: '',
  dbDirectory: '/data/dxxu/AF2-PDB/07.AlphaPocket',
  pocketList: '',
  pocketDir: '',
  receptorDir: '',
  ligandDir: ''
});

const speciesOptions = ['Arabidopsis', 'Rice', 'Maize', 'Soybean'];
const hormoneOptions = [
  'ABA_abscisic_acid',
  'BR_brassinosteroid',
  'Ethylene',
  'JA_jasmonic_acid',
  'Auxin',
  'Cytokinin',
  'GA_gibberellin',
  'SL_strigolactone',
  'SA_salicylic_acid'
];

function submitForm() {
  if (valid.value) {
    // Submit logic here
    console.log('Form submitted:', form);
  }
}

</script>

<template>
  <v-app>
    <Header />
    <Footer />

    <v-main>
      <v-container>
        <v-form ref="form" v-model="valid" lazy-validation>
          <v-select
            v-model="form.species"
            :items="speciesOptions"
            label="Species"
            required
          ></v-select>
          <v-select
            v-model="form.hormone"
            :items="hormoneOptions"
            label="Hormone"
            required
          ></v-select>
          <v-text-field
            v-model="form.pocketList"
            :placeholder="`01.AF2_Pocket/v4/${form.species}_v4_pocket.list`"
            label="Pocket List"
            required
          ></v-text-field>
          <v-btn :disabled="!valid" color="success" @click="submitForm">Submit</v-btn>
        </v-form>
      </v-container>
    </v-main>
  </v-app>
</template>

<style scoped>
.plant_select {
  background-color: #4d898d;
}
.cyto_select {
  background-color: #d7e5e7;
}
.clickable-row {
  cursor: pointer;
}
</style>
