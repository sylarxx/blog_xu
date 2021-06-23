import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import LearningNotes from '../views/LearningNotes.vue'
import ProjectBugs from '../views/ProjectBugs.vue'

const routes = [
  {
    path: '',
    redirect: '/home'
  },
  {
    path: '/home',
    component: Home,
    component: () => import('../views/Home.vue')
  },
  {
    path: '/learningnotes',
    component: LearningNotes,
    component: () => import('../views/LearningNotes.vue')
  },
  {
    path: '/projectbugs',
    component: ProjectBugs,
    component: () => import('../views/ProjectBugs.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
