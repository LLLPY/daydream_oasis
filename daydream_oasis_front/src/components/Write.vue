
<template>
    <div id="container">
        <div id="info-form" style="box-shadow: var(--el-box-shadow-light);">
            <el-row  :gutter="20" justify="center">

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
                        <el-col :span="19"> <el-cascader placeholder="请输入分类" filterable clearable :props="props"
                                size="large"></el-cascader>
                        </el-col>

                    </el-row>


                </el-col>

                <!-- avatar -->
                <el-col :span="3">
                    <el-row>
                        <el-col :span="8" class="el-input-group__prepend title-box">封面</el-col>
                        <el-col :span="16"> <el-upload v-model:file-list="fileList"
                                action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
                                list-type="picture-card" :on-preview="handlePictureCardPreview" :on-remove="handleRemove"
                                :on-change="handleChange" w-full>
                                <el-icon>
                                    <Plus />
                                </el-icon>
                            </el-upload>

                            <el-dialog v-model="dialogVisible.value">
                                <img w-full :src="avatar.value" />
                            </el-dialog></el-col>

                    </el-row>



                </el-col>

                <!-- 标签 -->
                <el-col :span="8">
                    <el-row>
                        <el-col :span="3" class="el-input-group__prepend title-box">标签</el-col>
                        <el-col :span="6"><el-autocomplete v-model="tag" :fetch-suggestions="tagQuerySearch" clearable
                                class="inline-input w-full" size="large" placeholder="请输入标签" @select="handleSelect"
                                @keyup.enter="handleInputConfirm" /></el-col>
                        <el-col :span="15">
                            <el-tag v-for="tag in tag_list" :key="tag.value" class="mx-1" closable
                                :disable-transitions="false" size="large" @close="handleClose(tag)">
                                {{ tag.value }}
                            </el-tag>
                        </el-col>
                    </el-row>



                </el-col>

                <!-- 发布 -->
                <el-col :span="2" style="text-align: right;">
                    <el-button type="primary" size="large">发&nbsp;&nbsp;布</el-button>
                </el-col>



            </el-row>
        </div>


        <Vditor />
    </div>
</template>
<script>
import Vditor from './Vditor.vue'
import { nextTick, ref } from 'vue'
import { Warning } from '../assets/MessageBox.js'
let id = 0

export default {
    data() {
        return {
            title: '',
            avatar: { value: '' },
            category: '',
            tag: '',
            tag_list: [{ value: 'tag1' }, { value: 'tag2' }],
            inputTagValue: '',
            inputTagVisible: { value: false },
            dialogVisible: { value: false },
            disabled: false,
            fileList: [],


            props: {
                checkStrictly: true, //选择其中的任意一项
                lazy: true,
                lazyLoad(node, resolve) {
                    const { level } = node
                    setTimeout(() => {
                        const nodes = Array.from({ length: level + 1 }).map((item) => ({
                            value: ++id,
                            label: `Option - ${id}`,
                            leaf: level >= 2,
                        }))
                        // Invoke `resolve` callback to return the child nodes data and indicate the loading is finished.
                        resolve(nodes)
                        console.log(nodes)
                    }, 1000)
                },
            }
        }
    },
    methods: {

        // 分类
        querySearch(queryString, cb) {
            const results = queryString
                ? restaurants.value.filter(createFilter(queryString))
                : restaurants.value
            // call callback function to return suggestions
            cb(results)
        }
        ,
        handleSelect(item) {
            console.log(item)
        },

        //图片上传
        handleRemove(uploadFile, uploadFiles) {
            this.avatar.value = ''
            this.dialogVisible.value = false
            document.getElementsByClassName('el-upload--picture-card')[0].classList.remove('hidden');

        },
        handlePictureCardPreview(file) {
            this.avatar.value = file.url
            this.dialogVisible.value = true
        },
        handleChange(uploadFile, uploadFiles) {
            console.log(uploadFile)
            console.log(uploadFiles)
            this.fileList[0] = uploadFile
            document.getElementsByClassName('el-upload--picture-card')[0].classList.add('hidden');

        },
        //标签
        handleClose(tag) {
            this.tag_list.splice(this.tag_list.indexOf(tag), 1)
        },
        tagQuerySearch(val) {
            // 请求后端获取tag列表
            return [{ value: 'vue' }, { value: 'element' }]
        },
        handleSelect(item) {
            if (this.tag_list.length >= 3) {
                Warning('最多只能选三个标签!')
                return
            } else {
                this.tag_list.push(item)
                this.tag = ''
            }

        },
        handleInputConfirm() {
            if (this.tag) {
                if (this.tag_list.length >= 3) {
                    Warning('最多只能选三个标签!')
                    return
                } else {
                    this.tag_list.push({ value: this.tag })
                    this.tag = ''
                }

            }
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

#info-form .el-input__wrapper{
    border-top-left-radius: 0!important;
    border-bottom-left-radius: 0!important;
    
}
</style>