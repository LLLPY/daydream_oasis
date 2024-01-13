<template>
  <ul id="blog-list">
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
            <!-- <span class="iconfont">&#xe64e;</span> -->
            {{ blog.category }}</span></span>


        <span class="tag-list info-box" v-if="blog.tag_list.length">

          <span class="tag" v-for="tag in blog.tag_list" @click="search({tag:tag})">
            <!-- <span class="iconfont">&#xeb47;</span> -->
            {{ tag }}
          </span>
        </span>

        <span class="update_time info-box">
          <!-- <span class="iconfont">&#xe9ab;</span> -->

          <span class="date">{{ blog.update_time }}</span></span>

        <span class="read info-box"><a :href="blog.id">阅读原文>></a> </span>
      </div>

    </li>

  </ul>
  <div id="pagination">
    <el-pagination background :pager-count="5" layout="prev, pager, next, sizes, jumper" :total="total" :size="size"
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
        if (data.code === '0') {
          data = data.data
          this.total = data.count
          this.pre = data.previous
          this.next = data.next
          this.blog_list = data.results

        } else {
          Warning(data.message)
        }
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
        if (data.code === '0') {
          data = data.data
          console.log(data)
          this.blog_list = data

        } else {
          Warning(data.message)
        }
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

#blog-list {
  padding: 0;
  margin: 0;
  width: 100%;
}

#blog-list .blog-preview:hover {
  transform: scale(1.05, 1.05);
}

#blog-list .blog-preview:hover > #blog-list .blog-preview:not(:hover) {
  filter: blur(10px);
  transform: scale(0.9, 0.9);
}


#blog-list .blog-preview {
  list-style: none;
  width: 100%;
  padding-left: 0.5rem;
  padding-right: 0.5rem;
  transition: 400ms;
  border-radius: 5px;
  margin-bottom: 1rem;
  cursor: pointer;
  box-shadow: 0 0 4px 0 rgba(0, 0, 0, .1);

}

#blog-list .blog-preview .title {
  margin-top: 0;
  margin-bottom: 0;
}


#blog-list .blog-preview hr {
  margin-top: 2px;
  margin-bottom: 3px;
  border: 1px solid #0000001f;
}

#blog-list .blog-preview .content {
  //min-height: 80px;
  max-height: 150px;
  display: flex;
  flex-direction: row;

}

#blog-list .blog-preview .content .avatar {
  flex: 4;
  padding-right: 2%;

}

#blog-list .blog-preview .content .avatar img {
  width: 100%;
  height: 100%;
  border: 1px solid #dee2e6;
  border-radius: 0.25rem;
  overflow: hidden;
}

#blog-list .blog-preview .content .article {
  flex: 7;
  overflow: hidden;
  font-size: 0.9rem;
  word-break: break-all;

}

/* 移动端适配 */
@media (max-width: 450px) {
  #blog-list .blog-preview .content {
    display: inline-block;
  }

  #blog-list .blog-preview .content .avatar,
  #blog-list .blog-preview .content .article {
    width: 100%;
  }

  /* 移动端最多显示三行内容 */
  #blog-list .blog-preview .content .article {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
    //white-space: nowrap;
  }

  .VPDoc {
    padding-left: 0.55rem !important;
    padding-right: 0.55rem !important;
  }

  #blog-list .blog-preview {
    margin-bottom: 1.5rem;
  }

  /* 隐藏掉分页的jumper */
  #pagination .el-pagination__jump,
  #pagination .el-pagination__sizes {
    display: none;
  }

}

#blog-list .blog-preview .info {
  font-size: 0.75rem;
  line-height: 1.5;
}

#blog-list .blog-preview .info .info-box {
  margin-left: 0.5rem;
}

#blog-list .blog-preview .info .info-box:nth-child(1) {
  margin-left: 0;
}

#blog-list .blog-preview .info .read a {
  text-decoration: none;
}

#blog-list .blog-preview .info .category,
#blog-list .blog-preview .info .tag,
#blog-list .blog-preview .info .date {
  border-radius: 4px;
  padding: 0.1rem;
}

#blog-list .blog-preview .info .category {
  background-color: orange;

}


#blog-list .blog-preview .info .tag {
  background-color: #22c55e;
  margin-left: 2px;
}

#blog-list .blog-preview .info .tag:nth-child(1) {
  margin-left: 0;
}


#blog-list .blog-preview .info .date {
  background-color: skyblue;
}

#blog-list .blog-preview .info .iconfont {
  margin: 0;
}
</style>