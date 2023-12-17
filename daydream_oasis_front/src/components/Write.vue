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
                         action="http://localhost:80/api/file/upload/"
                         :with-credentials="withCredentials"
                         list-type="picture-card" :on-preview="handlePictureCardPreview"
                         :on-remove="handlePictureRemove"
                         :on-change="handlePictureChange"
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

export default {
  data() {
    return {
      title: '',
      avatar: {value: ''},
      category: '',
      category_list: [],
      tag: '',
      tag_list: [],
      dialogVisible: {value: false},
      fileList: [],
      withCredentials: true
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
      this.avatar.value = ''
      this.dialogVisible.value = false
      document.getElementsByClassName('el-upload--picture-card')[0].classList.remove('hidden');

    },
    handlePictureCardPreview(file) {
      this.avatar.value = file.url
      this.dialogVisible.value = true
    },
    handlePictureChange(uploadFile, uploadFiles) {
      this.fileList[0] = uploadFile
      document.getElementsByClassName('el-upload--picture-card')[0].classList.add('hidden');
    },
    handlePictureSucc(response, uploadFile, uploadFiles) {
      console.log(response)
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
    submit() {
      if (this.title.length === 0 || this.title.length > 30) {
        Warning('标题的长度范围是0~30!')
        return
      }
      if (this.category.length === 0 || this.category.length > 8) {
        Warning('分类的长度范围是0~8!')
        return;
      }
      if (this.tag_list.length === 0) {
        Warning('请至少选择一个标签叭!')
        return;
      }

      let content = window.vditor.getValue()
      if (content.length <= 5) {
        Warning('内容太短辣!')
        return;
      }
      let data = {
        'title': this.title,
        'category': this.category,
        'avatar': this.avatar.value,
        'tag_list': this.tag_list,
        'content': content
      }
      axios_ins.post('/api/blog/', data).then(response => {
        let data = response.data
        if(data['code']==='1'){
          Warning(data['message'])
        }else{

        }
      })
    }
  }
}


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