<template>
  <div class="nav">
    <div class="login">
      <div class="" @click="goLogin">{{ !isLogin && '登录🚪' || user }}</div>
    </div>
  </div>
</template>

<script setup>
import {ref} from 'vue'
import {get_cookie, decodeByteString} from '../assets/js/tools'

let isLogin = ref(false)
let user = ref()

let username = get_cookie('username')

if (username) {
  username = decodeByteString(username)
  isLogin.value = true
  user.value = username
}


const goLogin = () => {

  if (isLogin.value) {
    // 跳转到个人中心
    location.href = '/home'
  } else {
    // 跳转到登录页面
    location.href = '/login'
  }
}

const initView = () => {
  user = '白日梦想圆'
}
</script>

<style scoped>
.nav {
  display: flex;
  align-items: center;
  height: 100%;
}

.login:hover {
  cursor: pointer;
}

@media (min-width: 768px) {
  .nav {
    margin-left: 12px;

    .login {
      padding-left: 12px;
    }

    &::before {
      content: '';
      display: block;
      clear: both;
      width: 1px;
      height: 24px;
      background-color: var(--vp-c-divider);
    }
  }
}
</style>
