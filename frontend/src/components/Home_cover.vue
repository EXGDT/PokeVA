<template>
  <img src="@/assets/Home_cover_nobg.svg" style="height: 100%; width: 100%" />
  <img src="@/assets/arrow.svg" class="arrow">
</template>

<style>
.arrow {
  position: absolute;
  height: 10%;
  width: 10%;
  left: 50%;
  bottom: 2vh;
  transform: translateX(-50%);
  animation: bounce 1.5s infinite;
}

@keyframes bounce {
  0%, 20%, 50%, 80%, 100% {
    transform: translateX(-50%) translateY(0);
  }
  40% {
    transform: translateX(-50%) translateY(1vh);
  }
  60% {
    transform: translateX(-50%) translateY(0.5vh);
  }
}
</style>
