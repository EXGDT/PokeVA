<script setup lang="ts">
import { computed, ref, watch, onMounted, onBeforeUnmount } from 'vue'
import Center_circle from '@/assets/T2T_Proteom.svg'
import Arabidopsis_circle from '@/assets/Arabidopsis_thalinana.svg'
import Glycine_circle from '@/assets/Glycine_max.svg'
import Oryza_circle from '@/assets/Oryza_sativa.svg'
import Zea_circle from '@/assets/Zea_mays.svg'
import Cytokinins_select from '@/components/Cytokinins_select.vue'

const parentSize = ref({ width: 0, height: 0 })
const containerRef = ref<HTMLElement | null>(null)

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

function updateParentSize() {
  if (containerRef.value) {
    parentSize.value = {
      width: containerRef.value.offsetWidth,
      height: containerRef.value.offsetHeight
    }
  }
}

const centerImageSize = computed(() => {
  const size = Math.min(parentSize.value.width, window.innerHeight * 0.8)
  return `${size * 0.54}px`
})

const surroundingImageSize = computed(() => {
  const size = Math.min(parentSize.value.width, window.innerHeight * 0.8)
  return `${size * 0.32}px`
})

const overlap = ref(0.015)
const surroundingImages = ref([
  { src: Arabidopsis_circle, alt: 'Arabidopsis_circle' },
  { src: Glycine_circle, alt: 'Glycine_circle' },
  { src: Oryza_circle, alt: 'Oryza_circle' },
  { src: Zea_circle, alt: 'Zea_circle' }
])

const centerImageStyle = computed(() => ({
  width: centerImageSize.value,
  height: centerImageSize.value
}))

const getSurroundingImageStyle = (index: number) => {
  const offset = parseFloat(centerImageSize.value) * overlap.value
  let styleObject = {
    width: surroundingImageSize.value,
    height: surroundingImageSize.value,
    transform: ''
  }
  switch (index) {
    case 0: // Top Image
      styleObject.transform = `translateY(calc((${centerImageSize.value}/2 + ${offset}vh) * -1))`
      break
    case 1: // Bottom Image
      styleObject.transform = `translateY(calc(${centerImageSize.value}/2 + ${offset}vh))`
      break
    case 2: // Left Image
      styleObject.transform = `translateX(calc((${centerImageSize.value}/2 + ${offset}vh) * -1))`
      break
    case 3:
      styleObject.transform = `translateX(calc(${centerImageSize.value}/2 + ${offset}vh))`
  }
  return styleObject
}

const showCytokinins = ref(false)

const toggleComponent = () => {
  showCytokinins.value = !showCytokinins.value
}

</script>

<template>
  <div
    ref="containerRef"
    v-if="!showCytokinins"
    class="position-relative justify-content-center align-items-center d-flex flex-grow-1 flex-colum h-100"
  >
    <!-- Center Image -->
    <img :src="Center_circle" alt="Center Image" class="rounded-circle" :style="centerImageStyle" />

    <!-- Surrounding Images -->
    <img
      v-for="(image, index) in surroundingImages"
      :key="index"
      :src="image.src"
      :alt="image.alt"
      class="rounded-circle position-absolute surroundingImages"
      :style="getSurroundingImageStyle(index)"
      @click="toggleComponent"
    />
  </div>
  <Cytokinins_select v-else />
</template>

<style scoped>
.surroundingImages {
  transition:
    transform 0.5s ease,
    border ease;
}

.surroundingImages:hover {
  transform: scale(1.2);
  border: 2px solid burlywood;
}
</style>
