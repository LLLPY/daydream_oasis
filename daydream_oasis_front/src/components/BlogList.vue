

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
          <span>{{ blog.author.username }}</span>
        </span>

        <span class="category-box info-box">
          <span class="iconfont">&#xe64e;</span>
          <span class="category">{{ blog.category }}</span></span>


        <span class="tag-list info-box" v-if="blog.tag_list.length">
          <span class="iconfont">&#xeb47;</span>
          <span class="tag" v-for="tag in blog.tag_list">{{ tag }}</span>
        </span>

        <span class="update_time info-box"><span class="iconfont">&#xe9ab;</span>

          <span>{{ blog.update_time }}</span></span>

        <span class="read info-box"><a :href="convert_url(blog)">阅读原文>></a> </span>
      </div>

    </li>

  </ul>
  <div id="pagination"> <el-pagination background layout="prev, pager, next, sizes, jumper" :total="total" :size="size"
      :hide-on-single-page="true" :page-sizes="[10, 20, 30, 50]" @size-change="handleSizeChange"
      @current-change="handleCurrentChange" />
  </div>
</template>

<script>
import axios_ins from "../assets/axios";
import { Warning } from "../assets/MessageBox";

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
      this.page = val
      this.get_blog_list()
    },
    convert_url(blog) {
      let path = blog.category_parent_list.join('/')
      let url
      if (blog.category === blog.title) {
        url = `${path}/${blog.category}/`
      } else {
        url = `${path}/${blog.category}/${blog.title}.html`

      }

      if (url.startsWith('blog')) {
        url = url.substring(5)
      }
      return url
    }
  },
  mounted() {
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
  /* border: 1px solid red; */

}

#blog-list .blog-preview:hover {
  transform: scale(1.1, 1.1);
}

#blog-list .blog-preview:hover>#blog-list .blog-preview:not(:hover) {
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
  margin-bottom: 5px;
  border: 1px solid #0000001f;
}

#blog-list .blog-preview .content {
  min-height: 80px;
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
  word-break: break-all; /* 或者 word-wrap: break-word; */


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

}

#blog-list .blog-preview .info {
  min-height: 35px;
  font-size: 0.75rem;

}

#blog-list .blog-preview .info span {
  line-height: 35px;
  margin-left: 0.1rem;
}

#blog-list .blog-preview .info .info-box {
  margin-left: 0.5rem;

}

#blog-list .blog-preview .info .info-box:nth-child(1) {
  margin-left: 0;
}

/* 靠右，同时清楚浮动的影响 */
#blog-list .blog-preview .info .read {
  float: right;
  clear: float; 
  display: inline-block;
}

#blog-list .blog-preview .info .read a {
  text-decoration: none;
}

#blog-list .blog-preview .info .author {}

#blog-list .blog-preview .info .category {
  background-color: orange;
  border-radius: 4px;
  padding: 0.1rem;
}


#blog-list .blog-preview .info .tag {
  background-color: #22c55e;
  border-radius: 4px;
  padding: 0.1rem;
}

#blog-list .blog-preview .info .iconfont {
  margin: 0;
}

#pagination {
  width: 100%;
}

#pagination .el-pagination {
  width: 100% !important;
}
</style>