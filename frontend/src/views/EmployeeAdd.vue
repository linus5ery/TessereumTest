<template>
  <div>
    <h2>Add Employee</h2>
    <form @submit.prevent="addEmployee" class="form">
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
        <button type="submit" class="submit-button">Add Employee</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      employee: {
        name: "",
        email: "",
        address: "",
        activated: true
      }
    };
  },
  methods: {
    async addEmployee() {
      try {
        const response = await axios.post("http://localhost:5001/employee", this.employee);
        if (response.data) {
            this.$emit("show-alert", {
            message: "Success adding employee",
            type: "success"
            });
          this.$router.push({ name: "EmployeeList" });
        }
      } catch (error) {
        this.$emit("show-alert", {
          message: "Error adding employee: " + error,
          type: "error"
        });
      }
    }
  }
};
</script>

<style>
</style>