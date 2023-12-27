import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'

// https://vitejs.dev/config/

const base = process.env.NODE_ENV === 'production' ? '/PHIPRD/' : '/';

export default defineConfig({
  plugins: [
    vue(),
    vueJsx(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  base: base,
  server: {
    proxy: {
      '/PokeVA_api': {
        target: 'http://172.21.66.13:8877',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/PokeVA_api/, '')
      }
    }
  }
})
