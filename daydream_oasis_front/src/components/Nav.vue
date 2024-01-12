<template>
  <div class="nav">
    <div class="login">
      <div class="" @click="goLogin">{{ !isLogin && '登录🚪' || user }}</div>
    </div>
  </div>
</template>

<script setup>
import { ref, unref } from 'vue'
let isLogin = ref(false)
let user = ref()
const goLogin=() => {
  isLogin.value = true
  initView()
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
