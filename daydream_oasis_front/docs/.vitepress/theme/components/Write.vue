<template>
  <div id="container">
    <div id="info-form" style="box-shadow: var(--el-box-shadow-light);">
      <el-row :gutter="20">

        <!-- 标题 -->
        <el-col :span="20">
          <el-input v-model="title" class="w-50 m-2" placeholder="请输入标题" clearable size="large" maxlength="30"
                    show-word-limit>
          </el-input>
        </el-col>
        <el-col :span="4" style="text-align: right;">
          <el-button type="primary" size="large" @click="pre_submit">保存草稿</el-button>
          <el-button type="primary" size="large" @click="pre_submit">发&nbsp;&nbsp;布</el-button>
        </el-col>

      </el-row>
    </div>
    <!-- 弹窗 -->
    <el-dialog v-model="dialogFormVisible" title="发&nbsp;布" width="500">

      <!-- 分类  -->
      <el-autocomplete v-model="category" :fetch-suggestions="categoryQuerySearch" clearable size="large"
                       placeholder="请输入分类" @select="handleCategorySelect" class="input-item"/>

      <!-- 专栏  -->
      <el-autocomplete v-model="category" :fetch-suggestions="categoryQuerySearch" clearable class="input-item"
                       size="large" placeholder="请输入专栏" @select="handleCategorySelect"/>

      <!-- avatar -->
      <el-row class="input-item">
        <el-col :span="16">
          <el-upload v-model:file-list="fileList" :action="api_url" :with-credentials="withCredentials"
                     list-type="picture-card" :on-preview="handlePictureCardPreview" :on-remove="handlePictureRemove"
                     :on-success="handlePictureSucc" w-full>
            <el-icon>
              <Plus/>
            </el-icon>
          </el-upload>

          <el-dialog v-model="dialogVisible.value">
            <img w-full :src="avatar.value"/>
          </el-dialog>
        </el-col>
      </el-row>

      <!-- 标签 -->
      <el-autocomplete v-model="tag" :fetch-suggestions="tagQuerySearch" clearable class="input-item" size="large"
                       placeholder="请输入标签" @select="handleTagSelect" @keyup.enter="handleTagInputConfirm"/>
      <el-row class="input-item">
        <el-tag v-for="tag in tag_list" :key="tag.value" class="mx-1" closable :disable-transitions="false" size="large"
                @close="handleTagClose(tag)">
          {{ tag.value }}
        </el-tag>
      </el-row>

      <template #footer>
        <div class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取消</el-button>
          <el-button @click="submit(true)">保存草稿</el-button>
          <el-button type="primary" @click="submit(false)">
            发&nbsp;布
          </el-button>
        </div>
      </template>
    </el-dialog>

    <Vditor/>
  </div>
</template>
<script>
import {Warning} from '../assets/js/MessageBox.js'
import {axios_ins, upload_api} from "../assets/js/axios";
import {goBackOrRedirect} from '../assets/js/tools'

