<template>
    <br>
    <div id="action-box">
<span class="iconfont">
  <svg class="icon" aria-hidden="true" :class="{active:false}"><use xlink:href="#icon-fenxiang"></use></svg>
  <span class="counter">{{ shared_count }}</span>
</span>
        <span class="iconfont">
  <svg class="icon" aria-hidden="true" :class="{active:has_collected}"><use xlink:href="#icon-shoucang-shoucang"
                                                                            @click="wrap_collect"></use></svg>
  <span class="counter">{{ collected_count }}</span>

</span>
        <span class="iconfont">
  <svg class="icon" aria-hidden="true" :class="{active:has_liked}"><use xlink:href="#icon-dianzan_kuai"
                                                                        @click="wrap_like"></use></svg>
  <span class="counter">{{ liked_count }}</span>
</span>
    </div>

</template>

<script>

import axios_ins from '../assets/axios'
import {Warning} from "../assets/MessageBox";

    export default {
        data() {
            return {
                blog_id: null,
                has_liked: false,
                liked_count: 0,
                has_collected: false,
                collected_count: 0,
                shared_count: 0
            }
        },
        methods: {
            get_blog_id() {
                // 获取blog的id
                this.blog_id = document.getElementsByClassName('info-box')[0].id
            },
            get_action_info() {

                axios_ins.get('/api/blog/' + this.blog_id + '/action_info/').then(response => {
                    const data = response.data.data
                    this.has_liked = data.has_liked
                    this.liked_count = data.liked_count
                    this.has_collected = data.has_collected
                    this.collected_count = data.collected_count
                    this.shared_count = data.shared_count

                })
            },
            like() {
                //   点赞
                axios_ins.post('/api/blog/' + this.blog_id + '/like/').then(response => {
                    const data = response.data
                    if (data.code === '0') {
                        this.liked_count += 1
                        this.has_liked = true

                    }else{
                        Warning(data.message)
                    }
                    
                })
            },
            cancel_like() {
                //   点赞
                axios_ins.post('/api/blog/' + this.blog_id + '/cancel_like/').then(response => {
                    const data = response.data
                    if (data.code === '0') {
                        this.liked_count -= 1
                        this.has_liked = false

                    }else{
                        Warning(data.message)
                    }
                    
                })
            },
            wrap_like(){
                if(this.has_liked){
                    this.cancel_like()
                }else{
                    this.like()
                }
            },

            collect() {
                //   收藏
                axios_ins.post('/api/blog/' + this.blog_id + '/collect/').then(response => {
                    const data = response.data
                    if (data.code === '0') {
                        this.collected_count += 1
                        this.has_collected = true
                    } else {
                        Warning(data.message)

                    }
                })
            },
            cancel_collect() {
                //   收藏
                axios_ins.post('/api/blog/' + this.blog_id + '/cancel_collect/').then(response => {
                    const data = response.data
                    if (data.code === '0') {
                        this.collected_count -= 1
                        this.has_collected = false
                    } else {
                        Warning(data.message)

                    }
                })
            },
            wrap_collect(){
                if(this.has_collected){
                    this.cancel_collect()
                }else{
                    this.collect()
                }
            },


        },
        mounted() {
            this.get_blog_id()
            this.get_action_info()

        },
        created() {

        }

    }


</script>

<style scoped>
    #action-box {
        margin-top: 10px;
        overflow: hidden;
        padding: 0.2em;
    }


    #action-box .iconfont {
        font-size: 1em;
        float: right;
        margin-right: 2em;
        border-radius: 3px;
        text-align: center;
    }

    #action-box .iconfont:first-child {
        margin-right: 0;
    }

    span:hover {
        cursor: pointer;
    }

    .icon {
        width: 1.2em;
        height: 1.2em;
        vertical-align: -0.15em;
        fill: gray;
        overflow: hidden;
        transition: fill 0.5s linear;
    }

    #action-box span .icon:hover,
    #action-box span .active {
        fill: skyblue;
    }

    #action-box span .counter {
        height: 1em;
        width: 100%;
        display: inline-block;
        text-align: center;
        line-height: 1em;
        font-size: 0.9em;
    }


</style>