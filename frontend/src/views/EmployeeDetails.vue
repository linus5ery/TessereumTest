<template>
  <div>
    <aside>
      <button @click="toggleActivation">
        {{ employee.activated ? "Deactivate" : "Activate" }}
      </button>
      <button @click="update">Update</button>
      <button @click="deleteEmployee">Delete</button>
    </aside>
    <div>
      <h2>{{ employee.name }}</h2>
      <p>Email: {{ employee.email }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      employee: {}
    }
  },
  created() {
    const id = this.$route.params.id;
    axios.get(`http://localhost:5001/employee/${id}`)
      .then(response => {
        this.employee = response.data;
      })
      .catch(error => {
        console.error(`There was an error fetching details for employee ${id}:`, error);
      });
  },
  methods: {
    toggleActivation() {
      this.employee.activated = !this.employee.activated;
      axios.put(`http://localhost:5001/employee/${this.employee.id}`, {
        activated: this.employee.activated
      })
      .catch(error => {
        console.error(`There was an error updating the activation status for employee ${this.employee.id}:`, error);
      });
    },
    update() {
      // Handle the logic to update the employee's info
      axios.put(`http://localhost:5001/employee/${this.employee.id}`, {
        activated: this.employee.activated,
        name: this.employee.name,
        email: this.employee.email,
      })
      .catch(error => {
        console.error(`There was an error updating the activation status for employee ${this.employee.id}:`, error);
      });
    },
    deleteEmployee() {
      axios.delete(`http://localhost:5001/employee/${this.employee.id}`)
        .then(() => {
          this.$router.push({ name: 'EmployeeList' });
        })
        .catch(error => {
          console.error(`There was an error deleting employee ${this.employee.id}:`, error);
        });
    }
  }
}
</script>
