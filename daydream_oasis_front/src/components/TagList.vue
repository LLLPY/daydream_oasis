<template>
  <div class="card">
    <div class="tools">
      <div class="circle">
        <span class="red box"></span>
      </div>
      <div class="circle">
        <span class="yellow box"></span>
      </div>
      <div class="circle">
        <span class="green box"></span>
      </div>
    </div>
    <div class="card__content">

      <span class="tag" v-for="(tag, index) in tag_list" :key="index"
            :style="{ backgroundColor:randomColor(),fontSize: randomSize() }">{{ tag.title }}</span>

    </div>
  </div>


</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      tag_list: []
    };
  },
  methods: {
    randomColor() {
      // 生成随机颜色
      return '#' + Math.floor(Math.random() * 16777215).toString(16);
    },
    randomSize() {
      // 生成随机字体大小
      return Math.floor(Math.random() * 10 + 5) + 'px';
    },
    fetchTags() {
      axios.get('http://127.0.0.1:8000/api/tag/?format=json').then(response => {
        this.tag_list = response.data.data
      }).catch(error => {
        console.log('error')
      })
    }
  },
  mounted() {
    this.fetchTags();
  }
};
</script>

<style>
.card {
  width: 100%;
  margin: 0.5em auto;
  border-radius: 3px;
  border: 1px solid silver;
  padding-bottom: 0.1em;
  padding-left: 0.1em;
  padding-right: 0.1em;
  margin-bottom: 0;
}

.tools {
  display: flex;
  align-items: center;
  padding: 9px;
}

.circle {
  padding: 0 4px;
}

.box {
  display: inline-block;
  align-items: center;
  width: 10px;
  height: 10px;
  padding: 1px;
  border-radius: 50%;
}

.red {
  background-color: #ff605c;
}

.yellow {
  background-color: #ffbd44;
}

.green {
  background-color: #00ca4e;
}

.card__content .tag {
  margin: 2px;
  display: inline-block;
  border-radius: 5px;
  padding: 0.2em;
  transition: background-color .3s linear;
}

.card__content .tag:hover {
  cursor: pointer;
  background-color: skyblue!important;
}

</style>

