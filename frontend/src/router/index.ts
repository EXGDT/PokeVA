import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ResultView from '../views/ResultView.vue'
import DetailView from '../views/DetailView.vue'
import JobView from '../views/JobView.vue'

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
      path: '/result',
      name: 'result',
      component: ResultView
    },
    {
      path: '/detail',
      name: 'detail',
      component: DetailView
    },
    {
      path: '/job',
      name: 'job',
      component: JobView
    },
  ]
})

export default router
