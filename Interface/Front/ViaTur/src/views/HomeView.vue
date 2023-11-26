<template>
  <main>
    <nav class="navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <a class="navbar-item">
          <h1 class="title"><strong>ViaTur</strong><br><p class="subtitle">Sua melhor escolha para turismo</p></h1>

        </a>
      </div>
    </nav>

    <div class="box">
      <h2 class="title">Compre aqui um serviço</h2>
      <div>

      </div>
    </div>
    <div class="box">
      <h2 class="title">Anuncie aqui seu serviço</h2>
      <div>
        <form>
          <div class="field">
            <label class="label">Fornecedor</label>
            <div class="control">
              <input class="input" type="text" placeholder="Diga o nome da sua empresa">
            </div>
          </div>

          <div class="field">
            <label class="label">Tipo de serviço</label>
            <div class="control">
              <div class="select">
                <select v-model="selectedOption">
                  <option>Passagem Aerea</option>
                  <option>Aluguel de carro</option>
                  <option>Reserva de hotel</option>
                  <option>Reserva de onibus</option>
                  <option>Reserva de restaurante</option>
                  <option>Agencia local</option>
                </select>
              </div>
            </div>
          </div>

          <div class="field">
            <label class="label">Valor do serviço</label>
            <div class="control">
              <input class="input" v-model="price" type="text" placeholder="Digite o valor">
            </div>
          </div>

          <div class="field">
            <label class="label">Endereço</label>
            <div class="control">
              <input class="input" type="text" v-model="address" placeholder="Digite o endereço">
            </div>
          </div>

          <div class="field">
            <label class="label">Data</label>
            <div class="control">
              <input class="input" type="date" v-model="data" placeholder="Digite a data">
            </div>
          </div>

          <div class="field">
            <label class="label">Descrição</label>
            <div class="control">
              <textarea class="textarea" v-model="description" placeholder="Textarea"></textarea>
            </div>
          </div>
          <div class="control">
            <button class="button is-link" @click="formSend" >Adicionar</button>
          </div>
        </form>
      </div>
    </div>
    <div class="box">

    </div>
  </main>
</template>

<script>
import axios from 'axios';

import {instance} from '@/main';

export default {
  name: 'home',

  data() {
    return {
      data: '',
      price: '',
      description: '',
      address: '',
      selectedOption: '',
    }
  },
  methods: {
    formSend: function () {
      alert(this.selectedOption);
      instance.post('/form', {
        'data': this.data,
        'price': this.price,
        'description': this.description,
        'address': this.address,
        'option': this.selectedOption,
      })
          .then((response) => {
            if (response) {
              this.data = '';
              this.price = '';
              this.description = '';
              this.address = '';
              this.selectedOption = '';

            }
          })
          .catch((error) => {
            alert(error);
            setTimeout(() => {

            }, 4000,)

          });
    },
  }
}
</script>


<style scoped>

nav {
  background-color: #b3d7ff ;
}

textarea {
  resize: none;
}
</style>