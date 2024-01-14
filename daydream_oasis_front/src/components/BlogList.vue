<template>
  <div class="wrap">
    <div class="item" v-for="(blog, index) in blog_list" :key="blog.id">
      <div class="item_title">
        {{ blog.title }} 
      </div>
      <div class="item_content">
        <div class="item_img">
          <img :src="blog.avatar" alt="">
        </div>
        <div class="item_abstract">
          {{ blog.abstract }}
        </div>
      </div>
    </div>
  </div>
  <!-- <ul id="blog-list">
    <li class="blog-preview" v-for="(blog, index) in blog_list">
      <h3 class="title">{{ blog.title }}</h3>
      <hr>
      <div class="content">
        <div class="avatar">
          <img :src="blog.avatar" alt="">
        </div>
        <div class="article">
          {{ blog.abstract }}
        </div>
      </div>
      <hr>
      <div class="info">
        <span class="author info-box">

          <span class="iconfont">&#xe6a4;</span>
          <span @click="search({author:blog.author.id})">{{ blog.author.username }}</span>
        </span>

        <span class="category-box info-box">

          <span class="category" @click="search({category:blog.category})">
             <span class="iconfont">&#xe64e;</span>
            {{ blog.category }}</span></span>


        <span class="tag-list info-box" v-if="blog.tag_list.length">

          <span class="tag" v-for="tag in blog.tag_list" @click="search({tag:tag})">
            <span class="iconfont">&#xeb47;</span>
            {{ tag }}
          </span>
        </span>

        <span class="update_time info-box">
         <span class="iconfont">&#xe9ab;</span> 

          <span class="date">{{ blog.update_time }}</span></span>

        <span class="read info-box"><a :href="blog.id">阅读原文>></a> </span>
      </div>

    </li>

  </ul> -->
  <div id="pagination">
    <el-pagination
      background 
      :pager-count="5" layout="prev, pager, next, sizes, jumper" :total="total" :size="size"
      :hide-on-single-page="true" :current-page="page" :page-sizes="[10, 20, 30, 50]"
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"/>
  </div>
</template>

<script>
import axios_ins from "../assets/axios";
import {Warning} from "../assets/MessageBox";
import {ref, computed} from 'vue';

export default {
  data() {
    return {
      page: 1,
      size: 10,
      total: 0,
      pre: null,
      next: null,
      detail: 'false',
      blog_list: [],
      screen_width: computed(() => {
        return window.innerWidth
      }),
      search_url: 'http://localhost:8000/api/blog/search/'
    }
  },
  methods: {
    get_blog_list() {
      axios_ins.get(`/api/blog/?page=${this.page}&size=${this.size}&detail=${this.detail}`).then(response => {
        let data = response.data
        data = data.data
        this.total = data.count
        this.pre = data.previous
        this.next = data.next
        this.blog_list = data.results

      })
    },
    handleSizeChange(val) {
      this.size = val
      this.get_blog_list()
    },
    handleCurrentChange(val) {
      // 当点击分页按钮时，滚动到指定的锚点
      let element = document.getElementById('VPContent');
      // 当点击分页按钮时，滚动到页面顶部
      window.scrollTo({
        top: 0,
        behavior: 'smooth' // 可以添加平滑滚动效果
      });
      this.page = val
      localStorage.setItem('page', val)
      this.get_blog_list()
    },
    search(params) {
      let url = this.search_url + '?'
      for (let key in params) {
        if (params.hasOwnProperty(key) && params[key]) {
          url += `${key}=${params[key]}&`
          console.log(key)
          console.log(params[key])
        }
      }
      axios_ins(url).then(response => {
        let data = response.data
          data = data.data
          this.blog_list = data
      })
    }
  },
  mounted() {
    this.page = +localStorage.getItem('page') || 1
    this.get_blog_list()
  }
}

</script>


<style scoped >
.wrap {
  width: 100%;

  .item {
    padding: 12px;
    box-shadow: 0 0 4px 0 rgba(0, 0, 0, .1);
    border-radius: 8px;
    margin-bottom: 24px;

    .item_title {
      padding: 10px 0;
      font-size: 20px;
      font-weight: bold;
      margin-bottom: 10px;
      border-bottom: 1px solid #eee;
    }

    .item_content {
      display: flex;
      height: 150px;

      .item_img {
        width: 40%;
        height: 100%;
        margin-right: 12px;
        flex-shrink: 0;
        border-radius: 8px;

        img {
          width: 100%;
          height: 100%;
          object-fit: cover;
          border-radius: 8px;
        }
      }

      .item_abstract {
        flex: 1;
        font-size: 16px;
        line-height: 1.5;
        overflow: hidden;
        text-overflow: ellipsis;
        line-height: 32px;
        /* letter-spacing: 1px; */
        /* text-align: justify; */
        word-break: break-all;
      }
    }
  }
}

@media (max-width: 767px) {
  .item_content {
   flex-direction: column;
   height: auto !important;

    .item_img {
      width: 100% !important;
      border-radius: 8px !important;
    }

    .item_abstract {
      display: -webkit-box;
      -webkit-line-clamp: 3; /* 指定要显示的行数 */
      -webkit-box-orient: vertical;
    }
  }
}
</style>
