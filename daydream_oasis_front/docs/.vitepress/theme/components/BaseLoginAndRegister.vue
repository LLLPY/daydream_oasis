<script setup>
import {Warning} from "../assets/js/MessageBox";
import {axios_ins} from "../assets/js/axios";
import {ref} from "vue";

const props = defineProps(['title', 'sub_title1', 'sub_link1', 'sub_title2', 'sub_link2', 'username', 'password', 'code', 'needCode'])
defineEmits(['submit', 'updateUsername', 'updatePassword', 'updateCode'])
let code_msg = ref('发送验证码')

function isValidPhoneNumber(phoneNumber) {
  // 使用正则表达式匹配手机号码
  let pattern = /^1[3456789]\d{9}$/;
  return pattern.test(phoneNumber);
}

function count_down() {
  let count = 60
  let interval = setInterval(function () {
    code_msg.value = count + '秒'
    if (count <= 0) {
      clearInterval(interval)
      code_msg.value = '发送验证码'
      document.getElementById('code-btn').disabled = false;
    }
    count--
  }, 1000)
}

function send_code() {
  if (code_msg.value === '发送验证码') {
    // 1.匹配手机号是否合法
    let phone_number = props.username
    if (isValidPhoneNumber(phone_number)) {
      // 请求后端发送验证码的接口
      axios_ins.post('/api/user/send_code/', {
        'mobile': phone_number,
        'action': props.title.toLowerCase()
      }).then(response => {
        let data = response.data
        if (data['code'] === '0') {
          document.getElementById('code-btn').disabled = true;
          count_down()
        }
      })
    } else {
      Warning('手机号不合法!')
    }
  }
}
</script>
<template>
  <div id="formBox">
    <h5>
      <span> <strong>{{ title }}</strong></span>
      <a :href="sub_link2">{{ sub_title2 }}</a>
      <a :href="sub_link1">{{ sub_title1 }}</a>
    </h5>
    <hr>

    <div class="input-box">
      <input class="" :value="username" @input="$emit('updateUsername', $event.target.value)" name="username"
             type="text" placeholder="请输入手机号" maxlength="20">
    </div>
    <div v-if="needCode" class="input-box code-box">
      <input class="col-10 text" :value="code" @input="$emit('updateCode', $event.target.value)" name="code"
             type="text" placeholder="请输入验证码"
             maxlength="20">
      <span id="code-btn" @click="send_code">{{ code_msg }}</span>
    </div>
    <div class="input-box">
      <input class="col-10 text" :value="password" @input="$emit('updatePassword', $event.target.value)" name="password"
             type="password" placeholder="请输入密码"
             maxlength="20">
    </div>
    <div class="input-box" @click="$emit('submit')" id="submit">
      Submit
    </div>
    <div class="input-box" style="border: none;text-align: right"><a href="/">Home</a></div>

  </div>

</template>


<style scoped>
#formBox {
  margin: auto auto;
  margin-top: 5% !important;
  padding: 24px !important;
  max-width: 415px;
  border: 1px solid gray;
  border-radius: 3px;
  transition: background-color .5s linear;
  background-color: rgba(0, 0, 0, 0.2);
}

@media (max-width: 450px) {
  #formBox {
    margin: auto 2%;
  }
}

#formBox:hover {
  background-color: transparent;
  box-shadow: rgba(149, 157, 165, 0.2) 0 8px 24px;
}

#formBox h5 a {
  margin-left: 5px;
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
  margin-left: 1em;
  width: 70%;
  //border: 1px solid red;
}


#code-btn {
  display: inline-block;
  width: 25%;
  font-size: 0.7rem;
  text-align: center;
  margin: 0;
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
