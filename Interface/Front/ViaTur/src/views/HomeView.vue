<template>
  <main>
    <nav class="navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <a class="navbar-item">
          <h1 class="title"><strong>ViaTur</strong><br>Sua melhor escolha para turismo</h1>

        </a>
      </div>
    </nav>

    <div class="box">
      <h2 class="title">Compre aqui um serviço</h2>
      <div class="box">
        <h3>Preencha seus dados para a compra</h3>
        <form>
          <div class="field">
            <label class="label">Nome completo</label>
            <div class="control">
              <input class="input" type="text" v-model="nameUser" placeholder="Diga o nome da sua empresa">
            </div>
          </div>

          <div class="field">
            <label class="label">Genero</label>
            <div class="control">
              <div class="select">
                <select v-model="GenderSelectedOption">
                  <option>Feminino</option>
                  <option>Masculino</option>
                </select>
              </div>
            </div>
          </div>

          <div class="field">
            <label class="label">CPF</label>
            <div class="control">
              <input class="input" v-model="cpf" type="text" placeholder="Digite o valor">
            </div>
          </div>

          <div class="field">
            <label class="label">Endereço</label>
            <div class="control">
              <input class="input" type="text" v-model="addressUser" placeholder="Digite o endereço">
            </div>
          </div>

          <div class="field">
            <label class="label">Data de Nascimento</label>
            <div class="control">
              <input class="input" type="date" v-model="birthday" placeholder="Digite a data">
            </div>
          </div>

        </form>
      </div>

      <div>
        <section class="section" id="Services">
        <!--
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
        -->
        </section>
      </div>
    </div>


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
            <button class="button is-link" @click="FormSend" >Adicionar</button>
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
              <button class="button is-link" @click="" >Atualizar</button>
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
              <button class="button is-link" @click="" >Excluir</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import {instance} from '@/main';
import axios from 'axios';

export default {
  name: 'home',

  data() {
    return {
      nameSupplier: '',
      dataService: '',
      priceService: '',
      descriptionService: '',
      addressService: '',
      selectedOptionService: '',
      serviceId: '',
      GenderSelectedOption: '',
      birthday: '',
      cpf: '',
      addressUser: '',
      nameUser: '',
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
  },
  methods: {
    FormSend: function () {
      instance.post('supplier', {
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
              this.selectedOption = true;

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