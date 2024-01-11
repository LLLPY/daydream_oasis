<template>
  <div>
    <div v-if="!isLogin" class="login" @click="tapa">
      <a href="/login">登录🚪</a>
    </div>
    <div v-else class="user" @click="tapa">用户名称</div>
  </div>

</template>

<script setup>
import { ref, unref } from 'vue'
let isLogin = ref(false)
const tapa=() => {
  isLogin.value = !unref(isLogin)
}
</script>

<style scoped>

</style>