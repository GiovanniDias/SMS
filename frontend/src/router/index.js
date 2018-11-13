import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
// import ListCourses from '@/components/Course/List'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    // {
    //   path: '/courses/',
    //   name: 'Courses',
    //   component: ListCourses
    // },
    // {
    //   path: '/students/',
    //   name: 'Students',
    //   component: ListStudents
    // }
  ]
})
