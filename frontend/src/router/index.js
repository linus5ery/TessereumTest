import { createRouter, createWebHistory } from 'vue-router'
import EmployeeList from './../views/EmployeeList.vue'
import EmployeeDetails from './../views/EmployeeDetails.vue'

const routes = [
  { path: '/', name: 'EmployeeList', component: EmployeeList },
  { path: '/employees/:id', name: 'EmployeeDetails', component: EmployeeDetails }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
