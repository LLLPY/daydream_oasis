<template>
       <div id="recommend-box">
        相关推荐
    </div>
    <div id="comment-box">
        这是一个框框，假设它是评论框吧！
    </div>
</template>

<script>
    export default {
        name: "recommend"
    }
</script>

<style scoped>

    #recommend-box {
        border: 1px solid red;
        margin-top: 10px;
    }

    #comment-box {
        border: 1px solid aqua;
        margin-top: 10px;
    }
</style>