<script>

import {Warning} from '../assets/MessageBox.js'
import axios_ins from "../assets/axios";
import BaseLoginAndRegister from './BaseLoginAndRegister.vue'

export default {
  components: {
    BaseLoginAndRegister
  },

  data() {
    return {
      username: '',
      password: '',
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
      axios_ins.post('/api/user/login/',
          {
            'username': this.username,
            'password': this.password,
            'code': this.code
          }).then(response => {
        const cookie = response.headers['set-cookie'];
        console.log(cookie)
        console.log(response.headers)
      })
    }
  }
}
</script>

<template>
  <BaseLoginAndRegister title="Forget" sub_title1="注册" sub_link1="/register.html" sub_title2="登录" sub_link2="/login.html"></BaseLoginAndRegister>
</template>