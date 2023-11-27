<template>
  <main>
    <section class="section" id="Services">
      <h2>aaaa</h2>
        <p class="column has-text-centered title">Nossos serviços</p>
        <div class=" has-text-centered ">
          <div class=" columns is-multiline is-centered">
            <span v-if="errorGetService" class="">{{ serviceErrorMsg }}</span>
            <article class="column is-one-third box mosaicService" v-for="service in currentServices">
              <i class=""></i>
              <p class="title">{{ service.title }}</p>
              <p class="subtitle">{{ service.content }}</p>
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

    }
  },

  created() {
    instance.get('supplier')
    /*
    .then((response) => {
      this.currentServices = response.data.enabled;
    })
    .catch((error) => {
      this.errorGetService = true;
      this.serviceErrorMsg = error;
    })*/
  }
}
</script>

<style scoped>

</style>