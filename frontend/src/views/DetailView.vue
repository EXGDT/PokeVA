<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
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

const resultHeaders = ref([
  { title: 'UniRef90 ID', value: 'target', align: 'start', width: '15%' },
  { title: 'Preotein Name', value: 'protein_name', align: 'start' },
  { title: 'Taxonomy', value: 'taxonomy', align: 'start' },
  { title: 'Taxonomy ID', value: 'taxid', align: 'start' },
  { title: 'Rep ID', value: 'repid', align: 'start' }
])

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
  await fetchData()
}

const fetchData = async () => {
  const plant = route.query.plant
  const pocket_id = route.query.pocket_id
  try {
    const params = {
      plant: plant,
      pocket_id: pocket_id,
      search: searchQuery.value,
      limit: countPerPage.value,
      offset: currentOffset.value,
      order_by: sortByParam.value
    }

    const response = await axios.get(`http://172.21.66.13:8877/searchMMseqs/`, { params })
    serverResults.value = response.data.results
    serverCount.value = response.data.count
  } catch (error) {
    console.error(error)
  }
}

const route = useRoute()

const currentTab = ref('tabM')
const proteinName = ref('')
const uniprotID = ref('')
const geneName = ref('')
const organism = ref('')
const subcellularLocation = ref('')
const string = ref('')
const functionDescription = ref('')

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

  const responseDetail = await axios.get(`http://172.21.66.13:8877/searchDetail/`, {
    params: { cyto, plant, pocket_id }
  })

  proteinName.value = responseDetail.data.protein_names
  uniprotID.value = responseDetail.data.uniprot_id
  geneName.value = responseDetail.data.gene_names
  organism.value = responseDetail.data.organism
  subcellularLocation.value = responseDetail.data.subcellular_location
  string.value = responseDetail.data.string
  functionDescription.value = responseDetail.data.function_description

  const response = await axios.get(`http://172.21.66.13:8877/searchPDBQT/`, {
    params: { cyto, plant, pocket_id }
  })

  const ligandData = response.data.ligand_content
  const receptorData = response.data.receptor_content
  const blobLigand = new Blob([ligandData], { type: 'chemical/x-pdb' })
  const blobReceptor = new Blob([receptorData], { type: 'chemical/x-pdb' })
  const blobLigandUrl = URL.createObjectURL(blobLigand)
  const blobReceptorUrl = URL.createObjectURL(blobReceptor)

  type MergeStructures = typeof MergeStructures
  const MergeStructures = PluginStateTransform.BuiltIn({
    name: 'merge-structures',
    display: { name: 'Merge Structures', description: 'Merge Structure' },
    from: PSO.Root,
    to: PSO.Molecule.Structure,
    params: {
      structures: PD.ObjectList(
        {
          ref: PD.Text('')
        },
        ({ ref }) => ref,
        { isHidden: true }
      )
    }
  })({
    apply({ params, dependencies }) {
      return Task.create('Merge Structures', async (ctx) => {
        if (params.structures.length === 0) return StateObject.Null

        const first = dependencies![params.structures[0].ref].data as Structure
        const builder = Structure.Builder({ masterModel: first.models[0] })
        for (const { ref } of params.structures) {
          const s = dependencies![ref].data as Structure
          for (const unit of s.units) {
            // TODO invariantId
            builder.addUnit(
              unit.kind,
              unit.model,
              unit.conformation.operator,
              unit.elements,
              unit.traits
            )
          }
        }

        const structure = builder.getStructure()
        return new PSO.Molecule.Structure(structure, { label: 'Merged Structure' })
      })
    }
  })

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

    const data1 = await window.molstar.builders.data.download(
      { url: blobReceptorUrl },
      { state: { isGhost: true } }
    )

    const data2 = await window.molstar.builders.data.download(
      { url: blobLigandUrl },
      { state: { isGhost: true } }
    )

    const trajectory1 = await window.molstar.builders.structure.parseTrajectory(data1, 'pdbqt')
    const trajectory2 = await window.molstar.builders.structure.parseTrajectory(data2, 'pdbqt')
    await window.molstar.builders.structure.hierarchy.applyPreset(trajectory1, 'default')
    await window.molstar.builders.structure.hierarchy.applyPreset(trajectory2, 'default')

    // async function loadStructuresFromUrlsAndMerge(sources: { url: string, format: BuiltInTrajectoryFormat, isBinary?: boolean }[]) {
    //   const structures: {ref: string}[] = []
    //   for (const {url, format, isBinary} of sources) {
    //     const data = await window.molstar?.builders.data.download({url, isBinary});
    //     const model = await window.molstar?.builders.structure.parseTrajectory(data, format);
    //     const modelProperties = await window.molstar?.builders.structure.insertModelProperties(model);
    //     const structure = await window.molstar?.builders.structure.createStructure(modelProperties || model);
    //     const structureProperties = await window.molstar?.builders.structure.insertStructureProperties(structure);
    //     structures.push({ref: structureProperties?.ref || structure.ref })
    //   }
    //   window.molstar?.managers.structure.hierarchy.updateCurrent(window.molstar.managers.structure.hierarchy.current.structures, 'remove');
    //   const dependsOn = structures.map(({ ref }) => ref);
    //   const data = window.molstar?.state.data.build().toRoot().apply(MergeStructures, { structures }, { dependsOn });
    //   const structure = await data?.commit();
    //   const structureProperties = await window.molstar?.builders.insertStructureProperties(structure);
    //   window.molstar?.behaviors.canvas3d.initialized.subscribe(async v => {
    //     await window.molstar?.builders.structure.representation.applyPreset(structureProperties || structure, StructurePreset)
    //   })
    // }

    // async function loadStructuresFromUrlsAndMerge(sources) {
    //   const structures = []
    //   for (const { url, format, isBinary } of sources) {
    //     const data = await window.molstar.builders.data.download({ url, isBinary })
    //     const trajectory = await window.molstar.builders.structure.parseTrajectory(data, format)
    //     const model = await window.molstar.builders.structure.createModel(trajectory)
    //     const modelProperties = await window.molstar.builders.structure.insertModelProperties(model)
    //     const structure = await window.molstar.builders.structure.createStructure(
    //       modelProperties || model
    //     )
    //     const structureProperties =
    //       await window.molstar.builders.structure.insertStructureProperties(structure)

    //     structures.push({ ref: structureProperties?.ref || structure.ref })
    //   }

    //   // 移除当前层级中的结构，以便合并
    //   window.molstar.managers.structure.hierarchy.updateCurrent(
    //     window.molstar.managers.structure.hierarchy.current.structures,
    //     'remove'
    //   )

    //   const dependsOn = structures.map(({ ref }) => ref)
    //   const mergeData = window.molstar.state.data
    //     .build()
    //     .toRoot()
    //     .apply(MergeStructures, { structures }, { dependsOn })
    //   const mergedStructure = await mergeData.commit()
    //   const mergedStructureProperties =
    //     await window.molstar.builders.structure.insertStructureProperties(mergedStructure)
    //   window.molstar.behaviors.canvas3d.initialized.subscribe(async () => {
    //     await window.molstar.builders.structure.representation.applyPreset(
    //       mergedStructureProperties || mergedStructure,
    //       StructurePreset
    //     )
    //   })
    // }

    // const data = window.molstar.managers.structure.hierarchy.current.structures[0]?.cell.obj?.data
    // if (!data) return
    // console.log(data)
    // const selection = Script.getStructureSelection(
    //   (Q) =>
    //     Q.struct.generator.atomGroups({
    //       'chain-test': Q.core.rel.eq(['B', Q.ammp('label_asym_id')])
    //     }),
    //   data
    // )
    // const loci = StructureSelection.toLociWithSourceUnits(selection)
    // console.log(loci)
  }
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
            <v-row fluid class="fill-height">
              <v-col class="fill-height">
                <div ref="molstarParent" class="h-100" style="position: relative; z-index: 5"></div>
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
                :headers="resultHeaders"
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
                :headers="resultHeaders"
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
