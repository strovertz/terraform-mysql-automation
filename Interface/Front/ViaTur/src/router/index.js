import Vue from 'vue'
import VueRouter from 'vue-router'
import LoginView from "../views/LoginView.vue";
import SupplierView from "../views/SupplierView.vue";
import UserView from "../views/UserView.vue";

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  base: import.meta.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/fornecedores',
      name: 'fornecedores',
      component: SupplierView,
    },
    {
      path: '/compra-de-servico',
      name: 'compra-servicos',
      component: UserView,
    }

  ]
})

export default router
