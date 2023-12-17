<template>
    <ul id="top-box">
        <div class="head">
            <span class="title">Top</span>
            <span class="more">更多</span>
        </div>

        <li v-for="(top,index) in top_list" :key="index" class="top">
            <span class="number" :style="{ fontSize: 20-index+'px' }">{{ index+1 }}</span>
            <span class="title"> <a :href="top.id">{{ top.title }}</a> </span>
            <span class="pv">{{ top.pv }}</span>
        </li>

    </ul>
</template>

<script>

    import axios_ins from "../assets/axios";
    import {Warning} from "../assets/MessageBox";

    export default {
        data() {
            return {
                top_list: []
            }
        },
        methods: {
            top_info() {
                axios_ins.get('/api/action_log/top_stat/').then(response => {
                    const data = response.data
                    if (data.code !== '0') {
                        Warning(data.message)
                        return
                    }
                    this.top_list = data.data
                    console.log(this.top_list)
                })

            }
        },
        mounted() {
            this.top_info()
        }
    }


</script>

<style>
    #top-box {
        border: 1px solid silver;
        width: 100%;
        margin: 0.5em auto;
        border-radius: 3px;
        margin-bottom: 0;
        padding-left: 0.1em;
        padding-right: 0.1em;
        box-shadow: 0 0 4px 0 rgba(0,0,0,.1);

    }

    #top-box .top {
        border-top: 1px solid silver;
    }

    #top-box .top span {
        display: inline-block;
    }

    #top-box .top .title {
        width: 65%;
        font-size: 0.9rem;
        transition: color linear .3s;
        
    }
    #top-box .top .title:hover{
        color: skyblue;
        text-decoration: underline;
    }

    #top-box .top .number,
    #top-box .top .pv {
        width: 10%;
        text-align: center;
    }

    #top-box .top .pv {
        width: 25%;
        font-size: 0.8em;
    }

    #top-box .head .title {
        color: black;
        font-weight: 600;
    }

    #top-box .head {
        padding-left: 0.2em;
        padding-right: 0.2em;
    }

    #top-box .head .more {
        font-size: 0.6em;
        float: right;
    }

    #top-box span {
        cursor: pointer;
    }

</style>