<template>
  <main>
    <nav class="navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <a class="navbar-item">
          <h1 class="title"><strong>ViaTur</strong><br>Sua melhor escolha para turismo</h1>
        </a>
        <button class="button" ><RouterLink to="/fornecedores" >area do fornecedor</RouterLink></button>
      </div>
    </nav>
    <section class="section" id="Services">
        <p class="column has-text-centered title">Nossos serviços</p>
        <div class=" has-text-centered ">
          <div class=" columns is-multiline is-centered">
            <span v-if="errorGetService" class="">{{ serviceErrorMsg }}</span>
            <article class="column is-one-third box mosaicService" v-for="services in currentServices" :key="services.id">
              <i></i>
              <p class="title">{{services.tipo_servico}}</p>
              <p>{{services.descricao}}</p>
              <p>valor: {{services.valor}}</p>
              <p>forma de pagamento: {{services.tipo_pagamento}}</p>
              <p>data partida: {{services.data}}</p>
              <p >fornecedor: {{ services.nome }}</p>
              <button class="button" @click="buy(services.id, services.valor)">Comprar</button>
            </article>
          </div>
        </div>

    </section>
  </main>
</template>

<script>
import {instance} from '@/main.js';
import Cookies from 'js-cookie'
export default {
  name: 'compra-servicos',
  data() {
    return {
      currentServices: [],
      errorGetService: '',
      serviceErrorMsg: '',
      userMail: '',
    }
  },

  created() {
    instance.get('supplier')
    .then((response) => {
      this.currentServices = response.data.services;
      console.log(response.data);
    })
    .catch((error) => {
      this.errorGetService = true;
      this.serviceErrorMsg = error;
    })
  },
  methods: {

    buy: function (serviceId, servicePrice){
      this.userMail = Cookies.get('email');
      instance.post('service', {
        serviceId,
        'userMail' : this.userMail,
        servicePrice

      })
          .then((Response)=>{
            alert('Produto no carrinho')
          })
          .catch((error)=>{
            alert('Error ao comprar')
      })
    }
  }
}
</script>

<style scoped>

</style>