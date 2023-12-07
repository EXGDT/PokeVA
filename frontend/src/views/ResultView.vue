<script setup lang="ts">
import { ref, watch, watchEffect, readonly } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

const route = useRoute()
const router = useRouter()

const resultHeaders = ref([
  { title: 'Pocket ID', value: 'pocket_id', align: 'start', width: '20%' },
  { title: 'Entry', value: 'entry', align: 'start' },
  { title: 'Protein Names', value: 'protein_names', align: 'start' },
  { title: 'Gene Names', value: 'gene_names', align: 'start' },
  { title: 'Organism', value: 'organism', align: 'start' },
  { title: 'PDB ID', value: 'pdb', align: 'start', width: '5%' },
  { title: 'Binding affinity', value: 'binding_affinity', align: 'start', width: '5%' }
])

interface DataItem {
  pocket_id: string
  entry: string
  protein_names: string
  gene_names: string
  organism: string
  pdb: string
  binding_affinity: number
}

const itemsPerPage = ref(10)
const totalItems = ref(0)
const serverItems = ref<DataItem[]>([])
interface LoadItemsParams {
  page: number
  itemsPerPage: number
}

const loadItems = async ({ page, itemsPerPage }: LoadItemsParams) => {
  const cyto = route.query.cyto
  const plant = route.query.plant
  const limit = itemsPerPage
  const offset = (page - 1) * itemsPerPage
  const response = await axios.get(`http://172.21.66.13:8877/searchAPI/`, {
    params: { cyto, plant, limit, offset }
  })
  serverItems.value = response.data.results
  totalItems.value = response.data.count
}

const onRowClick = (item) => {
  const pocket_id = item.pocket_id
  const cyto = route.query.cyto
  const plant = route.query.plant
  router.push({
    name: 'detail',
    query: { pocket_id: pocket_id, plant: plant, cyto: cyto }
  })
}

const plantCytoList = ref([
  {
    plant: 'Arabidopsis thaliana',
    cytos: [
      { cyto: 'Auxin' },
      { cyto: 'Cytokinin' },
      { cyto: 'Ethylene' },
      { cyto: 'Gibberellin' },
      { cyto: 'Jasmonic acid' },
      { cyto: 'Salicylic acid' },
      { cyto: 'Strigolactone' },
      { cyto: 'Abscisic acid' },
      { cyto: 'Brassinosteroid' }
    ]
  },
  {
    plant: 'Oryza sativa',
    cytos: [
      { cyto: 'Auxin' },
      { cyto: 'Cytokinin' },
      { cyto: 'Ethylene' },
      { cyto: 'Gibberellin' },
      { cyto: 'Jasmonic acid' },
      { cyto: 'Salicylic acid' },
      { cyto: 'Strigolactone' },
      { cyto: 'Abscisic acid' },
      { cyto: 'Brassinosteroid' }
    ]
  },
  {
    plant: 'Glycine max',
    cytos: [
      { cyto: 'Auxin' },
      { cyto: 'Cytokinin' },
      { cyto: 'Ethylene' },
      { cyto: 'Gibberellin' },
      { cyto: 'Jasmonic acid' },
      { cyto: 'Salicylic acid' },
      { cyto: 'Strigolactone' },
      { cyto: 'Abscisic acid' },
      { cyto: 'Brassinosteroid' }
    ]
  },
  {
    plant: 'Zea mays',
    cytos: [
      { cyto: 'Auxin' },
      { cyto: 'Cytokinin' },
      { cyto: 'Ethylene' },
      { cyto: 'Gibberellin' },
      { cyto: 'Jasmonic acid' },
      { cyto: 'Salicylic acid' },
      { cyto: 'Strigolactone' },
      { cyto: 'Abscisic acid' },
      { cyto: 'Brassinosteroid' }
    ]
  }
])

interface PlantMapping {
  [key: string]: string
}
interface CytoMapping {
  [key: string]: string
}
const plantMapping: PlantMapping = {
  'Arabidopsis thaliana': 'Arabidopsis',
  'Oryza sativa': 'Oryza',
  'Glycine max': 'Glycine',
  'Zea mays': 'Zea'
}
const cytoMapping: CytoMapping = {
  'Auxin': 'Auxin',
  'Cytokinin': 'Cytokinin',
  'Ethylene': 'Ethylene',
  'Gibberellin': 'Gibberellin',
  'Jasmonic acid': 'Jasmonic_acid',
  'Salicylic acid': 'Salicylic_acid',
  'Strigolactone': 'Stringolactone',
  'Abscisic acid': 'Abscisic_acid',
  'Brassinosteroid': 'Brassinosteroid'
}

const updateDataTable = async (plantName: string, cytoName: string) => {
  const plantValue = plantMapping[plantName]
  const cytoValue = cytoMapping[cytoName]
  const params = { plant: plantValue, cyto: cytoValue }

  try {
    const response = await axios.get(`http://172.21.66.13:8877/searchAPI/`, { params })
    serverItems.value = response.data.results
    totalItems.value = response.data.count
  } catch (error) {
    console.error(error)
  }
  router.push({ path: '/result', query: { plant: plantValue, cyto: cytoValue } });
}

const searchInput=ref('')
const searchAPIHandles = async () => {
  try {
    const searchQuery = searchInput.value;
    const params = {
      plant: route.query.plant,
      cyto: route.query.cyto,
      search: searchQuery,
    };
    const response = await axios.get(`http://172.21.66.13:8877/searchAPI/`, { params });
    serverItems.value = response.data.results;
    totalItems.value = response.data.count;
  } catch (error) {
    console.error(error);
  }
};
</script>

<template>
  <v-app>
    <Header />
    <Footer />

    <v-navigation-drawer app color="#D5E4E4" width="288">
      <v-list class="m-3">
        <v-list-group
          v-for="(plantCyto, index) in plantCytoList"
          :key="plantCyto.plant"
          :value="plantCyto.plant"
        >
          <template v-slot:activator="{ props }">
            <v-list-item
              v-bind="props"
              :title="plantCyto.plant"
              rounded="4"
              class="m-1"
              style="background-color: #4d898d"
            ></v-list-item>
          </template>
          <v-list-item
            v-for="(cytos, index) in plantCyto.cytos"
            :key="index"
            :title="cytos.cyto"
            style="background-color: #eefefe"
            rounded="5"
            class="m-1 ms-3"
            @click="updateDataTable(plantCyto.plant, cytos.cyto)"
          ></v-list-item>
        </v-list-group>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <v-data-table-server
        v-model:items-per-page="itemsPerPage"
        :headers="resultHeaders"
        :items-length="totalItems"
        :items="serverItems"
        :fixed-header="true"
        @update:options="loadItems"
        class="h-100"
      >
        <template v-slot:top>
          <v-text-field
            label="Search"
            placeholder="Pocket ID/Uniprot ID/Gene names……"
            v-model="searchInput"
            @input="searchAPIHandles"
            rounded="4"
            density="compact"
            bg-color="#4d898d"
            variant="solo"
            class="ms-4 mt-4 me-4 mb-0"
            hide-details
          >
          </v-text-field>
        </template>
        <template v-slot:bottom>
          <div class="text-center pt-2">
            <v-pagination :length="totalItems"></v-pagination>
          </div>
        </template>
      </v-data-table-server>
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
</style>
