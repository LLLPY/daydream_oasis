<template>
  <div id="action-box">
<span class="iconfont">
  <svg class="icon" aria-hidden="true"><use xlink:href="#icon-fenxiang"></use></svg>
  <span class="counter">10000</span>
</span>
    <span class="iconfont">
  <svg class="icon" aria-hidden="true"><use xlink:href="#icon-shoucang-shoucang"></use></svg>
  <span class="counter">100k</span>

</span>
    <span class="iconfont">
  <svg class="icon" aria-hidden="true"><use xlink:href="#icon-dianzan_kuai"></use></svg>
  <span class="counter">9.8k</span>
</span>
  </div>

</template>

<script>
</script>

<style scoped>
#action-box {
  margin-top: 10px;
  overflow: hidden;
  padding: 0.2em;
  border:1px solid red;
}


#action-box .iconfont {
  font-size: 1em;
  float: right;
  margin-right: 2em;
  border-radius: 3px;
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
  margin: auto;
}

#action-box span .icon:hover {
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