import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Session from '@/components/Session'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/courses/',
      name: 'Courses',
      component: Session
    },
    {
      path: '/students/',
      name: 'Students',
      component: Session
    }
  ]
})
