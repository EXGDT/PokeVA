import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HomeViewV from '../views/HomeViewV.vue'
import ResultView from '../views/ResultView.vue'
import menu from '../components/Menu.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/homev',
      name: 'homev',
      component: HomeViewV
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
      path: '/result',
      name: 'result',
      component: ResultView
    },
    {
      path: '/menu',
      name: 'menu',
      component: menu
    }
  ]
})

export default router
