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
      <div class="item_extra">
        <span class="info-box" @click="search({author:blog.author.id})">
          <span class="iconfont">&#xe6a4;</span>{{ blog.author.username }} {{ blog.update_time }}
        </span>
        <span class="info-box category" @click="search({category:blog.category})"> {{ blog.category }} </span>
        <span class="info-box tag" v-for="tag in blog.tag_list" @click="search({tag:tag})">{{ tag }}</span>
        <span class="info-box read"><a :href="blog.id">阅读原文>></a> </span>
        <span></span>
      </div>
    </div>
  </div>

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
import {axios_ins} from "../assets/js/axios";
import {computed} from 'vue';

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


<style>

#top-box {
  margin-top: 0;
}

.wrap {
  width: 100%;

  .item {
    padding: 12px;
    box-shadow: 0 0 10px 0 rgba(0, 0, 0, .1);
    border-radius: 8px;
    margin-bottom: 24px;
    transition: all linear .5s;

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
      margin-bottom: 10px;


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
        overflow: hidden;
        text-overflow: ellipsis;
        line-height: 32px;
        letter-spacing: 1px;
        text-align: justify;
        word-break: break-all;
      }
    }

    .item_extra {
      padding-top: 8px;
      border-top: 1px solid #eee;

      .info-box {
        margin-left: 8px;
        font-size: 0.8rem;
        border-radius: 2px;
        padding: 2px 4px;

        .iconfont {
          font-size: 14px;
        }

        &:nth-child(1) {
          margin-left: 0;
        }
      }

      .category {
        background-color: rgba(255, 165, 0, 0.7);
      }

      .tag {
        background-color: rgba(235, 235, 250, 0.7);
      }

      a {
        text-decoration: none;
      }
    }

  }

  /* .item:hover {
    box-shadow: 0 0 5px 0 rgba(0, 0, 0, .3);
  } */


}

@media (max-width: 450px) {

  .VPDoc {
    padding-left: 0.55rem !important;
    padding-right: 0.55rem !important;
    padding-top: 12px!important;
  }

  .item {
    width: 100%;

    .item_content {
      display: block !important;
      height: auto !important;

      .item_img {
        width: 100% !important;
        border-radius: 8px !important;

        img {
          width: 100% !important;
          max-height: 250px;

        }
      }

      .item_abstract {
        display: -webkit-box;
        -webkit-line-clamp: 3;
        -webkit-box-orient: vertical;
        overflow: hidden;
      }
    }
  }

  /* 隐藏掉分页的jumper */
  #pagination .el-pagination__jump,
  #pagination .el-pagination__sizes {
    display: none;
  }
}

// 分页第一个按钮边距很大
.el-page,
.vp-doc ul {
  padding-left: 0 !important;
}

</style>
