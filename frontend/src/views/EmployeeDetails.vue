<template>
  <div>
    <aside style="margin-bottom: 10px;">
      <button class="button_custom" style="margin-right: 5px;" @click="toggleActivation">
        {{ employee.activated ? "Deactivate" : "Activate" }}
      </button>
      <button class="button_custom" @click="deleteEmployee">Delete</button>
    </aside>
    <div style="margin-bottom: 10px;">
      <form @submit.prevent="update" class="form">
        <div class="form-group">
          <label>Name:</label>
          <input v-model="employee.name" type="text" required />
        </div>
        <div class="form-group">
          <label>Email:</label>
          <input v-model="employee.email" type="email" required />
        </div>
        <div class="form-group">
          <label>Address:</label>
          <input v-model="employee.address" type="text" required />
        </div>
        <div class="form-group">
          <label>Activated:</label>
          <select v-model="employee.activated">
            <option value=true>Active</option>
            <option value=false>Not Active</option>
          </select>
        </div>
        <div>
          <button type="submit" class="submit-button">Update</button>
        </div>
      </form>
    </div>
    <a class="link" href="/">Back to home</a>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      employee: {},
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
        this.$emit('show-alert', {
          message: 'Error fetching details for employee: ' + error,
          type: 'error'
        });
        this.$router.push({ name: 'EmployeeList' });
      });
  },
  methods: {
    toggleActivation() {
      this.employee.activated = !this.employee.activated;
      axios.put(`http://localhost:5001/employee/${this.employee.id}`, {
        activated: this.employee.activated
      })
      .then(() => {
        this.$emit('show-alert', {
          message: 'Success updating the activation status for employee: ' + Boolean(this.employee.activated),
          type: 'success'
        });
      })
      .catch(error => {
        console.error(`There was an error updating the activation status for employee ${this.employee.id}:`, error);
        this.$emit('show-alert', {
          message: 'Error updating the activation status for employee: ' + error,
          type: 'error'
        });
      });
    },
    update() {
      // Handle the logic to update the employee's info
      axios.put(`http://localhost:5001/employee/${this.employee.id}`, {
        activated: this.employee.activated,
        name: this.employee.name,
        email: this.employee.email,
      })
      .then(() => {
        this.$emit('show-alert', {
          message: 'Success updating the employee',
          type: 'success'
        });
      })
      .catch(error => {
        console.error(`There was an error updating the for employee ${this.employee.id}:`, error);
        this.$emit('show-alert', {
          message: 'Error updating the employee: ' + error,
          type: 'error'
        });
      });
    },
    deleteEmployee() {
      axios.delete(`http://localhost:5001/employee/${this.employee.id}`)
        .then(() => {
          this.$emit('show-alert', {
            message: 'Employee deleted successfully',
            type: 'success'
          });
          this.$router.push({ name: 'EmployeeList' });
        })
        .catch(error => {
          console.error(`There was an error deleting employee ${this.employee.id}:`, error);
          this.$emit('show-alert', {
            message: 'Error deleting employee: ' + error,
            type: 'error'
          });
        });
    }
  }
}
</script>

<style scoped>
</style>