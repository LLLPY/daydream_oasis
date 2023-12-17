<script>

import {Warning} from '../assets/MessageBox.js'
import axios from 'axios'
import BaseLoginAndRegister from './BaseLoginAndRegister.vue'

export default {
  components: {
    BaseLoginAndRegister
  },

  data() {
    return {
      username: 'root',
      password: '1234',
      code: '1234'
    }

  },
  methods: {
    submit(event) {
      // 阻止默认事件
      event.preventDefault();
      if (this.username.length === 0) {
        Warning('用户名不能为空!')
        return;
      }

      if (this.password.length === 0) {
        Warning('密码不能为空!')
        return;
      }
      console.log(this.password)
      axios.post('http://127.0.0.1:8000/api/user/login/',
          {
            'username': this.username,
            'password': this.password,
            'code': this.code
          }).then(response => {
        const cookie = response.headers['set-cookie'];
        console.log(cookie)
        console.log(response.headers)
      }).catch(reason => {
      })
    }
  }
}
</script>

<template>
  <BaseLoginAndRegister title="Register" sub_title1="登录" sub_link1="/login.html" sub_title2="忘记密码?" sub_link2="/forget_password.html"></BaseLoginAndRegister>
</template>