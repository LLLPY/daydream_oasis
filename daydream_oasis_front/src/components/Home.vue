<template>
  欢迎回家: {{ username }}!
  <span @click="logout">退出登录</span>
</template>
<script>

import axios_ins from "../assets/axios";
import {get_cookie, decodeByteString} from "../assets/js/tools";
import {Warning} from "../assets/MessageBox";

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
    if (!get_cookie('username')) {
      Warning('请先登录!')
      history.back()
    } else {
      this.username = decodeByteString(get_cookie('username'))
    }
  }
}

</script>

<style scoped>

</style>