var last_form_data = {};
let blog = {
  data() {
    return {
      blog_id: null,
      title: '',
      avatar: {value: ''},
      category: '',
      category_list: [],
      tag: '',
      tag_list: [],
      dialogVisible: {value: false},
      fileList: [],
      withCredentials: true,
      api_url: upload_api,
      dialogFormVisible: false
    }
  },
  computed: {
    form_data: function () {
      return {
        'id': this.blog_id,
        'title': this.title,
        'category': this.category,
        'avatar': this.avatar.value,
        'tag_list': this.tag_list,
        'content': null,
      }
    }
  },
  methods: {
    // 分类
    categoryQuerySearch(queryString, cb) {
      axios_ins.get('api/category/', {params: {title: queryString, k: 5}})
          .then(response => {
            const data = response.data.data || [];
            const processedData = data.map(({id, title, ...rest}) => ({value: title, ...rest}));
            cb(processedData);
          })
          .catch(error => {
            Warning(error)
            cb([]);
          });
    },

    handleCategorySelect(item) {
      this.category = item.value
    },

    //图片上传
    handlePictureRemove(uploadFile, uploadFiles) {
      // 移除图片
      this.avatar.value = ''
      this.dialogVisible.value = false
      this.fileList.pop()
      document.getElementsByClassName('el-upload--picture-card')[0].classList.remove('hidden');
    },
    handlePictureCardPreview(file) {
      // 大图预览
      this.avatar.value = file.url
      this.dialogVisible.value = true
    },
    handlePictureSucc(response, uploadFile, uploadFiles) {
      // 图片上传成功
      if (response.code === '0') {
        this.fileList[0] = uploadFile
        document.getElementsByClassName('el-upload--picture-card')[0].classList.add('hidden');
        this.avatar.value = response.data.url
      } else {
        this.handlePictureRemove(uploadFile, uploadFiles)
        Warning(response.message)
      }
    },
    //标签
    handleTagClose(tag) {
      this.tag_list.splice(this.tag_list.indexOf(tag), 1)
    },
    tagQuerySearch(queryString, cb) {
      // 请求后端获取tag列表
      axios_ins.get('api/tag/', {params: {title: queryString, k: 5}})
          .then(response => {
            const data = response.data.data || [];
            const processedData = data.map(({id, title, ...rest}) => ({value: title, ...rest}));
            cb(processedData);
          })
          .catch(error => {
            Warning(error)
            cb([]);
          });
    },

    handleTagSelect(item) {
      if (this.tag_list.length >= 3) {
        Warning('最多只能选三个标签!')
        return
      } else {
        this.tag_list.push(item)
        this.tag = ''
      }

    },
    handleTagInputConfirm() {
      if (this.tag) {
        if (this.tag_list.length >= 3) {
          Warning('最多只能选三个标签!')
          return
        } else {
          this.tag_list.push({value: this.tag})
          this.tag = ''
        }

      }
    },
    title_check(warn = true) {
      if (this.title.length === 0 || this.title.length > 30) {
        if (warn) {
          Warning('标题的长度范围是0~30!')
        }
        return false;
      } else {
        return true;
      }
    },
    content_check(warn = true) {
      let content = window.vditor.getValue()
      if (content.length <= 5) {
        if (warn) {
          Warning('内容太短辣!')
        }
        return false;
      } else {
        return true;
      }
    },
    form_check(warn = true) {

      if (!this.title_check(warn)) {
        return false;
      }

      if (this.category.length === 0 || this.category.length > 8) {
        if (warn) {
          Warning('分类的长度范围是0~8!')
        }
        return false;
      }

      if (this.tag_list.length === 0) {
        if (warn) {
          Warning('请至少选择一个标签叭!')
        }
        return false;
      }
      return this.content_check(warn);
    },
    pre_submit() {
      if (this.title_check() && this.content_check()) {
        this.dialogFormVisible = true
      }
    },
    submit(is_draft = false) {
      // 提交前关闭自动更新，否则可能会导致提交在更新之后
      clearInterval(this.interval)
      let data = this.form_data
      data.is_draft = is_draft
      data.content = window.vditor.getValue()

      if (is_draft || this.form_check()) {
        axios_ins.post('/api/blog/?action=submit', data).then(response => {
          if (is_draft) {
            goBackOrRedirect('/blog/');
          } else {
            window.location.href = `/blog/content?id=${this.blog_id}`;
          }
          this.dialogFormVisible = false
        });
      }
    },
    get_draft() {
      // 获取最近的一次草稿
      axios_ins("/api/blog/get_draft/").then(response => {
        let data = response.data
        if (Object.keys(data.data).length) {
          data = data.data
          this.blog_id = data.id
          this.title = data.title
          this.category = data.category
          this.avatar.value = data.avatar
          this.fileList[0] = {url: data.avatar}
          document.getElementsByClassName('el-upload--picture-card')[0].classList.add('hidden');
          this.tag_list = data.tag_list.map(function (val) {
            return {value: val}
          })
          this.content = data.content
          let obj = this
          let interval = setInterval(function () {
            try {
              window.vditor.setValue(data.content)
              last_form_data = {...obj.form_data}
              last_form_data.content = window.vditor.getValue()
              clearInterval(interval)
              console.log("结束调用")
            } catch (e) {
              console.log("继续调用")
            }
          }, 500)
          Warning("接着上次继续编辑...")
        }
      })
    },
    sortAndStringify(obj) {
      // 将对象的属性名按照字母顺序排序
      let sortedObj = {};
      Object.keys(obj).sort().forEach(key => {
        sortedObj[key] = obj[key];
      });
      // 将排序后的对象转换为字符串
      return JSON.stringify(sortedObj);
    },
    _update_draft() {
      let is_valid = this.form_check(false)
      let data = this.form_data
      data.content = window.vditor.getValue()
      let is_change = this.sortAndStringify(last_form_data) !== this.sortAndStringify(data); // 输出 true
      if (is_valid && is_change) {
        last_form_data = {...data}
        data.is_draft = true
        axios_ins.post('/api/blog/?action=update_draft', data).then(response => {
          let data = response.data
          let new_blog_id = data.data.blog_id
          if (new_blog_id) {
            this.blog_id = new_blog_id
          }
        })
      }
    },
    update_draft() {
      //   更新草稿
      this.interval = setInterval(this._update_draft, 3000)
    },

  },
  mounted() {
    axios_ins.get('/api/user/info/').then(response => {
      if (response.data.code !== '0') {
        window.history.back()
      } else {
        this.get_draft()
        setTimeout(this.update_draft, 5000)
      }
    })


  }
}
export default blog

</script>

<style>
#container {
  padding-left: 5%;
  padding-right: 5%;
  min-width: 1200px;
}

#info-form {
  /* border: 1px solid red; */
  height: 50px;
  line-height: 50px;
  margin: 5px auto;
  padding-left: 5px;
  padding-right: 5px;
  border-radius: 5px;
}

.el-upload-list__item,
.el-upload--picture-card {
  width: 80px !important;
  height: 50px !important;
}

.hidden {
  display: none !important;
}

.title-box {
  border: var(--el-border-width) var(--el-border-style) var(--el-border-color);
  height: 40px;
  margin: 6px auto;
  border-top-right-radius: 0;
  border-bottom-right-radius: 0;

}

#info-form .el-input__wrapper {
  border-top-left-radius: 0 !important;
  border-bottom-left-radius: 0 !important;
}

.input-item {
  width: 100%;
  margin-bottom: 8px;
}
</style>
