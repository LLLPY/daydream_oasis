<style src="../assets/font/iconfont.css"></style>
<script setup>
    defineProps(['id', 'title', 'author', 'pv', 'read_times', 'pre_cost_time', 'category', 'tag_list', 'create_time', 'update_time'])
    import '../assets/font/iconfont'
</script>

<script>
    import axios_ins from "../assets/axios";

    export default {
        data() {
            return {
                blog_id: null,
                // tag_list: null
            }
        },

        methods: {
            get_blog_id() {
                // 获取blog的id
                this.blog_id = document.getElementsByClassName('info-box')[0].id
            },
            get_tag_list() {
                let tag_str = document.getElementById('tag-list').innerText
            },
            upload_action() {
                let res = axios_ins.post('/api/action_log/upload_action/', {
                    action: 6,
                    cost_time: 0,
                    blog_id: this.blog_id
                })
            }

        },
        mounted() {
            this.get_blog_id()
            this.upload_action()
        }
    }
</script>

<template>
    <div class="info-box" :id="id">
        <h1>{{ title }}</h1>
        <span>作者:{{ author }}</span>
        <span>浏览器:{{ pv }}</span>
        <span>阅读量:{{ read_times }}</span>
        <span>预计阅读时长:{{ pre_cost_time }}</span>
        <span>分类:{{ category }}</span>
        <span id="tag-list">{{ tag_list }}</span>
        <span>创建时间:{{ create_time }}</span>
        <span>更新时间:{{ update_time }}</span>
        <hr/>
    </div>
</template>

<style scoped>
    .info-box span {
        display: inline-block;
        font-size: 0.8em;
        color: silver;
        margin: 0.2em;
    }

</style>