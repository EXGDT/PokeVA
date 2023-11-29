<script setup lang="ts">
import { computed, ref, watch, onMounted, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'

import Center_circle from '@/assets/T2T_Proteom.svg'
import Arabidopsis_circle from '@/assets/Arabidopsis_thalinana.svg'
import Glycine_circle from '@/assets/Glycine_max.svg'
import Oryza_circle from '@/assets/Oryza_sativa.svg'
import Zea_circle from '@/assets/Zea_mays.svg'

const surroundingImages = ref([
  { src: Arabidopsis_circle, alt: 'Arabidopsis' },
  { src: Glycine_circle, alt: 'Glycine' },
  { src: Oryza_circle, alt: 'Oryza' },
  { src: Zea_circle, alt: 'Zea' }
])

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

const parentSize = ref({ width: 0, height: 0 })
const containerRef = ref<HTMLElement | null>(null)
const searchAPI = ref<string[]>([])

const cytokininsDisplay = ref(false)
const hideCytokinins = () => {
  cytokininsDisplay.value = false
}
const showCytokinins = (event: MouseEvent, imageAlt: string) => {
  event.stopPropagation()
  cytokininsDisplay.value = true
  searchAPI.value.push(imageAlt)
}

const router = useRouter()
const showDatabaseResult = (event: MouseEvent, imageAlt: string) => {
  event.stopPropagation()
  searchAPI.value.push(imageAlt)
  const plant = searchAPI.value[0]
  const cyto = searchAPI.value[1]
  router.push({
    path: '/result',
    query: {
      plant: plant,
      cyto: cyto
    }
  })
}

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
  const min_edge = Math.min(parentSize.value.width, window.innerHeight * 0.8)
  return `${min_edge / 1.95}px` //0.125x coverage, 0.6x size, 0.6x+0.6x+0.75x = 1.95x
})

const centerImageStyle = computed(() => ({
  width: centerImageSize.value,
  height: centerImageSize.value
}))

const surroundingImageSize = computed(() => {
  return `${parseFloat(centerImageSize.value) * 0.6}px`
})

const isHovered = ref(new Array(surroundingImages.value.length).fill(false))
const updateHoverState = (index: number, hover: boolean) => {
  isHovered.value[index] = hover
}

const getSurroundingImageStyle = (index: number) => {
  let baseTransform = ''
  switch (index) {
    case 0: // Top Image
      baseTransform = `translateY(calc(${centerImageSize.value} * -0.7))`
      break
    case 1: // Bottom Image
      baseTransform = `translateY(calc(${centerImageSize.value} * 0.7))`
      break
    case 2: // Left Image
      baseTransform = `translateX(calc(${centerImageSize.value} * -0.7))`
      break
    case 3:
      baseTransform = `translateX(calc(${centerImageSize.value} * 0.7))`
  }
  let hoverTransform = isHovered.value[index] ? 'scale(1.1)' : 'scale(1)'
  return {
    width: surroundingImageSize.value,
    height: surroundingImageSize.value,
    transform: `${baseTransform} ${hoverTransform}`,
    transition: 'transform 0.3s ease-in-out'
  }
}

const minEdgeSize = computed(() => {
  const min_edge = Math.min(parentSize.value.width, window.innerHeight * 0.8)
  return `${min_edge}px`
})

const centerCytoSize = computed(() => {
  const min_edge = Math.min(parentSize.value.width, window.innerHeight * 0.8)
  return `${min_edge * 0.3}px`
})

const cytokinins_list_style = (index: number) => {
  let styleObject = {
    width: centerCytoSize.value,
    height: centerCytoSize.value,
    transform: ''
  }

  switch (index) {
    case 0:
      styleObject.transform = `translate(calc(${minEdgeSize.value} * -0.35), calc(${minEdgeSize.value} * -0.35))`
      break
    case 1:
      styleObject.transform = `translate(calc(${minEdgeSize.value} * 0), calc(${minEdgeSize.value} * -0.35))`
      break
    case 2:
      styleObject.transform = `translate(calc(${minEdgeSize.value} * 0.35), calc(${minEdgeSize.value} * -0.35))`
      break
    case 3:
      styleObject.transform = `translate(calc(${minEdgeSize.value} * -0.35), calc(${minEdgeSize.value} * 0))`
      break
    case 4:
      styleObject.transform = `translate(calc(${minEdgeSize.value} * 0), calc(${minEdgeSize.value} * 0))`
      break
    case 5:
      styleObject.transform = `translate(calc(${minEdgeSize.value} * 0.35), calc(${minEdgeSize.value} * 0))`
      break
    case 6:
      styleObject.transform = `translate(calc(${minEdgeSize.value} * -0.35), calc(${minEdgeSize.value} * 0.35))`
      break
    case 7:
      styleObject.transform = `translate(calc(${minEdgeSize.value} * 0), calc(${minEdgeSize.value} * 0.35))`
      break
    case 8:
      styleObject.transform = `translate(calc(${minEdgeSize.value} * 0.35), calc(${minEdgeSize.value} * 0.35))`
  }
  return styleObject
}

const onClickOutside = (event: MouseEvent) => {
  if (containerRef.value && !containerRef.value.contains(event.target as Node)) {
    hideCytokinins()
  }
}

onMounted(() => {
  document.addEventListener('click', onClickOutside)
})

onBeforeUnmount(() => {
  document.removeEventListener('click', onClickOutside)
})
</script>

<template>
  <div
    v-if="!cytokininsDisplay"
    ref="containerRef"
    class="position-relative justify-content-center align-items-center d-flex flex-grow-1 flex-colum h-100"
  >
    <img :src="Center_circle" alt="Center Image" class="rounded-circle" :style="centerImageStyle" />

    <!-- Surrounding Images -->
    <img
      v-for="(image, index) in surroundingImages"
      :key="index"
      :src="image.src"
      :alt="image.alt"
      class="rounded-circle position-absolute surroundingImages"
      :style="getSurroundingImageStyle(index)"
      @click="showCytokinins($event, image.alt)"
    />
  </div>
  <div
    v-else
    ref="containerRef"
    class="position-relative justify-content-center align-items-center d-flex flex-grow-1 flex-colum h-100"
  >
    <img
      v-for="(image, index) in cytokinins_list"
      :src="image.src"
      :alt="image.alt"
      :style="cytokinins_list_style(index)"
      class="position-absolute"
      @click="showDatabaseResult($event, image.alt)"
    />
  </div>
</template>

<style></style>
