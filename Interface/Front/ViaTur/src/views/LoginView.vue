<template>
  <main>
    <nav class="navbar box">
      <div class="navbar-brand">
        <div class="navbar-item ">
          <router-link to="/"><img  src="https://th.bing.com/th/id/OIP.43PtV0ofraOOYDONHNAa8wHaFP?rs=1&pid=ImgDetMain.jpg" alt="Logo marca" style="width:42px;height:42px;"></router-link>
          <h1 class="title">ViaTur - Sua melhor escolha para turismo</h1>
        </div>
      </div>
      <div class="navbar-menu NavBar">
        <ul class="navbar-end" id="navbarForms">
          <li class="navbar-item">
            <router-link to="/fornecedores">Fornecedores</router-link>
          </li>
        </ul>
      </div>
    </nav>
    <div v-if="creatPanel===0" class="section columns is-fullheight  is-centered">
      <div id="main" class="column is-half  box has-text-centered">
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
          <button class="button is-rounded is-light" @click="Login">Logar</button>
        </div>
        <div>
          <br>
          <button @click="createAccountStep" class="button is-rounded is-light ">criar uma conta</button>

        </div>
      </div>

    </div>


    <div class="box" v-if="creatPanel !== 0">
      <div class="box">
        <h3 class="title">Preencha seus dados para logar</h3>
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

        <div class="field">
          <label class="label">Email</label>
          <div class="control">
            <input class="input" v-model="email" type="text" placeholder="Digite o valor">
          </div>
        </div>

        <div class="field">
          <label class="label">Senha</label>
          <div class="control">
            <input class="input" v-model="password" type="text" placeholder="Digite o valor">
          </div>
        </div>
        <div>
          <span v-if="verifyLog">verifique se os dados estão corretos</span>
        </div>
        <button class="button" @click="CreateAccount">Criar Conta</button>
      </div>
    </div>
  </main>
</template>

<script>
import {instance} from '@/main';
import router from "@/router";
import Cookies from 'js-cookie'

export default {
  name: 'home',

  data() {
    return {
      GenderSelectedOption: '',
      birthday: '',
      cpf: '',
      addressUser: '',
      nameUser: '',
      creatPanel: 0,
      email: '',
      password: '',
      verifyLog: false,
    }
  },
  methods: {
    createAccountStep: function () {
      this.creatPanel = 1;
    },
    Login: function (){
      instance.get('userCreate',  {params: {email: this.email, password: this.password}})
          .then((Response)=>{
            console.log(Response.data.id)
            Cookies.set('email', this.email);
            router.push({path: '/compra-de-servico'});
          })
          .catch((error)=>{
            window.setTimeout(()=> {
              this.verifyLog = true;
            }, 2000)
          });
    },
    CreateAccount: function (){
      instance.post(`userCreate`,{
        'GenderSelectedOption': this.GenderSelectedOption,
        'birthday': this.birthday,
        'cpf': this.cpf,
        'addressUser': this.addressUser,
        'nameUser': this.nameUser,
        'email': this.email,
        'password': this.password,
      })
          .then((Response)=>{
            alert('conta criada');
            Cookies.set('email', this.email);
            router.push({path: '/compra-de-servico'});
          })
          .catch((error)=> {
              window.setTimeout(()=>{
                this.verifyLog = true;
            }, 2000)
          });
    },
  }
}
</script>

<style scoped>

</style>