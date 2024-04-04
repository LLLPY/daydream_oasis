<template>
  欢迎回家: {{ username }}!
  <span @click="logout">退出登录</span>
</template>
<script>
import { axios_ins } from "../assets/js/axios";
import { get_cookie, ord2char } from "../assets/js/tools";
import { Warning } from "../assets/js/MessageBox";

export default {
  data() {
    return {
      username: "",
    };
  },
  methods: {
    logout() {
      axios_ins.post("/api/user/logout/").then((response) => {
        history.go(-1);
        location.reload();
      });
    },
  },
  mounted() {
    if (!get_cookie("auth_token")) {
      Warning("请先登录!");
      history.go(-1);
    } else {
      this.username = ord2char(get_cookie("username"));
    }
  },
};
</script>

<style scoped></style>
