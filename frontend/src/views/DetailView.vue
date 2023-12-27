<script setup lang="ts">
import { ref, onMounted, computed, watch } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

import { Structure } from 'molstar/lib/mol-model/structure'
import type { BuiltInTrajectoryFormat } from 'molstar/lib/mol-plugin-state/formats/trajectory'
import { createPluginUI } from 'molstar/lib/mol-plugin-ui'
import { DefaultPluginUISpec } from 'molstar/lib/mol-plugin-ui/spec'
import { PluginSpec } from 'molstar/lib/mol-plugin/spec'
import { PluginConfig } from 'molstar/lib/mol-plugin/config'
import { PluginUIContext } from 'molstar/lib/mol-plugin-ui/context'
import { Script } from 'molstar/lib/mol-script/script'
import { StructureSelection } from 'molstar/lib/mol-model/structure/query'
import {
  PluginStateObject as PSO,
  PluginStateTransform
} from 'molstar/lib/mol-plugin-state/objects'
import { ParamDefinition as PD } from 'molstar/lib/mol-util/param-definition'
import { StateObject } from 'molstar/lib/mol-state'
import { Task } from 'molstar/lib/mol-task'
import 'molstar/lib/mol-plugin-ui/skin/light.scss'

import { Swiper, SwiperSlide } from 'swiper/vue'
import 'swiper/css'
import 'swiper/css/pagination'
import { Pagination, Mousewheel } from 'swiper/modules'
const modules = ref([Pagination, Mousewheel])

import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

interface ResultHeader {
  title: string
  value: string
  align: 'start' | 'center' | 'end'
  width?: string
}

interface DataItem {
  target: string
  protein_name: string
  taxonomy: string
  taxid: string
  repid: string
}
interface LoadItemsParams {
  page: number
  itemsPerPage: number
  sortBy: SortOption[]
}
interface SortOption {
  key: string
  order: 'asc' | 'desc'
}

const resultHeadersM = ref<ResultHeader[]>([
  { title: 'UniRef90 ID', value: 'target', align: 'start', width: '15%' },
  { title: 'Preotein Name', value: 'protein_name', align: 'start' },
  { title: 'Taxonomy', value: 'taxonomy', align: 'start' },
  { title: 'Taxonomy ID', value: 'taxid', align: 'start' },
  { title: 'Rep ID', value: 'repid', align: 'start' }
])
const resultHeadersF = ref<ResultHeader[]>([
  { title: 'Uniprot ID', value: 'uniprot_id', align: 'start', width: '15%' },
  { title: 'Preotein Name', value: 'protein_names', align: 'start' },
  { title: 'Gene Name', value: 'gene_names', align: 'start' },
  { title: 'DOI ID', value: 'doi_id', align: 'start' },
  { title: 'E-value', value: 'evalue', align: 'start' }
])

const serverCount = ref(0)
const serverResults = ref<DataItem[]>([])
const currentOffset = ref(0)
const searchQuery = ref('')
const countPerPage = ref(25)
const currentPage = ref(1)
const sortByParam = ref('')
const totalPages = computed(() => Math.ceil(serverCount.value / countPerPage.value))

const loadItems = async ({ page, itemsPerPage, sortBy }: LoadItemsParams) => {
  countPerPage.value = itemsPerPage
  currentOffset.value = (page - 1) * itemsPerPage
  if (sortBy.length) {
    console.log(typeof sortBy)
    const sortKey = sortBy[0].key
    const sortOrder = sortBy[0].order
    sortByParam.value = sortOrder === 'desc' ? `-${sortKey}` : sortKey
  }
  await fetchData(currentTab.value)
}

const fetchData = async (tab: 'tabM' | 'tabF') => {
  const plant = route.query.plant
  const pocket_id = route.query.pocket_id
  const params = {
    plant: plant,
    pocket_id: pocket_id,
    search: searchQuery.value,
    limit: countPerPage.value,
    offset: currentOffset.value,
    order_by: sortByParam.value
  }
  if (tab === 'tabM') {
    const response = await axios.get(`/PokeVA_api/searchMMseqs/`, { params })
    serverResults.value = response.data.results
    serverCount.value = response.data.count
  } else if (tab === 'tabF') {
    const response = await axios.get(`/PokeVA_api/searchFoldseek/`, { params })
    serverResults.value = response.data.results
    serverCount.value = response.data.count
  }
}

