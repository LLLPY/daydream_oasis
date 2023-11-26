<script setup>
import { useData } from 'vitepress'
import axios_ins from "../assets/axios";
import '../assets/font/iconfont'
import '../assets/font/iconfont.css'
import '../assets/css/blog_info.css'
const { params } = useData()
const blog = params.value

function upload_action() {
    let res = axios_ins.post('/api/action_log/upload_action/', {
        action: 6,
        cost_time: 0,
        blog_id: blog.id
    })
    console.log(res)
}

upload_action()

</script>

<template>
    <div class="info-box">
        <h1>{{ blog.title }}</h1>
        <span class="author">作者:<a href="#">{{ blog.author_username }}</a></span>
        <span class="category">分类:<a href="#">{{ blog.category }}</a></span>
        <span id="tag-list" v-if="blog.tag_list.length">标签: <span v-for="tag in blog.tag_list" class="tag"><a href="#">{{ tag
        }}</a></span> </span>
        <span>浏览量:{{ blog.pv }}</span>
        <span>阅读量:{{ blog.read_times }}</span>
        <span>预计阅读时长:{{ blog.read_time }}</span>
        <span>创建时间:{{ blog.create_time }}</span>
        <span>更新时间:{{ blog.update_time }}</span>
        <hr />
    </div>
</template>