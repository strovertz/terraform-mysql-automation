<template>
  <main>
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
              <button class="button">Comprar</button>
            </article>
          </div>
        </div>

    </section>
  </main>
</template>

<script>
import {instance} from '@/main.js';
export default {
  name: 'compra-servicos',
  data() {
    return {
      currentServices: [],
      errorGetService: '',
      serviceErrorMsg: '',
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
  }
}
</script>

<style scoped>

</style>