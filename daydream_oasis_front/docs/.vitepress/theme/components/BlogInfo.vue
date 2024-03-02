<template>
  <div class="info-box" :id="blog.id">
    <h1>{{ blog.title }}</h1>
    <span class="author"
      >作者:<a href="#">{{ blog.author.username }}</a></span
    >
    <span v-if="blog.category" class="category"
      >分类:<a href="#">{{ blog.category }}</a></span
    >
    <span v-if="blog.section" class="section"
      >专栏:<a href="#">{{ blog.section }}</a></span
    >
    <span id="tag-list" v-if="blog.tag_list.length"
      >标签:
      <span v-for="tag in blog.tag_list" class="tag"
        ><a href="#">{{ tag }}</a></span
      >
    </span>
    <span>浏览量:{{ blog.pv }}</span>
    <!-- <span>阅读量:{{ blog.read_times }}</span> -->
    <span>预计阅读时长:{{ blog.read_time }}</span>
    <span>创建时间:{{ blog.create_time }}</span>
    <span>更新时间:{{ blog.update_time }}</span>
    <span class="edit" @click="edit_blog">编辑</span>
    <span class="delete" @click="delete_blog">删除</span>
    <hr />
  </div>
  <img :src="blog.avatar" :alt="blog.title" />
  <div v-html="blog.html" />
</template>
<script setup>
import { axios_ins } from "../assets/js/axios";
import "../assets/font/iconfont.css";
import { ref } from "vue";
import { get_url_params } from "../assets/js/tools.js";
import { createMarkdownRenderer } from "../assets/js/markdown/markdown";

const md = await createMarkdownRenderer();
const params = get_url_params();

// 根据博客id拿到博客的完整信息
let blog = ref({ id: params.id, tag_list: [], author: {} });

async function get_blog_info() {
  let response = await axios_ins.get(`/api/blog/${blog.value.id}/`);
  if (response.data.code === "0") {
    let data = response.data.data;
    blog.value = data;
    let html = md.render(blog.value.content);
    blog.value.html = html;
    let keywords = `${blog.value.title} ${blog.value.category} ${blog.value.section} ${blog.value.tag_list} ${blog.value.author.username}`;
    add_meta_info(keywords);
  } else {
    window.history.back();
  }
}

get_blog_info();

function delete_blog() {
  let res = confirm("确认删除吗?");
  if (res) {
    axios_ins.delete(`/api/blog/${blog.value.id}/`).then((response) => {
      let data = response.data;
      if (data.code === "0") {
        window.location.href = "/blog/";
      }
    });
  }
}

function edit_blog() {
  axios_ins.put(`/api/blog/${blog.value.id}/`).then((response) => {
    let data = response.data;
    if (data.code === "0") {
      window.location.href = "/write";
    }
  });
}

function add_meta_info(data) {
  let meta = document.createElement("meta");
  meta.name = "keywords";
  meta.content = data;
  document.head.appendChild(meta);
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
