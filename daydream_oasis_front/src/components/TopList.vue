<template>
  <ul id="top-box">
    <div class="head">
      <span class="title">Top</span>
      <span class="more">更多</span>
    </div>

    <li v-for="(top,index) in top_list" :key="index" class="top">
      <span class="number">{{ top.id }}</span><span class="title">{{ top.title }}</span><span class="pv">{{
        top.pv
      }}</span>
    </li>

  </ul>
</template>

<script>

export default {
  data() {
    return {
      top_list: [
        {id: 1, title: 'xxxxxxxxx', pv: '10.02k'},
        {id: 2, title: 'xxx', pv: '10k'},
        {id: 3, title: 'xxx', pv: '10k'},
        {id: 4, title: 'xxx', pv: '10k'},
        {id: 5, title: 'xxx', pv: '10k'},
        {id: 6, title: 'xxx', pv: '10k'},
      ]
    }
  }
}


</script>

<style>
#top-box {
  border: 1px solid silver;
  width: 100%;
  margin: 0.5em auto;
  border-radius: 3px;
  margin-bottom: 0;
  padding-left: 0.1em;
  padding-right: 0.1em;
}

#top-box .top {
  border-top: 1px solid silver;
}

#top-box .top span {
  display: inline-block;
}

#top-box .top .title {
  width: 65%;
}

#top-box .top .number,
#top-box .top .pv {
  width: 10%;
  text-align: center;
}

#top-box .top .pv {
  width: 25%;
  font-size: 0.8em;
}

#top-box .head .title{
  color: black;
  font-weight: 600;
}

#top-box .head{
padding-left: 0.2em;
padding-right: 0.2em;
}

#top-box .head .more {
  font-size: 0.6em;
  float: right;
}

#top-box span{
  cursor: pointer;
}

</style>