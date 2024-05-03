<template>
  <div class="nav">
    <div class="login">
      <div v-if="isLogin" @click="goLogin" class="block">
        <el-avatar
          :size="25"
          :src="user.avatar"
          :alt="user.username"
          :title="user.username"
        />
      </div>
      <div v-else @click="goLogin">登录</div>
    </div>
  </div>
</template>

<script setup>
import { ref, unref } from "vue";
import { get_user_info } from "../assets/js/tools";

const goLogin = () => {
  if (isLogin.value) {
    // 跳转到个人中心
    location.href = "/home";
  } else {
    // 跳转到登录页面
    location.href = "/login";
  }
};

const initView = () => {
  let data = get_user_info();
  if (Object.keys(data).length) {
    isLogin.value = true;
  }
  user = unref(data);
};

let isLogin = ref(false);
let user = ref();

initView();
</script>

<style scoped>
.nav {
  display: flex;
  align-items: center;
  height: 100%;
}

.block {
  display: flex;
  align-items: center;
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
      content: "";
      display: block;
      clear: both;
      width: 1px;
      height: 24px;
      background-color: var(--vp-c-divider);
    }
  }
}
</style>
