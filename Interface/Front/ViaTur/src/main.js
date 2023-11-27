import Vue from 'vue'
import { createPinia, PiniaVuePlugin } from 'pinia'
import router from './router'
import App from './App.vue'
import axios from 'axios'
const instance = axios.create({
  baseURL: 'http://127.0.0.1:8000/api'
});

import './assets/main.css'

export {instance};
Vue.use(PiniaVuePlugin, axios)

new Vue({
  router,
  pinia: createPinia(),
  render: (h) => h(App)
}).$mount('#app')
