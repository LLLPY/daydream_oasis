<script setup>
    defineProps(['title', 'sub_title1', 'sub_link1', 'sub_title2', 'sub_link2'])
</script>
<script>

    import {Warning} from '../assets/MessageBox.js'
    import axios_ins from '../assets/axios'
    import {Info} from "../assets/MessageBox";


    export default {

        data() {
            return {
                username: '',
                password: '',
                code: '1234'
            }

        },
        methods: {
            submit(event) {
                // 阻止默认事件
                event.preventDefault();
                if (this.username.length === 0) {
                    Warning('用户名不能为空!')
                    return;
                }

                if (this.password.length === 0) {
                    Warning('密码不能为空!')
                    return;
                }
                axios_ins.post('/api/user/login/',
                    {
                        'username': this.username,
                        'password': this.password,
                        'code': this.code,
                    }).then(response => {
                    const data = response.data
                    if (data.code === '0'){
                        window.history.back();
                        location.reload();
                        Info(data.message)
                    }else{
                        Warning(data.message)
                    }

                })
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
            <svg class="icon" aria-hidden="true">
                <use xlink:href="#icon-jurassic_user"></use>
            </svg>
            <input class="" v-model="username" name="username" type="text" placeholder="请输入用户名/手机号" maxlength="20">
        </div>
        <div class="input-box">
            <svg class="icon" aria-hidden="true">
                <use xlink:href="#icon-mima"></use>
            </svg>
            <input class="col-10 text" v-model="password" name="password" type="password" placeholder="请输入密码"
                   maxlength="20">
        </div>
        <div class="input-box" @click="submit" id="submit">
            Submit
        </div>
        <div class="input-box" style="border: none;text-align: right"><a href="/">Home</a></div>

    </div>

</template>


<style scoped>


    #formBox {
        margin: auto auto;
        margin-top: 5% !important;
        padding: 5% !important;
        padding-bottom: 0 !important;
        max-width: 450px;
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


    .icon {
        width: 1.1em;
        height: 1.1em;
        display: inline-block;
        vertical-align: middle;
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
        margin-left: 0.2em;
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
        text-align: center;
    }

    .input-box .iconfont, #code, a {
        color: #009688;
    }
</style>
