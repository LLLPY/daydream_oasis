<script setup>
    defineProps(['title', 'author', 'pv', 'read_times', 'pre_cost_time', 'category', 'tag_list', 'create_time', 'update_time'])
</script>
<template title>
    <div class="info-box">
        <h1>{{ title }}</h1>
        <span>作者:{{ author }}</span>
        <span>浏览器:{{ pv }}</span>
        <span>阅读量:{{ read_times }}</span>
        <span>预计阅读时长:{{ pre_cost_time }}</span>
        <span>分类:{{ category }}</span>
        <span>标签:    <span v-for="tag in tag_list">{{ tag }}</span></span>
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