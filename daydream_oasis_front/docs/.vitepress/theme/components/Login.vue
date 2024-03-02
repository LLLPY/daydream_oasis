<script>
import { Warning, Info } from "../assets/js/MessageBox.js";
import { axios_ins } from "../assets/js/axios";
import BaseLoginAndRegister from "./BaseLoginAndRegister.vue";
import { goBackOrRedirect } from "../assets/js/tools";

export default {
  components: {
    BaseLoginAndRegister,
  },
  data() {
    return {
      username: "",
      password: "",
      code: "",
    };
  },
  methods: {
    updateUsername(value) {
      this.username = value;
    },
    updatePassword(value) {
      this.password = value;
    },
    submit() {
      if (this.username.length === 0) {
        Warning("用户名不能为空!");
        return;
      }

      if (this.password.length === 0) {
        Warning("密码不能为空!");
        return;
      }
      axios_ins
        .post("/api/user/login/", {
          username: this.username,
          password: this.password,
          code: this.code,
        })
        .then((response) => {
          const data = response.data;
          if (data.code === "0") {
            Info(data.message);
            // 用户信息写入local storage，用于discuss的评论
            let discuss_data =
              JSON.parse(localStorage.getItem("discuss")) || {};
            discuss_data.nick = data.data.username;
            discuss_data.mail = data.data.email;
            console.log(discuss_data);
            localStorage.setItem("discuss", JSON.stringify(discuss_data));
            goBackOrRedirect("/blog/");
          }
        });
    },
  },
};
</script>
<template>
  <BaseLoginAndRegister
    title="Login"
    sub_title1="注册"
    sub_link1="/register.html"
    sub_title2="忘记密码?"
    sub_link2="/forget_password.html"
    needCode=""
    :username="username"
    @updateUsername="updateUsername"
    :password="password"
    @updatePassword="updatePassword"
    @submit="submit"
  ></BaseLoginAndRegister>
</template>

<style scoped>
.code-box {
  display: none;
}
</style>
