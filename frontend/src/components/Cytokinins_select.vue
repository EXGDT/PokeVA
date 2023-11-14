<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue'
import Auxins from '@/assets/Auxins.svg'
import Cytokinins from '@/assets/Cytokinins.svg'
import Ethylene from '@/assets/Ethylene.svg'
import Gibberellin from '@/assets/Gibberellin.svg'
import Jasmonic_acid from '@/assets/Jasmonic_acid.svg'
import Salicylic_acid from '@/assets/Salicylic_acid.svg'
import Strigolactones from '@/assets/Strigolactones.svg'
import Abscisic_acid from '@/assets/Abscisic_acid.svg'
import Brassinosteroids from '@/assets/Brassinosteroids.svg'

const cytokinins_list = ref([
  { src: Auxins, alt: 'Auxins' },
  { src: Cytokinins, alt: 'Cytokinins' },
  { src: Ethylene, alt: 'Ethylene' },
  { src: Gibberellin, alt: 'Gibberellin' },
  { src: Jasmonic_acid, alt: 'Jasmonic_acid' },
  { src: Salicylic_acid, alt: 'Salicylic_acid' },
  { src: Strigolactones, alt: 'Strigolactones' },
  { src: Abscisic_acid, alt: 'Abscisic_acid' },
  { src: Brassinosteroids, alt: 'Brassinosteroids' }
])

const containerRef = ref<HTMLElement | null>(null)
const parentSize = ref({ width: 0, height: 0 })

function updateParentSize() {
  if (containerRef.value) {
    parentSize.value = {
      width: containerRef.value.offsetWidth,
      height: containerRef.value.offsetHeight
    }
  }
}

onMounted(() => {
  updateParentSize()
  const observer = new ResizeObserver(updateParentSize)
  if (containerRef.value) {
    observer.observe(containerRef.value)
  }
  watch(
    () => containerRef.value,
    (newValue, oldValue) => {
      if (oldValue) observer.unobserve(oldValue)
      if (newValue) observer.observe(newValue)
    }
  )
})

const centerImageSize = computed(() => {
  const size = Math.min(parentSize.value.width, window.innerHeight * 0.8)
  return `${size * 0.30}px`
})

const cytokinins_list_style = (index: number) => {
  let styleObject = {
    width: centerImageSize.value,
    height: centerImageSize.value,
    transform: ''
  }

  switch (index) {
    case 0:
      styleObject.transform = `translate(-25vh, -25vh)`
      break
    case 1:
      styleObject.transform = `translate(0vh, -25vh)`
      break
    case 2:
      styleObject.transform = `translate(25vh, -25vh)`
      break
    case 3:
      styleObject.transform = `translate(-25vh, 0vh)`
      break
    case 4:
      styleObject.transform = `translate(0vh, 0vh)`
      break
    case 5:
      styleObject.transform = `translate(25vh, 0vh)`
      break
    case 6:
      styleObject.transform = `translate(-25vh, 25vh)`
      break
    case 7:
      styleObject.transform = `translate(0vh, 25vh)`
      break
    case 8:
      styleObject.transform = `translate(25vh, 25vh)`
  }
  return styleObject
}

</script>

<template>
  <div
    ref="containerRef"
    class="position-relative justify-content-center align-items-center d-flex flex-grow-1 h-100 me-3"
  >
    <img
      v-for="(items, index) in cytokinins_list"
      :src="items.src"
      :alt="items.alt"
      :style="cytokinins_list_style(index)"
      class="position-absolute"
    />
  </div>
</template>
