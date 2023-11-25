<template>
  <main>
    <nav class="navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <a class="navbar-item">
          <h1 class="title"><strong>ViaTur</strong></h1><p class="subtitle">Sua melhor escolha para turismo</p>
        </a>
      </div>
    </nav>

    <div class="UserPanel">
      <h2>Compre aqui um serviço</h2>
      <div>

      </div>
    </div>
    <div class="SupplierPanel">
      <h2>Anuncie aqui seu serviço</h2>
      <div>
        <form class="box">

          <div class="field">
            <label class="label">Fornecedor</label>
            <div class="control">
              <input class="input" type="text" placeholder="Text input">
            </div>
          </div>

          <div class="field">
            <label class="label">Tipo de serviço</label>
            <div class="control">
              <div class="select">
                <select>
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
              <input class="input" v-model="price" type="text" placeholder="Text input">
            </div>
          </div>

          <div class="field">
            <label class="label">Endereço</label>
            <div class="control">
              <input class="input" type="text" v-model="address" placeholder="Text input">
            </div>
          </div>

          <div class="field">
            <label class="label">Data</label>
            <div class="control">
              <input class="input" type="text" v-model="data" placeholder="Text input">
            </div>
          </div>

          <div class="field">
            <label class="label">Descrição</label>
            <div class="control">
              <textarea class="textarea" v-model="description" placeholder="Textarea"></textarea>
            </div>
          </div>
          <div class="control">
            <button class="button is-link" @click="formSend" >Enviar</button>
          </div>
        </form>
      </div>
    </div>
    <div></div>
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
    }
  },
  methods: {
    formSend: function () {
      instance.post('/form', {
        'email': this.mail,
        'phone': this.phone,
        'msg': this.msg,
        'name': this.name
      })
          .then((response) => {
            if (response) {
              this.name = '';
              this.phone = '';
              this.mail = '';
              this.msg = '';
              this.confirmation = true;
              this.hidden = false;
            }
          })
          .catch((error) => {
            this.errorSend = true;
            this.errorMsg = error;
            setTimeout(() => {
              this.errorSend = false;
            }, 4000,)

          });
    },
  }
}
</script>
