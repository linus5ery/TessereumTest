<template>
  <div>
    <div v-if="alertMessage" :class="['alert', alertType]">
      <span>{{ alertMessage }}</span>
      <button @click="closeAlert" class="close-alert">x</button>
    </div>
    <transition name="fade-slide" mode="out-in">
        <router-view @show-alert="showAlert" />
    </transition>
  </div>
</template>

<script>
export default {
  data() {
    return {
      alertMessage: '',
      alertType: ''
    }
  },
  methods: {
    showAlert(event) {
      this.alertMessage = event.message;
      this.alertType = event.type;
    },
    closeAlert() {
      this.alertMessage = '';
    },
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.fade-slide-enter-active {
  transition: opacity 1s, transform 1s;
}

.fade-slide-leave-active {
  transition: opacity 1s, transform 1s;
}

.fade-slide-enter-from, .fade-slide-leave-to {
  opacity: 0;
  transform: translateX(-30px);
}

.fade-slide-enter-to, .fade-slide-leave-from {
  opacity: 1;
  transform: translateX(0);
}

.alert {
  padding: 15px;
  margin-bottom: 20px;
  border: 1px solid transparent;
  border-radius: 4px;
  text-align: center;
}

.success {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}

.error {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
}

.close-alert {
  position: relative;
  float: right;
  background-color: transparent;
  border: none;
  cursor: pointer;
  font-size: 16px;
  line-height: 1;
  color: #767676;
}

.close-alert:focus {
  outline: none;
}

.button_custom {
  padding: 4px;
  border-radius: 5px;
  cursor: pointer;
  box-shadow: 2.5px 5px #888888;
}

.link {
  text-decoration: none;
  color: black;
  background-color: #f2f2f2;
  border: 1px solid black;
  padding: 4px;
  border-radius: 5px;
  cursor: pointer;
  box-shadow: 2.5px 5px #888888;
}

.form {
  width: 100%;
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}

.form-group {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.form-group label {
  flex: 1;
  margin-right: 16px;
}

.form-group input,
.form-group select {
  flex: 2;
}

.submit-button {
  padding: 8px 16px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.submit-button:hover {
  background-color: #0056b3;
}
</style>
