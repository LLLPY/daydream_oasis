<script setup>
    defineProps(['id'])
</script>
<script>
import '../assets/font/iconfont'
import { Warning } from "../assets/MessageBox";
import axios_ins from "../assets/axios";
import '../assets/font/iconfont.css'
import '../assets/css/blog_info.css'

export default {
    data() {
        return {
            blog_id: null,
            title: null,
            author_id: null,
            author_username: null,
            pv: null,
            read_times: null,
            read_time: null,
            category: null,
            tag_list: [],
            create_time: null,
            update_time: null,
            content:null
        }
    },

    methods: {
        get_blog_id() {
            // 获取blog的id
            this.blog_id = document.getElementsByClassName('info-box')[0].id
        },
        get_tag_list() {
            let tag_str = document.getElementById('tag-list').innerText
        },
        upload_action() {
            let res = axios_ins.post('/api/action_log/upload_action/', {
                action: 6,
                cost_time: 0,
                blog_id: this.blog_id
            })
        },
        get_blog_info() {
            axios_ins.get('/api/blog/' + this.blog_id + '/').then(response => {
                let data = response.data
                if (data.code !== '0') {
                    Warning(data.message)
                } else {
                    data = data.data
                    this.title = data.title
                    this.author_username = data.author.username
                    this.pv = data.pv
                    this.read_times = data.read_times
                    this.read_time = data.read_time
                    this.category = data.category
                    this.tag_list = data.tag_list
                    this.create_time = data.create_time
                    this.update_time = data.update_time
                    // this.content = data.content

                }
                console.log(data)
            })
        }

    },
    mounted() {
        this.get_blog_id()
        this.get_blog_info()
        this.upload_action()
    }
}
</script>

<template>
    <div class="info-box" :id="id">
        <h1>{{ title }}</h1>
        <span class="author">作者:<a href="#">{{ author_username }}</a></span>
        <span class="category">分类:<a href="#">{{ category }}</a></span>
        <span id="tag-list" v-if="tag_list.length">标签:  <span v-for="tag in tag_list" class="tag"><a href="#">{{ tag }}</a></span> </span>
        <span>浏览量:{{ pv }}</span>
        <span>阅读量:{{ read_times }}</span>
        <span>预计阅读时长:{{ read_time }}</span>
        <span>创建时间:{{ create_time }}</span>
        <span>更新时间:{{ update_time }}</span>
        <hr />
    </div>
    
</template>