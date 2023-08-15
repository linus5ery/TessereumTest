import { createRouter, createWebHistory } from 'vue-router'
import EmployeeList from './../views/EmployeeList.vue'
import EmployeeDetails from './../views/EmployeeDetails.vue'
import EmployeeAdd from './../views/EmployeeAdd.vue'

const routes = [
  { path: '/', name: 'EmployeeList', component: EmployeeList },
  { path: '/employee/:id', name: 'EmployeeDetails', component: EmployeeDetails },
  { path: '/employee/add', name: 'EmployeeAdd', component: EmployeeAdd },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
