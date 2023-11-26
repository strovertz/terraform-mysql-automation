import Vue from 'vue'
import { createPinia, PiniaVuePlugin } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios'
const instance = axios.create({
  baseURL: 'http://127.0.0.1:8000/'
});

import './assets/main.css'

export {instance};
Vue.use(PiniaVuePlugin, axios)

new Vue({
  router,
  pinia: createPinia(),
  render: (h) => h(App)
}).$mount('#app')
