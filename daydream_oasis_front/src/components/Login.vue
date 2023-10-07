<template>
  <div id="formBox" class="text-center shadow-lg">
    <h5>
      <span>登录<span class="iconfont">&#xec05;</span></span>
      <a href="#"><span class="iconfont">&#xe66b;</span>忘记密码?</a>
      <a href="#"><span class="iconfont">&#xe684;</span>注册</a>
    </h5>
    <hr>

    <div class="input-box row">
      <div class="col-2 text-center"><span class="iconfont">&#xe60f;</span></div>
      <input class="col-10 text" v-model="username" name="username" type="text"
             placeholder="请输入用户名/手机号" maxlength="20">
    </div>
    <div class="input-box row">
      <div class="col-2 text-center"><span class="iconfont">&#xe728;</span></div>
      <input class="col-10 text" v-model="password" name="password" type="password" placeholder="请输入密码"
             maxlength="20">
    </div>
    <div class="input-box" @click="submit" id="submit">
      登&nbsp;&nbsp;&nbsp;录
    </div>
    <div class="input-box text-right" style="border: none;"><a href="/">回到首页</a></div>

  </div>

</template>


<script>
export default {
  data() {
    return {
      username: '',
      password: '',
    }

  },
  methods: {
    submit(event) {
      // 阻止默认事件
      event.preventDefault();
      if (this.username.length === 0) {
        return
      }

      if (this.password.length === 0) {
        toast_show('请输入密码!');
        return
      }
    }
  }
}
</script>

<style>

#formBox {
  margin: auto auto;
  margin-top: 5% !important;
  padding-left: 5% !important;
  padding-right: 5% !important;
  padding-top: 5% !important;
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
  text-align: left;
  position: relative;
  margin-bottom: 30px;
  padding-bottom: 10px;
}

#formBox h5 a {
  float: right;
}

.input-box {
  height: 46px;
  line-height: 46px;
  margin-top: 25px !important;
  border: silver 2px solid;
  border-radius: 50px;
}

.input-box .col-2, .input-box .col-10 {
  padding: 0 !important;
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
}

.input-box .iconfont, #code, a {
  color: #009688;
}
</style>
