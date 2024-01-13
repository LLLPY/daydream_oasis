<template>
  欢迎回家: {{ username }}!
  <span @click="logout">退出登录</span>
</template>
<script>

import axios_ins from "../assets/axios";
import {get_cookie, decodeByteString} from "../assets/js/tools";

export default {
  data() {
    return {
      username: ''
    }
  },
  methods: {
    logout() {
      axios_ins.post('/api/user/logout/',).then(response => {
        let data = response.data
        console.log(data)
        window.history.back();
        location.reload();

      })
    }
  },
  mounted() {
    this.username = decodeByteString(get_cookie('username'))
  }
}

</script>

<style scoped>

</style>