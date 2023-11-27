<template>
  <main>
    <div class="box">
      <h2 class="title">Anuncie aqui seu serviço</h2>
      <div>
        <form>
          <div class="field">
            <label class="label">Fornecedor</label>
            <div class="control">
              <input class="input" type="text" v-model="nameSupplier" placeholder="Diga o nome da sua empresa">
            </div>
          </div>

          <div class="field">
            <label class="label">Tipo de serviço</label>
            <div class="control">
              <div class="select">
                <select v-model="selectedOptionService">
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
              <input class="input" v-model="priceService" type="text" placeholder="Digite o valor">
            </div>
          </div>

          <div class="field">
            <label class="label">Endereço</label>
            <div class="control">
              <input class="input" type="text" v-model="addressService" placeholder="Digite o endereço">
            </div>
          </div>

          <div class="field">
            <label class="label">Data</label>
            <div class="control">
              <input class="input" type="date" v-model="dataService" placeholder="Digite a data">
            </div>
          </div>

          <div class="field">
            <label class="label">Descrição</label>
            <div class="control">
              <textarea class="textarea" v-model="descriptionService" placeholder="Textarea"></textarea>
            </div>
          </div>
          <div class="control">
            <button class="button is-link" @click="FormSend">Adicionar</button>
          </div>
        </form>
      </div>
    </div>


    <div class="box">
      <div class="box">
        <h2 class="title">Edite seu serviço aqui</h2>
        <div>
          <form>
            <div class="field">
              <label class="label">Id Serviço</label>
              <div class="control">
                <input class="input" type="text" v-model="serviceId" placeholder="Coloque o numero">
              </div>
            </div>

            <div class="field">
              <label class="label">Tipo de serviço</label>
              <div class="control">
                <div class="select">
                  <select v-model="selectedOptionService">
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
                <input class="input" v-model="priceService" type="text" placeholder="Digite o valor">
              </div>
            </div>

            <div class="field">
              <label class="label">Endereço</label>
              <div class="control">
                <input class="input" type="text" v-model="addressService" placeholder="Digite o endereço">
              </div>
            </div>

            <div class="field">
              <label class="label">Data</label>
              <div class="control">
                <input class="input" type="date" v-model="dataService" placeholder="Digite a data">
              </div>
            </div>

            <div class="field">
              <label class="label">Descrição</label>
              <div class="control">
                <textarea class="textarea" v-model="descriptionService" placeholder="Textarea"></textarea>
              </div>
            </div>
            <div class="control">
              <button class="button is-link" @click="">Atualizar</button>
            </div>
          </form>
        </div>
      </div>
    </div>


    <div class="box">
      <div class="box">
        <h2 class="title">Exclua seu serviço aqui</h2>
        <div>
          <form>
            <div class="field">
              <label class="label">Id Serviço</label>
              <div class="control">
                <input class="input" type="text" v-model="serviceId" placeholder="Coloque o numero">
              </div>
            </div>
            <div class="control">
              <button class="button is-link" @click="">Excluir</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </main>
</template>

<script>

import {instance} from '@/main';

export default {
  name: 'fornecedores',

  data() {
    return {
      nameSupplier: '',
      dataService: '',
      priceService: '',
      descriptionService: '',
      addressService: '',
      selectedOptionService: '',
      serviceId: '',
    }
  },
  methods: {
    FormSend: function () {
      instance.post('supplier', {
        'dataService': this.dataService,
        'priceService': this.priceService,
        'descriptionService': this.descriptionService,
        'addressService': this.addressService,
        'selectedOptionService': this.selectedOptionService,
      })
          .then((response) => {
            alert(response);
            if (response) {
              this.dataService = '';
              this.priceService = '';
              this.descriptionService = '';
              this.addressService = '';
              this.selectedOptionService = '';
            }
          })
          .catch((error) => {
            alert(error);
          });
    },
  }
}
</script>

<style scoped>

</style>