const route = useRoute()

const currentTab = ref<'tabM' | 'tabF'>('tabM')
const proteinName = ref('')
const uniprotID = ref('')
const geneName = ref('')
const organism = ref('')
const subcellularLocation = ref('')
const string = ref('')
const functionDescription = ref('')

const molstarParent = ref<HTMLElement | null>(null)
const changeMolstarFocus = ref(() => {})
const downloadUrl = ref('')

declare global {
  interface Window {
    molstar?: PluginUIContext
  }
}

onMounted(async () => {
  const cyto = route.query.cyto
  const plant = route.query.plant
  const pocket_id = route.query.pocket_id

  const responseDetail = await axios.get(`/PokeVA_api/searchDetail/`, {
    params: { cyto, plant, pocket_id }
  })

  proteinName.value = responseDetail.data.protein_names
  uniprotID.value = responseDetail.data.uniprot_id
  geneName.value = responseDetail.data.gene_names
  organism.value = responseDetail.data.organism
  subcellularLocation.value = responseDetail.data.subcellular_location
  string.value = responseDetail.data.string
  functionDescription.value = responseDetail.data.function_description

  const response = await axios.get(`/PokeVA_api/searchPDBQT/`, {
    params: { cyto, plant, pocket_id }
  })

  const ligandData = response.data.ligand_content
  const receptorData = response.data.receptor_content
  const complexData = response.data.complex_content
  const blobLigand = new Blob([ligandData], { type: 'chemical/x-pdb' })
  const blobReceptor = new Blob([receptorData], { type: 'chemical/x-pdb' })
  const blobComplex = new Blob([complexData], { type: 'chemical/x-pdb' })
  const blobLigandUrl = URL.createObjectURL(blobLigand)
  const blobReceptorUrl = URL.createObjectURL(blobReceptor)
  const blobComplexUrl = URL.createObjectURL(blobComplex)
  downloadUrl.value = URL.createObjectURL(blobComplex)

  if (molstarParent.value !== null) {
    molstarParent.value.addEventListener(
      'wheel',
      (event) => {
        event.stopPropagation()
      },
      { passive: false }
    )

    const MySpec: PluginSpec = {
      ...DefaultPluginUISpec(),
      config: [
        [PluginConfig.VolumeStreaming.Enabled, false],
        [PluginConfig.Viewport.ShowExpand, true],
        [PluginConfig.Viewport.ShowControls, false],
        [PluginConfig.Viewport.ShowSettings, true],
        [PluginConfig.Viewport.ShowAnimation, false]
      ],
      layout: {
        initial: {
          isExpanded: false,
          controlsDisplay: 'outside'
        }
      }
    }

    window.molstar = await createPluginUI(molstarParent.value, MySpec)
    changeMolstarFocus.value = () => {
      if (window.molstar) {
        const ligandData =
          window.molstar.managers.structure.hierarchy.selection.structures[0]?.components[1]?.cell
            .obj?.data
        const ligandLoci = Structure.toStructureElementLoci(ligandData as any)

        window.molstar.managers.camera.focusLoci(ligandLoci)
        window.molstar.managers.structure.focus.setFromLoci(ligandLoci)
      }
    }

    // const data1 = await window.molstar.builders.data.download(
    //   { url: blobReceptorUrl },
    //   { state: { isGhost: true } }
    // )

    // const data2 = await window.molstar.builders.data.download(
    //   { url: blobLigandUrl },
    //   { state: { isGhost: true } }
    // )

    const data3 = await window.molstar.builders.data.download(
      { url: blobComplexUrl },
      { state: { isGhost: true } }
    )

    // const trajectory1 = await window.molstar.builders.structure.parseTrajectory(data1, 'pdbqt')
    // const trajectory2 = await window.molstar.builders.structure.parseTrajectory(data2, 'pdbqt')
    const trajectory3 = await window.molstar.builders.structure.parseTrajectory(data3, 'pdbqt')
    // await window.molstar.builders.structure.hierarchy.applyPreset(trajectory1, 'default')
    // await window.molstar.builders.structure.hierarchy.applyPreset(trajectory2, 'default')
    await window.molstar.builders.structure.hierarchy.applyPreset(trajectory3, 'default')
  }
})
watch(currentTab, () => {
  loadItems({ page: 1, itemsPerPage: countPerPage.value, sortBy: [] })
})
</script>

