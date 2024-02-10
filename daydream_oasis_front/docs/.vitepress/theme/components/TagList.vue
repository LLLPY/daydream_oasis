<template>
  <div class="card" id="tag-box">
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
      <div class="more">
        <span class=""><a href="/blog/1389.html">更多</a></span>
      </div>
    </div>
    <div class="card__content">

      <span class="tag" v-for="(tag, index) in tag_list" :key="index">{{ tag.title }}</span>

    </div>
  </div>


</template>

<script>
import {axios_ins} from '../assets/js/axios'

export default {
  data() {
    return {
      tag_list: []
    };
  },
  methods: {
    fetchTags() {
      axios_ins.get('/api/tag/?format=json').then(response => {
        this.tag_list = response.data.data
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
  align-items: center;
  padding: 9px;
  padding-bottom: 0;

}

.circle {
  display: inline-block;
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

.card__content {
  text-align: justify;
  word-break: break-all;
  padding: 5px;
  padding-bottom: 0;

  .tag {
    margin-right: 5px;
    font-size: 0.8rem;
    border-radius: 2px;
    padding: 2px 4px;
    background-color: rgba(235, 235, 250, 0.7);
  }

  .tag:nth-child(1) {
    margin-left: 0;
  }
}


.card__content .tag:hover {
  cursor: pointer;
  background-color: skyblue !important;
}

.card .tools .more {
  float: right;
  font-size: 0.6em;
}

.card .tools .more:hover {
  color: gray;
}

.VPDocAside #tag-box {
  max-height: 318px;
  overflow: hidden;
  box-shadow: 0 0 4px 0 rgba(0, 0, 0, .1);

}

a {
  text-decoration: none !important;
}


</style>
