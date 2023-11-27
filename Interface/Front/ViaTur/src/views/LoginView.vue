<template>
  <main>
    <div class="section columns is-fullheight  is-centered">
      <div v-if="!nextStep" id="main" class="column is-half  box has-text-centered">
        <h2>Login</h2>
        <br>
        <div>
          <label>Email</label>
          <br>
          <input v-model="email" id="email" type="email">
        </div>
        <div>
          <br>
          <label>Senha</label>
          <br>
          <input v-model="password" type="password" id="password">
        </div>
        <div>
          <span v-if="verifyLog">verifica se o email e senha estão corretos</span>
        </div>
        <div>
          <br>
          <button class="button is-rounded is-light" @click="loginValidation">Logar</button>
        </div>
        <div>
          <br>
          <button @click="createAccountStep" class="button is-rounded is-light " >criar uma conta </button>

        </div>
      </div>
      <div v-else-if="nextStep">

      </div>
    </div>
    <nav class="navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <a class="navbar-item">
          <h1 class="title"><strong>ViaTur</strong><br>Sua melhor escolha para turismo</h1>
        </a>
      </div>
    </nav>

    <div class="box">
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
    </div>
  </main>
</template>

<script>
import {instance} from '@/main';
export default {
  name: 'home',

  data() {
    return {
      GenderSelectedOption: '',
      birthday: '',
      cpf: '',
      addressUser: '',
      nameUser: '',
    }
  },
}
</script>

<style scoped>

</style>