<template>
  <main>
    <div class="box">
      <h2 class="title">Anuncie aqui seu serviço</h2>
      <div>

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
          <label class="label">Forma de pagamento</label>
          <div class="control">
            <div class="select">
              <select v-model="selectedPayService">
                <option>Débito</option>
                <option>Crédito x2</option>
                <option>Crédito x3</option>
                <option>Crédito x4</option>
                <option>Crédito x5</option>
                <option>Crédito x6</option>
                <option>Crédito x7</option>
                <option>Crédito x8</option>
                <option>Crédito x9</option>
                <option>Crédito x10</option>
                <option>Crédito x11</option>
                <option>Crédito x12</option>
                <option>Pix</option>
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
              <label class="label">Forma de pagamento</label>
              <div class="control">
                <div class="select">
                  <select v-model="selectedPayService">
                    <option>Débito</option>
                    <option>Crédito x2</option>
                    <option>Crédito x3</option>
                    <option>Crédito x4</option>
                    <option>Crédito x5</option>
                    <option>Crédito x6</option>
                    <option>Crédito x7</option>
                    <option>Crédito x8</option>
                    <option>Crédito x9</option>
                    <option>Crédito x10</option>
                    <option>Crédito x11</option>
                    <option>Crédito x12</option>
                    <option>Pix</option>
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
              <button class="button is-link" @click="UpdateService">Atualizar</button>
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
              <button class="button is-link" @click="DeleteService">Excluir</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import {instance} from '@/main';
import axios from 'axios'

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
      selectedPayService: '',
    }
  },
  methods: {
    FormSend: function () {
      event.preventDefault();

      instance.post('/supplier', {
        'dataService': this.dataService,
        'priceService': this.priceService,
        'descriptionService': this.descriptionService,
        'addressService': this.addressService,
        'selectedOptionService': this.selectedOptionService,
        'nameSupplier': this.nameSupplier,
        'selectedPayService': this.selectedPayService
      })
          .then((response) => {
            alert('Serviço adicionado')
            this.nameSupplier = '';
            this.dataService = '';
            this.priceService = '';
            this.descriptionService = '';
            this.addressService = '';
            this.selectedOptionService = '';
            this.selectedPayService = '';

          })
          .catch((error) => {
            alert(error);
          });
    },

    UpdateService: function (){
      event.preventDefault();
      instance.put(`/supplier/${this.serviceId}`, {
        'dataService': this.dataService,
        'priceService': this.priceService,
        'descriptionService': this.descriptionService,
        'addressService': this.addressService,
        'selectedOptionService': this.selectedOptionService,
        'nameSupplier': this.nameSupplier,
        'selectedPayService': this.selectedPayService
      })
          .then((response) => {
            alert('Serviço modificado');
            this.serviceId = '';
            this.nameSupplier = '';
            this.dataService = '';
            this.priceService = '';
            this.descriptionService = '';
            this.addressService = '';
            this.selectedOptionService = '';
            this.selectedPayService = '';

          })
          .catch((error) => {
            alert(error);
          });
    },
    DeleteService: function (){
      event.preventDefault();
      instance.delete(`/supplier/${this.serviceId}`)
          .then((response) => {
            alert('exclusão com sucesso')
            this.serviceId = '';
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