<template>
  <v-app>
    <Header />
    <Footer />
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
            <v-row class="fill-height">
              <v-col class="fill-height">
                <v-card
                  class="m-0"
                  max-width="100%"
                  :title="proteinName"
                  rel="noopener"
                  variant="flat"
                ></v-card>
                <div
                  ref="molstarParent"
                  style="height: 80%; position: relative; z-index: 5; overflow: hidden"
                ></div>
                <v-row justify="space-between" class="mt-5">
                  <v-col cols="5">
                    <v-btn
                      class="text-none"
                      color="#428587"
                      size="large"
                      rounded
                      variant="flat"
                      style="min-width: 90%"
                      :href="downloadUrl" download="complex.pdb"
                    >
                      Download Complex
                    </v-btn></v-col
                  ><v-col cols="5">
                    <v-btn
                      class="text-none"
                      color="#428587"
                      size="large"
                      rounded
                      variant="flat"
                      style="min-width: 90%"
                      @click="changeMolstarFocus"
                    >
                      Show interaction
                    </v-btn>
                  </v-col>
                </v-row>
              </v-col>
              <v-col>
                <v-card class="fill-height">
                  <v-card-title class="headline blue--text">Information</v-card-title>

                  <v-card-subtitle class="pb-0">Protein name</v-card-subtitle>
                  <v-card-text class="text--primary">
                    {{ proteinName }}
                  </v-card-text>

                  <v-card-subtitle class="pb-0">Gene name</v-card-subtitle>
                  <v-card-text class="text--primary"> {{ geneName }} </v-card-text>

                  <v-card-subtitle class="pb-0">Source organism</v-card-subtitle>
                  <v-card-text class="text--primary">
                    {{ organism }}
                  </v-card-text>

                  <v-card-subtitle class="pb-0">UniProt ID</v-card-subtitle>
                  <v-card-text class="text--primary">
                    {{ uniprotID }}
                  </v-card-text>

                  <v-card-subtitle class="pb-0">Subcellular Location</v-card-subtitle>
                  <v-card-text class="text--primary">{{ subcellularLocation }}</v-card-text>
                </v-card>
              </v-col>
            </v-row>
          </swiper-slide>
          <swiper-slide>
            <v-container class="h-100">
              <v-tabs v-model="currentTab">
                <v-tab value="tabM">MMseqs Uniprot90 Hits</v-tab>
                <v-tab value="tabF">Foldseek PDB100 Hits</v-tab>
              </v-tabs>
              <v-data-table-server
                :items-per-page="20"
                :items-per-page-options="[20, 50, 100]"
                :headers="resultHeadersM"
                :items-length="serverCount"
                :items="serverResults"
                :fixed-header="true"
                @update:options="loadItems"
                v-show="currentTab === 'tabM'"
                @wheel.stop
                class="h-100"
              >
              </v-data-table-server>
              <v-data-table-server
                :items-per-page="20"
                :items-per-page-options="[20, 50, 100]"
                :headers="resultHeadersF"
                :items-length="serverCount"
                :items="serverResults"
                :fixed-header="true"
                @update:options="loadItems"
                v-show="currentTab === 'tabF'"
                @wheel.stop
                class="h-100"
              >
              </v-data-table-server>
            </v-container>
          </swiper-slide>
        </swiper>
      </v-container>
    </v-main>
  </v-app>
</template>

<style scoped>
.mySwiper {
  height: 100%;
  width: 100%;
}

.swiper-slide {
  width: 100%;
  overflow: hidden;
}
</style>
