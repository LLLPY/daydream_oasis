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
</template>
<script>
import axios_ins from "../assets/axios";
import '../assets/font/iconfont'
import '../assets/font/iconfont.css'
import '../assets/css/blog_info.css'
import {Info, Warning} from "../assets/MessageBox";


export default {
  data() {
    return {
      blog: {
        id: parseInt(window.location.pathname.split("/").pop()),
        title: null,
        author: {
          id: null,
          username: null,
        },
        avatar: null,
        category: null,
        tag_list: [],
        pv: null,
        read_times: null,
        read_time: null,
        create_time: null,
        update_time: null
      }
    }

  },
  methods: {
    get_blog_info() {
      axios_ins.get(`/api/blog/${this.blog.id}/`).then(response => {
        let data = response.data
        this.blog = data.data
      })
    },
    upload_action() {
      let res = axios_ins.post('/api/action_log/upload_action/', {
        action: 6,
        cost_time: 0,
        blog_id: this.blog.id
      })
    },
    delete_blog() {
      let res = confirm('确认删除吗?')
      if (res) {
        axios_ins.delete(`/api/blog/${this.blog.id}/`).then(response => {
          let data = response.data
          window.location.href = '/blog/'
          Info(data['message'])
        })
      }

    },
    edit_blog() {
      axios_ins.put(`/api/blog/${this.blog.id}/`).then(response => {
        let data = response.data
        window.location.href = '/write'
        Info(data['message'])
      })
    }
  },


  mounted() {
    this.get_blog_info()
    this.upload_action()
  }
}


</script>

