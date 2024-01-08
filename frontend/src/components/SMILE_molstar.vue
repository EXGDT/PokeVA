<script setup lang="ts">
import { createPluginUI } from 'molstar/lib/mol-plugin-ui'
import { DefaultPluginUISpec } from 'molstar/lib/mol-plugin-ui/spec'
import { PluginSpec } from 'molstar/lib/mol-plugin/spec'
import { PluginConfig } from 'molstar/lib/mol-plugin/config'
import { PluginUIContext } from 'molstar/lib/mol-plugin-ui/context'
import { ref, onMounted, watch } from 'vue'
import axios from 'axios'
import 'molstar/lib/mol-plugin-ui/skin/light.scss'

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

// const inputText = ref('');
// watch(inputText, (newValue, oldValue) => {
//   axios.post('/SMILE2pdb', { data: newValue })
//     .then(response => {
//       console.log(response.data);
//     })
//     .catch(error => {
//       console.error(error);
//     });
// });

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
</script>

<template>
  <v-text-field
    label="SMILE Preview & Inverse Docking"
    placeholder="C=C(c1ccccc1)c2ccccc2"
    v-model="smilesInput"
    @input="handleInputChange"
    rounded
    density="compact"
    bg-color="#FBFCF9"
    variant="solo"
  >
  </v-text-field>
  <div ref="molstarParent" class="h-80" style="position: relative"></div>
  <v-btn class="text-none mt-5 mb-2" color="#FBFCF9" size="large" rounded variant="flat" style="min-width: 95%">
    Submit an inverse docking job with our datasets
  </v-btn>
</template>

<style>
.h-80 {
  height: 80%;
}
</style>
