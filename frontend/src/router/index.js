import Vue from 'vue'
import Router from 'vue-router'
import Login from '../components/Login.vue'
import BookShelf from '../components/BookShelf.vue'
import Home from '../components/Home.vue'
import History from '../components/History.vue'
import User from '../components/User.vue'
import InternetSearch from '../components/InternetSearch.vue'
import Load from '../components/Load.vue'
import Novel from '../components/Novel.vue'
import test from '../components/test.vue'
import { path } from 'chromedriver'
import { compare } from 'semver'




Vue.use(Router)

const routes = [
  {
    path: '/',
    name: 'Login',
    meta: { layout: 'no-sidebar' }, // 添加元信息
    component: Login
  },
  {
    path: '/home',
    name: 'Home',
    meta: { layout: 'default' }, // 添加元信息
    component: Home
  },
  {
    path: '/bookshelf',
    name: 'BookShelf',
    meta: { layout: 'default' }, // 添加元信息
    component: BookShelf
  },
  {
    path: '/history',
    name: 'History',
    meta: { layout: 'default' }, // 添加元信息
    component: History
  },
  {
    path: '/user',
    name: 'User',
    meta: { layout: 'default' },
    component: User
  },
  {
    path: '/internetsearch',
    name: 'InternetSearch',
    meta: { layout: 'default' },
    component: InternetSearch
  },
  {
    path: '/load',
    name: 'Load',
    meta: { layout: 'default' },
    component: Load
  },
  {
    path: '/novel',
    name: 'Novel',
    meta: { layout: 'default' },
    component: Novel
  },
  {
    path: '/test',
    name:'test',
    component: test
  }

]

export default new Router({
  routes
})
