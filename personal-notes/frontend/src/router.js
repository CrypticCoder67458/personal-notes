// router.js

import { createRouter, createWebHistory } from 'vue-router'
import StartingPage from './pages/StartingPage.vue'
import LoginPage from './pages/LoginPage.vue'
import RegisterPage from './pages/RegisterPage.vue'
import ViewNotes from './components/ViewNotes.vue'

const routes = [
  { path: '/', component: StartingPage },
  { path: '/login', component: LoginPage },
  { path: '/register', component: RegisterPage },
  { path: '/notes', component: ViewNotes }
]
const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
 
