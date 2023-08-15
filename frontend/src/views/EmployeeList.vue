<template>
  <div>
    <table class="striped-table" style="margin-bottom: 10px;">
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
          <td><button class="button_custom" @click="viewDetails(employee.id)">Details</button></td>
        </tr>
      </tbody>
    </table>
    <a class="link" href="/employee/add">Add employee</a>
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

<style scoped>
.striped-table {
  width: 100%;
  border-collapse: collapse;
  border: 1px solid lightslategray;
}

.striped-table th {
  background-color: #f2f2f2;
  text-align: center;
  padding: 8px;
}

.striped-table td {
  padding: 8px;
}

.striped-table tr:nth-child(even) {
  background-color: #f2f2f2;
}
</style>