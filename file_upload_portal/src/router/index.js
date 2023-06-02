import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import FileUploadView from '../views/FileUploadView'
import TextToFile from '../views/TextToFile'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/navi',
    name: 'navi',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/NavigationView.vue')
  },
  {
    path: '/fup',
    name: 'fup',
    component: FileUploadView
  },
  {
    path: '/cpc',
    name: 'cpc',
    component: TextToFile
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
