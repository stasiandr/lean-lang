import Vue from 'vue'
import VueRouter from 'vue-router'

import Login from '../views/public/Login'
import Register from '../views/public/Register'
import Landing from '../views/public/Landing'

import Tasks from '../views/Tasks'
import Classroom from '../views/Classroom'
import Account from '../views/Account'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Landing',
    component: Landing,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
  },

  {
    path: '/account',
    name: 'Account',
    component: Account,
  },
  {
    path: '/classroom',
    name: 'Classroom',
    component: Classroom,
  },
  {
    path: '/tasks',
    name: 'Tasks',
    component: Tasks,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
})

export default router
