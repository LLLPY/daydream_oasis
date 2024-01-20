<script>

import {Info, Warning} from '../assets/js/MessageBox.js'
import BaseLoginAndRegister from './BaseLoginAndRegister.vue'
import {axios_ins} from "../assets/js/axios";
import {goBackOrRedirect} from "../assets/js/tools";

export default {
  components: {
    BaseLoginAndRegister
  },
  data() {
    return {
      username: '',
      password: '',
      code: ''
    }
  },
  methods: {
    updateUsername(value) {
      this.username = value
    },
    updatePassword(value) {
      this.password = value
    },
    updateCode(value) {
      this.code = value
    },
    submit() {
      if (this.username.length === 0) {
        Warning('用户名不能为空!')
        return;
      }
      if (this.code.length === 0) {
        Warning('验证码不能为空!')
        return;
      }
      if (this.password.length === 0) {
        Warning('密码不能为空!')
        return;
      }
      axios_ins.post('/api/user/register/',
          {
            'username': this.username,
            'password': this.password,
            'code': this.code
          }).then(response => {
        const data = response.data
        goBackOrRedirect('/blog/')
        Info(data.message)
      })
    }
  }
}
</script>

<template>
  <BaseLoginAndRegister title="Register" sub_title1="登录" sub_link1="/login.html"
                        sub_title2="忘记密码?" sub_link2="/forget_password.html"
                        needCode='true'
                        :username="username" @updateUsername="updateUsername"
                        :password="password" @updatePassword="updatePassword"
                        :code="code" @updateCode="updateCode"
                        @submit="submit"

  ></BaseLoginAndRegister>
</template>

<style scoped>
.code-box {
  display: block;
}
</style>