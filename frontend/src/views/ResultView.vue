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
  align: 'start' | 'center' | 'end'
  width?: string
  sortable?: boolean
}

interface DataItem {
  pocket_id: string
  uniprot_id: string
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
  { title: 'Pocket ID', value: 'pocket_id', align: 'start', width: '22%' },
  { title: 'Uniprot ID', value: 'uniprot_id', align: 'start', width: '8%' },
  { title: 'Protein Names', value: 'protein_names', align: 'start', width: '30%' },
  { title: 'Gene Names', value: 'gene_names', align: 'start', width: '20%' },
  { title: 'PDB ID', value: 'pdb', align: 'start', sortable: false, width: '8%' },
  {
    title: 'Binding affinity',
    value: 'binding_affinity',
    align: 'start',
    width: '12%',
    sortable: false
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

const fixedData = ref({
  pocket_id: 'bestPocket',
  afdb_id: 'bestPocket',
  uniprot_id: 'bestPocket',
  protein_names: 'bestPocket',
  gene_names: 'bestPocket',
  organism: 'bestPocket',
  pdb: 'bestPocket',
  binding_affinity: -6.936
})

const serverCount = ref(0)
const serverResults = ref<DataItem[]>([])
const currentOffset = ref(0)
const searchQuery = ref('')
const filterQuery = ref('')
const countPerPage = ref(25)
const sortByParam = ref('')
const isFiltered = ref(false)

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

const filterAPIHandles = async () => {
  if (isFiltered.value) {
    filterQuery.value = ''
    isFiltered.value = false
  } else {
    filterQuery.value = 'pdb'
    isFiltered.value = true
  }
  await fetchData()
}

const loadItems = async ({ page, itemsPerPage, sortBy }: LoadItemsParams) => {
  countPerPage.value = itemsPerPage
  currentOffset.value = (page - 1) * itemsPerPage
  if (sortBy.length) {
    const orderByFields = sortBy
      .map((item) => {
        return item.order === 'desc' ? `-${item.key}` : item.key
      })
      .join(',')
    sortByParam.value = orderByFields
  } else {
    sortByParam.value = ''
  }
  await fetchData()
}

const fetchData = async () => {
  const plant = route.query.plant
  const cyto = route.query.cyto
  const params = {
    plant: plant,
    cyto: cyto,
    search: searchQuery.value,
    filter: filterQuery.value,
    limit: countPerPage.value,
    offset: currentOffset.value,
    order_by: sortByParam.value ? `${sortByParam.value},binding_affinity` : 'binding_affinity'
  }

  const response = await axios.get(`/PokeVA_api/searchAPI/`, { params })
  serverResults.value = response.data.results
  serverCount.value = response.data.count
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
        items-per-page-text="Results Per Page"
        :headers="resultHeaders"
        :items-length="serverCount"
        :items="serverResults"
        :fixed-header="true"
        :multi-sort="true"
        :options.sync="options"
        density="compact"
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
            hide-details
            class="ms-3 mt-3 me-3 mb-0"
          >
            <template v-slot:append>
              <v-btn
                :color="isFiltered ? 'secondary' : '#4d898d'"
                rounded
                v-model="filterQuery"
                @click="filterAPIHandles"
              >
                Only PDB
              </v-btn>
            </template>
          </v-text-field>
        </template>
        <template v-slot:item="{ item }">
          <tr>
            <td>
              <span
                @click.stop="toDetail(item)"
                class="clickable-row ellipsis-text"
                style="max-with: 16vw"
              >
                {{ item.pocket_id }}
              </span>
            </td>
            <td>
              <span> {{ item.uniprot_id }} </span>
            </td>
            <td class="ellipsis-text" style="max-width: 24vw">
              <v-tooltip activator="parent" location="bottom">{{ item.protein_names }}</v-tooltip>
              <span :title="item.protein_names"> {{ item.protein_names }} </span>
            </td>
            <td class="ellipsis-text" style="max-width: 16vw">
              <v-tooltip activator="parent" location="bottom">{{ item.gene_names }}</v-tooltip>
              <span> {{ item.gene_names }} </span>
            </td>
            <td>
              <span> {{ item.pdb }} </span>
            </td>
            <td>
              <span> {{ item.binding_affinity }} </span>
            </td>
          </tr>
        </template>
        <template v-slot:body.append>
          <tr>
            <td style="color: red">{{ fixedData.pocket_id }}</td>
            <td style="color: red">{{ fixedData.uniprot_id }}</td>
            <td style="color: red">{{ fixedData.protein_names }}</td>
            <td style="color: red">{{ fixedData.gene_names }}</td>
            <td style="color: red">{{ fixedData.pdb }}</td>
            <td style="color: red">{{ fixedData.binding_affinity }}</td>
          </tr>
        </template>
      </v-data-table-server>
    </v-main>
  </v-app>
</template>

<style>
.plant_select {
  background-color: #4d898d;
}
.cyto_select {
  background-color: #d7e5e7;
}
.clickable-row {
  cursor: pointer;
}

.ellipsis-text {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* .v-table thead th span {
  white-space: nowrap;
} */
</style>
