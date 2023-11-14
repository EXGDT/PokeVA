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
        [PluginConfig.Viewport.ShowControls, true],
        [PluginConfig.Viewport.ShowSettings, true],
        [PluginConfig.Viewport.ShowAnimation, false]
      ],
      layout:{
        initial:{
          isExpanded: false,
          regionState: {top:"hidden",left:"hidden",right:"hidden",bottom:"hidden"},
        }
      }
    }

    window.molstar = await createPluginUI(molstarParent.value, MySpec)

    const data = await window.molstar.builders.data.download(
      { url: 'https://files.rcsb.org/download/3PTB.pdb' },
      { state: { isGhost: true } }
    )

    const trajectory = await window.molstar.builders.structure.parseTrajectory(data, 'pdb')
    await window.molstar.builders.structure.hierarchy.applyPreset(trajectory, 'default')

  }
})

const inputText = ref('');
watch(inputText, (newValue, oldValue) => {
  axios.post('/SMILE2pdb', { data: newValue })
    .then(response => {
      console.log(response.data);
    })
    .catch(error => {
      console.error(error);
    });
});

</script>

<template>
  <div class="input-group mb-2 mt-2">
    <span class="input-group-text">SMILE</span>
    <input type="text" class="form-control" placeholder="C=C(c1ccccc1)c2ccccc2">
  </div>
  <div ref="molstarParent" class="h-85" style="position: relative"></div>
</template>

<style>
.h-85 {
  height: 85%;
}
</style>