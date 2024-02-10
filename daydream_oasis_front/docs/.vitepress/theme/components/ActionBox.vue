<template>
  <br>
  <div id="action-box">
    <span class="iconfont">
      <svg class="icon" aria-hidden="true" :class="{ active: false }">
        <use xlink:href="#icon-fenxiang"></use>
      </svg>
      <span class="counter">{{ shared_count }}</span>
    </span>
    <span class="iconfont">
      <svg class="icon" aria-hidden="true" :class="{ active: has_collected }">
        <use xlink:href="#icon-shoucang-shoucang" @click="wrap_collect"></use>
      </svg>
      <span class="counter">{{ collected_count }}</span>

    </span>
    <span class="iconfont">
      <svg class="icon" aria-hidden="true" :class="{ active: has_liked }">
        <use xlink:href="#icon-dianzan_kuai" @click="wrap_like"></use>
      </svg>
      <span class="counter">{{ liked_count }}</span>
    </span>
  </div>
</template>

<script setup>

import { axios_ins } from '../assets/js/axios'
import { ref } from 'vue'
import { get_url_params } from "../assets/js/tools.js";

let params = get_url_params()
const blog = params
let liked_count = ref(0)
let shared_count = ref(0)
let collected_count = ref(0)
let has_liked = ref(false)
let has_collected = ref(false)


function get_action_info() {

  axios_ins.get(`/api/blog/${blog.id}/action_info/`).then(response => {
    let data = response.data
    if (data.code === '0') {
      data = data.data
      has_liked.value = data.has_liked
      liked_count.value = data.liked_count
      has_collected.value = data.has_collected
      collected_count.value = data.collected_count
      shared_count.value = data.shared_count
    }
  })
}

get_action_info()

function like() {
  //   点赞
  axios_ins.post(`/api/blog/${blog.id}/like/`).then(response => {
    if (response.data.code === '0') {
      liked_count.value += 1
      has_liked.value = true
    }
  })
}

function cancel_like() {
  //   点赞
  axios_ins.post(`/api/blog/${blog.id}/cancel_like/`).then(response => {
    if (response.data.code === '0') {
      liked_count.value -= 1
      has_liked.value = false
    }

  })
}

function wrap_like() {
  if (has_liked.value) {
    cancel_like()
  } else {
    like()
  }
}

function collect() {
  //   收藏
  axios_ins.post(`/api/blog/${blog.id}/collect/`).then(response => {
    if (response.data.code === '0') {
      collected_count.value += 1
      has_collected.value = true
    }
  })
}

function cancel_collect() {
  //   收藏
  axios_ins.post(`/api/blog/${blog.id}/cancel_collect/`).then(response => {
    if (response.data.code === '0') {
      collected_count.value -= 1
      has_collected.value = false
    }
  })
}

function wrap_collect() {
  if (has_collected.value) {
    cancel_collect()
  } else {
    collect()
  }
}


</script>

<style scoped>
#action-box {
  margin-top: 10px;
  overflow: hidden;
  padding: 0.2em;
}


#action-box .iconfont {
  font-size: 1em;
  float: right;
  margin-right: 2em;
  border-radius: 3px;
  text-align: center;
}

#action-box .iconfont:first-child {
  margin-right: 0;
}

span:hover {
  cursor: pointer;
}

.icon {
  width: 1.2em;
  height: 1.2em;
  vertical-align: -0.15em;
  fill: gray;
  overflow: hidden;
  transition: fill 0.5s linear;
}

#action-box span .icon:hover,
#action-box span .active {
  fill: skyblue;
}

#action-box span .counter {
  height: 1em;
  width: 100%;
  display: inline-block;
  text-align: center;
  line-height: 1em;
  font-size: 0.9em;
}
</style>
