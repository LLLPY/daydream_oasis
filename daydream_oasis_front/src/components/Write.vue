<template>
  <div id="container">
    <div id="info-form" style="box-shadow: var(--el-box-shadow-light);">
      <el-row :gutter="20" justify="center">

        <!-- 标题 -->
        <el-col :span="6">
          <el-input v-model="title" class="w-50 m-2" placeholder="请输入标题" clearable size="large">
            <template #prepend>标题</template>
          </el-input>
        </el-col>

        <!-- 分类 -->
        <el-col :span="5">
          <el-row>
            <el-col :span="5" class="el-input-group__prepend title-box">分类</el-col>
            <el-col :span="19">
              <el-autocomplete v-model="category" :fetch-suggestions="categoryQuerySearch" clearable
                               class="inline-input w-full" size="large" placeholder="请输入分类"
                               @select="handleCategorySelect"/>
            </el-col>
          </el-row>
        </el-col>

        <!-- avatar -->
        <el-col :span="3">
          <el-row>
            <el-col :span="8" class="el-input-group__prepend title-box">封面</el-col>
            <el-col :span="16">
              <el-upload v-model:file-list="fileList"
                         action="http://www.lll.plus/api/file/upload/"
                         :with-credentials="withCredentials"
                         list-type="picture-card" :on-preview="handlePictureCardPreview"
                         :on-remove="handlePictureRemove"
                         :on-success="handlePictureSucc"
                         w-full>
                <el-icon>
                  <Plus/>
                </el-icon>
              </el-upload>

              <el-dialog v-model="dialogVisible.value">
                <img w-full :src="avatar.value"/>
              </el-dialog>
            </el-col>
          </el-row>
        </el-col>

        <!-- 标签 -->
        <el-col :span="8">
          <el-row>
            <el-col :span="3" class="el-input-group__prepend title-box">标签</el-col>
            <el-col :span="6">
              <el-autocomplete v-model="tag" :fetch-suggestions="tagQuerySearch" clearable
                               class="inline-input w-full" size="large" placeholder="请输入标签"
                               @select="handleTagSelect"
                               @keyup.enter="handleTagInputConfirm"/>
            </el-col>
            <el-col :span="15">
              <el-tag v-for="tag in tag_list" :key="tag.value" class="mx-1" closable
                      :disable-transitions="false" size="large" @close="handleTagClose(tag)">
                {{ tag.value }}
              </el-tag>
            </el-col>
          </el-row>
        </el-col>

        <!-- 发布 -->
        <el-col :span="2" style="text-align: right;">
          <el-button type="primary" size="large" @click="submit">发&nbsp;&nbsp;布</el-button>
        </el-col>


      </el-row>
    </div>
    <Vditor/>
  </div>
</template>
<script>
import {Warning} from '../assets/MessageBox.js'
import axios_ins from "../assets/axios";
import {get_cookie} from "../assets/js/tools";

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
      this.fileList[0] = uploadFile
      document.getElementsByClassName('el-upload--picture-card')[0].classList.add('hidden');
      this.avatar.value = response['data']['url']
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
    form_check(warn = true) {
      if (this.title.length === 0 || this.title.length > 30) {
        if (warn) {
          Warning('标题的长度范围是0~30!')
        }

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

      let content = window.vditor.getValue()
      if (content.length <= 5) {
        if (warn) {
          Warning('内容太短辣!')
        }
        return false;
      }
      return true;
    },
    submit() {
      let is_valid = this.form_check()
      if (is_valid) {
        // 提交前关闭自动更新，否则可能会导致提交在更新之后
        clearInterval(this.interval)
        let data = this.form_data
        data.is_draft = false
        data.content = window.vditor.getValue()
        axios_ins.post('/api/blog/?action=submit', data).then(response => {
          window.location.href = `/blog/${this.blog_id}.html`
        })
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
    console.log()
    if (!get_cookie('auth_token')) {
      Warning('请先登录!')
      history.back()
    } else {
      this.get_draft()
      setTimeout(this.update_draft, 5000)
    }

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
</style>