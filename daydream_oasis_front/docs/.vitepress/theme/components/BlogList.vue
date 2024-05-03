<template>
  <el-affix :offset="110">
    <div id="filter-box">
      <template v-for="tag in filter_tag_list">
        <el-tag
          v-if="tag.visible"
          :key="tag.label"
          closable
          :disable-transitions="false"
          type="info"
          @close="handleClose(tag)"
        >
          {{ tag.label }}：{{ tag.value }}
        </el-tag>
      </template>
    </div>
  </el-affix>

  <div class="wrap">
    <div class="item" v-for="(blog, index) in blog_list" :key="blog.id">
      <div class="item_title">
        {{ blog.title }}
      </div>
      <div class="item_content">
        <div class="item_img">
          <img :src="blog.avatar" alt="" />
        </div>
        <div class="item_abstract">
          {{ blog.abstract }}
        </div>
      </div>
      <div class="item_extra">
        <span
          class="info-box"
          @click="search({ author: blog.author.username })"
        >
          <span class="iconfont">&#xe6a4;</span>{{ blog.author.username }}
          {{ blog.update_time }}
        </span>
        <span
          class="info-box category"
          @click="search({ category: blog.category })"
        >
          {{ blog.category }}
        </span>
        <span
          class="info-box section"
          v-if="blog.section"
          @click="search({ section: blog.section })"
        >
          {{ blog.section }}
        </span>
        <span
          class="info-box tag"
          v-for="tag in blog.tag_list"
          @click="search({ tag: tag })"
          >{{ tag }}</span
        >
        <span class="info-box read"
          ><a :href="'content?id=' + blog.id">阅读原文>></a>
        </span>
        <span></span>
      </div>
    </div>
  </div>

  <div id="pagination">
    <el-pagination
      background
      :pager-count="5"
      layout="prev, pager, next, sizes, jumper"
      :total="total"
      :size="size"
      :hide-on-single-page="true"
      :current-page="page"
      :page-sizes="[10, 20, 30, 50]"
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
    />
  </div>

  <!-- Scroll down to see the bottom-right button. -->
  <el-backtop :right="40" :bottom="120" style="z-index: 100000" />
</template>

<script>
import { axios_ins } from "../assets/js/axios";
import { computed } from "vue";

let blog_list_obj = {
  data() {
    return {
      page: 1,
      size: 10,
      total: 0,
      pre: null,
      next: null,
      detail: "false",
      blog_list: [],
      params: {},
      screen_width: computed(() => {
        return window.innerWidth;
      }),
      filter_tag_list: [
        { key: "author", label: "作者", value: "", visible: false },
        { key: "category", label: "分类", value: "", visible: false },
        { key: "section", label: "专栏", value: "", visible: false },
        { key: "tag", label: "标签", value: "", visible: false },
        { key: "keyword", label: "关键词", value: "", visible: false },
      ],
    };
  },
  methods: {
    get_blog_list() {
      this.params.page = this.page;
      this.params.size = this.size;
      this.params.detail = this.detail;
      axios_ins
        .get(`/api/blog/?${this.objectToUrlParams(this.params)}`)
        .then((response) => {
          let data = response.data;
          if (data.code === "0") {
            data = data.data;
            this.total = data.count;
            this.pre = data.previous;
            this.next = data.next;
            this.blog_list = data.results;
          }
        });
    },
    handleSizeChange(val) {
      this.size = val;
      this.get_blog_list();
    },
    handleCurrentChange(val) {
      // 当点击分页按钮时，滚动到页面顶部
      window.scrollTo({
        top: 0,
        behavior: "smooth", // 可以添加平滑滚动效果
      });
      this.page = val;
      localStorage.setItem("page", val);
      this.get_blog_list();
    },
    search(params) {
      this.params = { ...this.params, ...params };
      // 更新过滤标签
      for (let i = 0; i < this.filter_tag_list.length; i++) {
        let key = this.filter_tag_list[i].key;
        let val = this.params[key];
        if (val) {
          this.filter_tag_list[i].value = val;
          this.filter_tag_list[i].visible = true;
        } else {
          this.filter_tag_list[i].visible = false;
        }
      }

      this.page = 1;
      this.get_blog_list();
      window.scrollTo({
        top: 0,
        behavior: "smooth", // 可以添加平滑滚动效果
      });
    },
    objectToUrlParams(obj) {
      return Object.keys(obj)
        .map(
          (key) => `${encodeURIComponent(key)}=${encodeURIComponent(obj[key])}`,
        )
        .join("&");
    },
    handleClose(tag) {
      // 删除params中当前的参数
      delete this.params[tag.key];
      this.search(this.params);
    },
  },

  mounted() {
    this.page = +localStorage.getItem("page") || 1;
    this.get_blog_list();
  },
};

function fade() {
  // 存储页面滚动前的位置
  let scrollTopBefore = window.scrollY;

  // 添加滚轮事件监听器
  window.addEventListener("scroll", () => {
    // 获取需要渐隐的元素
    var fadingElement = document.querySelector(".el-affix");

    // 获取页面滚动后的位置
    const scrollTopAfter = window.scrollY;

    // 判断页面是否真正滚动了
    if (scrollTopBefore !== scrollTopAfter && fadingElement) {
      // 如果滚动了，隐藏元素
      fadingElement.classList.add("_hidden");

      // 如果已经存在延迟隐藏的计时器，则清除它
      if (fadingElement.fadeTimeout) {
        clearTimeout(fadingElement.fadeTimeout);
      }

      // 创建一个新的延迟隐藏计时器，在停止滚动后恢复元素的显示
      fadingElement.fadeTimeout = setTimeout(() => {
        fadingElement.classList.remove("_hidden");
      }, 1000); // 延迟时间要与CSS中transition的时间一致

      // 更新页面滚动前的位置为当前位置
      scrollTopBefore = scrollTopAfter;
    }
  });
}

fade();

export default blog_list_obj;
</script>

<style>
#top-box {
  margin-top: 0;
}

.wrap {
  width: 100%;
  .item {
    padding: 12px;
    box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.1);
    border-radius: 8px;
    margin-bottom: 24px;
    transition: all linear 0.5s;

    .item_title {
      padding: 10px 0;
      font-size: 20px;
      font-weight: bold;
      margin-bottom: 10px;
      border-bottom: 1px solid #eee;
    }

    .item_content {
      display: flex;
      height: 152px;
      margin-bottom: 10px;

      .item_img {
        width: 40%;
        height: 100%;
        margin-right: 12px;
        flex-shrink: 0;
        border-radius: 8px;
        overflow: hidden;

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
      .section {
        background-color: rgba(114, 239, 94, 0.7);
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
    padding-top: 12px !important;
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

  .el-affix .el-affix--fixed {
    top: 80px !important;
  }
}

/*分页第一个按钮边距很大*/
.el-page,
.vp-doc ul {
  padding-left: 0 !important;
}

#filter-box {
  width: 100%;
  border: 1px solid rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
  padding: 0 12px;
  border-radius: 8px;
  background-color: white;
  box-shadow: 0 1px 0px 0 rgba(0, 0, 0, 0.1);
}

.el-affix {
  transition: opacity 1.5s linear !important; /* 使用transition实现渐变效果 */
  opacity: 1;
}

._hidden {
  opacity: 0;
}

#filter-box:empty {
  margin-bottom: 0;
  border: none;
}

#filter-box span {
  margin-left: 8px;
  margin-top: 10px;
  margin-bottom: 10px;
}

#filter-box span:nth-child(1) {
  margin-left: 0;
}
</style>
