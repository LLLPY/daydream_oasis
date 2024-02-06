<template>
  <div class="info-box" :id="blog.id">
    <h1>{{ blog.title }}</h1>
    <span class="author">作者:<a href="#">{{ blog.author.username }}</a></span>
    <span class="category">分类:<a href="#">{{ blog.category }}</a></span>
    <span id="tag-list" v-if="blog.tag_list.length">标签: <span v-for="tag in blog.tag_list" class="tag"><a href="#">{{
        tag
      }}</a></span> </span>
    <span>浏览量:{{ blog.pv }}</span>
    <span>阅读量:{{ blog.read_times }}</span>
    <span>预计阅读时长:{{ blog.read_time }}</span>
    <span>创建时间:{{ blog.create_time }}</span>
    <span>更新时间:{{ blog.update_time }}</span>
    <span class="edit" @click="edit_blog">编辑</span>
    <span class="delete" @click="delete_blog">删除</span>
    <hr/>
  </div>
  <div v-html="blog.html"/>

</template>
<script setup>
import {axios_ins} from "../assets/js/axios"
import '../assets/font/iconfont.css'
import {Info} from "../assets/js/MessageBox"
import markdownit from 'markdown-it'
import {ref} from 'vue'
import {get_url_params} from "../assets/js/tools.js";

const md = markdownit()
const params = get_url_params()

// 根据博客id拿到博客的完整信息
let blog = ref({id: params.id})

async function get_blog_info() {
  let response = await axios_ins.get(`/api/blog/${blog.value.id}/`)
  if (response.data.code === '1') {
    window.history.back()
  } else {
    blog.value = response.data.data
    blog.value.html = md.render(blog.value.content)
  }

}
get_blog_info()

function upload_action() {
  let res = axios_ins.post('/api/action_log/upload_action/', {
    action: 6,
    cost_time: 0,
    blog_id: blog.id
  })
}

function delete_blog() {
  let res = confirm('确认删除吗?')
  if (res) {
    axios_ins.delete(`/api/blog/${blog.id}/`).then(response => {
      let data = response.data
      window.location.href = '/blog/'
      Info(data['message'])
    })
  }
}

function edit_blog() {
  axios_ins.put(`/api/blog/${blog.id}/`).then(response => {
    let data = response.data
    window.location.href = '/write'
    Info(data['message'])
  })
}

</script>

<style>
.info-box span {
  display: inline-block;
  font-size: 0.8em;
  margin: 0.2em;
}

a {
  text-decoration: none;
}

.vp-doc h2 {
  border-top: none !important;
  margin-top: 24px !important;
}

.info-box .edit,
.info-box .delete:hover {
  cursor: pointer;
}
</style>
