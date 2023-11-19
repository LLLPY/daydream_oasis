<template>
  <BaseLoginAndRegister title="Login" sub_title1="注册" sub_link1="/register.html" sub_title2="忘记密码?" sub_link2="/forget_password.html"></BaseLoginAndRegister>
</template>
<script>

import {Warning, Info} from '../assets/MessageBox.js'
import axios_ins from "../assets/axios";
import BaseLoginAndRegister from './BaseLoginAndRegister.vue'


export default {
  extends:BaseLoginAndRegister,
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
      axios_ins.post('/api/user/login/',
          {
            'username': this.username,
            'password': this.password,
            'code': this.code
          }).then(response => {
          const data = response.data
          Info(data.message)
        const cookie = response.headers['set-cookie'];
        console.log(cookie)
        console.log(response.headers)
        console.log(document.referrer)
      })
    },
    fun(){
      console.log(66666)
    }
  }
}


</script>

