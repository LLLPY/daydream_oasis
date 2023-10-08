<template>
  <div id="formBox">
    <h5>
      <span>登录<svg class="icon" aria-hidden="true"><use xlink:href="#icon-login"></use></svg></span>
      <a href="#">
        <svg class="icon" aria-hidden="true">
          <use xlink:href="#icon-wangjimima"></use>
        </svg>
        忘记密码?</a>
      <a href="#">
        <svg class="icon" aria-hidden="true">
          <use xlink:href="#icon-zhuce"></use>
        </svg>
        注册</a>
    </h5>
    <hr>

    <div class="input-box">
      <svg class="icon" aria-hidden="true">
        <use xlink:href="#icon-jurassic_user"></use>
      </svg>
      <input class="" v-model="username" name="username" type="text" placeholder="请输入用户名/手机号" maxlength="20">
    </div>
    <div class="input-box">
      <svg class="icon" aria-hidden="true">
        <use xlink:href="#icon-mima"></use>
      </svg>
      <input class="col-10 text" v-model="password" name="password" type="password" placeholder="请输入密码"
             maxlength="20">
    </div>
    <div class="input-box" @click="submit" id="submit">
      登&nbsp;&nbsp;&nbsp;录
    </div>
    <div class="input-box" style="border: none;text-align: right"><a href="/">回到首页</a></div>

  </div>

</template>


<script>

import {Warning} from '../assets/MessageBox.js'
import axios from 'axios'

export default {
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

<style>


#formBox {
  margin: auto auto;
  margin-top: 5% !important;
  padding: 5% !important;
  padding-bottom: 0 !important;
  max-width: 450px;
  border: 1px solid gray;
  border-radius: 3px;
  transition: background-color .5s linear;
  background-color: rgba(0, 0, 0, 0.3);
}

#formBox:hover {
  background-color: transparent;
}

#formBox h5 {
  border: 1px solid red;
}

.icon {
  width: 1.2em;
  height: 1.2em;
  display: inline-block;
  color: red;
}

#formBox h5 a {
  float: right;
}

.input-box {
  height: 46px;
  line-height: 40px;
  margin-top: 25px !important;
  border: silver 2px solid;
  border-radius: 50px;
  padding-left: 0.2em;
}

input {
  background-color: transparent;
  border: none;
}

#code-box {
  position: relative;
}

#code {
  position: absolute;
  right: 5%;
  cursor: pointer;
  background-color: rgba(0, 0, 0, 0);
  border: none;
  outline: none;
}

#submit {
  background: #0096e6;
  font-size: 1.2rem;
  cursor: pointer;
  text-align: center;
}

.input-box .iconfont, #code, a {
  color: #009688;
}
</style>
