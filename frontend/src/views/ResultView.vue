<script setup lang="ts">
import { ref, computed, reactive } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

const route = useRoute()
const router = useRouter()

interface ResultHeader {
  title: string
  value: string
  align: 'start' | 'center' | 'end' // 根据实际需要调整
  width?: string // 可选属性
  sortable?: boolean // 可选属性
}

interface DataItem {
  pocket_id: string
  entry: string
  protein_names: string
  gene_names: string
  organism: string
  pdb: string
  binding_affinity: number
  [key: string]: string | number
}

interface PlantMapping {
  [key: string]: string
}

interface CytoMapping {
  [key: string]: string
}

interface SortOption {
  key: string
  order: 'asc' | 'desc'
}

interface LoadItemsParams {
  page: number
  itemsPerPage: number
  sortBy: SortOption[]
}

const resultHeaders = ref<ResultHeader[]>([
  { title: 'Pocket ID', value: 'pocket_id', align: 'start', width: '15%' },
  { title: 'AFDB ID', value: 'afdb_id', align: 'start' },
  { title: 'Protein Names', value: 'protein_names', align: 'start' },
  { title: 'Gene Names', value: 'gene_names', align: 'start' },
  { title: 'Organism', value: 'organism', align: 'start' },
  { title: 'PDB ID', value: 'pdb', align: 'start', width: '6%' },
  {
    title: 'Binding affinity',
    value: 'binding_affinity',
    align: 'start',
    width: '12%',
    sortable: true
  }
])

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

const plantMapping: PlantMapping = {
  'Arabidopsis thaliana': 'Arabidopsis',
  'Oryza sativa': 'Oryza',
  'Glycine max': 'Glycine',
  'Zea mays': 'Zea'
}
const cytoMapping: CytoMapping = {
  Auxin: 'Auxin',
  Cytokinin: 'Cytokinin',
  Ethylene: 'Ethylene',
  Gibberellin: 'Gibberellin',
  'Jasmonic acid': 'Jasmonic_acid',
  'Salicylic acid': 'Salicylic_acid',
  Strigolactone: 'Stringolactone',
  'Abscisic acid': 'Abscisic_acid',
  Brassinosteroid: 'Brassinosteroid'
}

const serverCount = ref(0)
const serverResults = ref<DataItem[]>([])
const currentOffset = ref(0)
const searchQuery = ref('')
const countPerPage = ref(25)
const currentPage = ref(1)
const sortByParam = ref('')
const totalPages = computed(() => Math.ceil(serverCount.value / countPerPage.value))

const options = reactive({
  page: 1,
  itemsPerPage: 25,
  sortBy: [],
  sortDesc: []
})

const updateDataTable = async (plantName: string, cytoName: string) => {
  const plantValue = plantMapping[plantName]
  const cytoValue = cytoMapping[cytoName]

  router.push({
    query: { plant: plantValue, cyto: cytoValue }
  })
  await fetchData()
}

const searchAPIHandles = async () => {
  await fetchData()
}

const loadItems = async ({ page, itemsPerPage, sortBy }: LoadItemsParams) => {
  countPerPage.value = itemsPerPage
  currentOffset.value = (page - 1) * itemsPerPage
  if (sortBy.length) {
    console.log(typeof sortBy)
    const sortKey = sortBy[0].key
    const sortOrder = sortBy[0].order
    sortByParam.value = sortOrder === 'desc' ? `-${sortKey}` : sortKey
  }
  await fetchData()
}

const fetchData = async () => {
  const plant = route.query.plant
  const cyto = route.query.cyto
  try {
    const params = {
      plant: plant,
      cyto: cyto,
      search: searchQuery.value,
      limit: countPerPage.value,
      offset: currentOffset.value,
      order_by: sortByParam.value
    }

    const response = await axios.get(`/PokeVA_api/searchAPI/`, { params })
    serverResults.value = response.data.results
    serverCount.value = response.data.count
  } catch (error) {
    console.error(error)
  }
}

const toDetail = (item: DataItem) => {
  const plant = route.query.plant
  const cyto = route.query.cyto
  const pocketId = item.pocket_id
  router.push({
    path: '/detail',
    query: {
      plant: plant,
      cyto: cyto,
      pocket_id: pocketId
    }
  })
}
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
        color="#D6E4E4"
        :hover="true"
        :items-per-page="20"
        :items-per-page-options="[20, 50, 100]"
        :headers="resultHeaders"
        :items-length="serverCount"
        :items="serverResults"
        :fixed-header="true"
        :multi-sort="false"
        :options.sync="options"
        @update:options="loadItems"
        class="h-100"
      >
        <template v-slot:top>
          <v-text-field
            label="Search"
            placeholder="Pocket ID/Uniprot ID/Gene names……"
            v-model="searchQuery"
            @input="searchAPIHandles"
            rounded="4"
            density="compact"
            bg-color="#4d898d"
            variant="solo"
            class="ms-3 mt-3 me-3 mb-0"
            hide-details
          >
          </v-text-field>
        </template>
        <template v-slot:item="{ item }">
          <tr @click="toDetail(item)" class="clickable-row">
            <td v-for="header in resultHeaders" :key="header.value">
              {{ item[header.value] }}
            </td>
          </tr>
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
.clickable-row {
  cursor: pointer;
}
</style>
