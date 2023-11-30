<script setup lang="ts">
import { ref, watchEffect, readonly } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()

const resultHeaders = readonly(
  ref([
    { title: 'Uniprot_id', value: 'uniprot_id', align: 'start' },
    { title: 'Protein names', value: 'protein_names', align: 'start' },
    { title: 'Gene names', value: 'gene_names', align: 'start' },
    { title: 'Organism', value: 'organism', align: 'start' },
    { title: 'PDB ID', value: 'pdb', align: 'start' },
    { title: 'Pocket ID', value: 'pocket_id', align: 'start' },
    { title: 'Binding affinity', value: 'binding_affinity', align: 'start' }
  ])
)

interface DataItem {
  uniprot_id: string
  protein_names: string
  gene_names: string
  organism: string
  pdb: string
  pocket_id: string
  binding_affinity: number
}

const itemsPerPage = ref(10)
const totalItems = ref(0)
const serverItems = ref<DataItem[]>([])
const loading = ref(true)
const fixedFooter = ref(true)
const page = ref(1)
interface LoadItemsParams {
  page: number
  itemsPerPage: number
}

const loadItems = async ({ page, itemsPerPage }: LoadItemsParams) => {
  loading.value = true
  const cyto = route.query.cyto
  const plant = route.query.plant
  const limit = itemsPerPage
  const offset = (page - 1) * itemsPerPage
  try {
    const response = await axios.get(`http://172.21.66.13:8877/searchAPI/`, {
      params: { cyto, plant, limit, offset }
    })
    serverItems.value = response.data.results
    totalItems.value = response.data.count
  } catch (error) {
    console.error(error)
  } finally {
    loading.value = false
  }
}

watchEffect(() => {
  loadItems({ page: page.value, itemsPerPage: itemsPerPage.value })
})
</script>

<template>
  <v-data-table-server
    v-model:items-per-page="itemsPerPage"
    :headers="resultHeaders"
    :items-length="totalItems"
    :items="serverItems"
    :loading="loading"
    :fixed-footer="fixedFooter"
    item-value="name"
    @update:options="loadItems"
  >
    <template v-slot:item.protein_names="{ item }">
      <div>
        <span class="text-ellipsis" :title="item.protein_names">{{ item.protein_names }}</span>
      </div>
    </template>
    <template v-slot:item.gene_names="{ item }">
      <div>
        <span class="text-ellipsis" :title="item.gene_names">{{ item.gene_names }}</span>
      </div>
    </template>
    <template v-slot:item.organism="{ item }">
      <div>
        <span class="text-ellipsis" :title="item.organism">{{ item.organism }}</span>
      </div>
    </template>
    <template v-slot:item.pocket_id="{ item }">
      <div>
        <span class="text-ellipsis" :title="item.pocket_id">{{ item.pocket_id }}</span>
      </div>
    </template>
  </v-data-table-server>
</template>

<style>
.text-ellipsis {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  display: block;
  max-width: 150px;
}
</style>
