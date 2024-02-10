<script>

import { Info, Warning } from '../assets/js/MessageBox.js'
import { axios_ins } from "../assets/js/axios";
import BaseLoginAndRegister from './BaseLoginAndRegister.vue'
import { goBackOrRedirect } from "../assets/js/tools";

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
      axios_ins.post('/api/user/modify_password/',
        {
          'username': this.username,
          'password': this.password,
          'code': this.code
        }).then(response => {
          const data = response.data
          if (data.code === '0') {
            Info(data.message)
            goBackOrRedirect('/blog/')

          }
        })
    }
  }
}
</script>

<template>
  <BaseLoginAndRegister title="Forget" sub_title1="注册" sub_link1="/register.html" sub_title2="登录" sub_link2="/login.html"
    needCode='true' :username="username" @updateUsername="updateUsername" :password="password"
    @updatePassword="updatePassword" :code="code" @updateCode="updateCode" @submit="submit"></BaseLoginAndRegister>
</template>
