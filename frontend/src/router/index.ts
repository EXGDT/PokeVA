import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Cytokinins_select from '../components/Cytokinins_select.vue'
import smile from '../components/SMILE_molstar.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/cytokinins',
      name: 'cytokinins',
      component: Cytokinins_select
    },
    {
      path: '/smile',
      name: 'smile',
      component: smile
    }
  ]
})

export default router
