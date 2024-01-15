<template>
  <BaseLoginAndRegister title="Login" sub_title1="注册" sub_link1="/register.html" sub_title2="忘记密码?" sub_link2="/forget_password.html"></BaseLoginAndRegister>
</template>
<script>

import {Warning, Info} from '../assets/js/MessageBox.js'
import axios_ins from "../assets/js/axios";
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

      })
    }
  }
}


</script>

