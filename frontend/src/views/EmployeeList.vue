<template>
  <div>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Email</th>
          <th>Activated</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="employee in employees" :key="employee.id">
          <td>{{ employee.id }}</td>
          <td>{{ employee.name }}</td>
          <td>{{ employee.email }}</td>
          <td>{{ employee.activated ? "Yes" : "No" }}</td>
          <td><button @click="viewDetails(employee.id)">Details</button></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      employees: []
    }
  },
  created() {
    axios.get('http://localhost:5001/employee')
      .then(response => {
        this.employees = response.data;
      })
      .catch(error => {
        console.error("There was an error fetching employees:", error);
      });
  },
  methods: {
    viewDetails(id) {
      this.$router.push({ name: 'EmployeeDetails', params: { id: id } });
    }
  }
}
</script>
