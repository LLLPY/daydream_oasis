<template>
  <div>
    <div id="progress" :style="{ width: `${progress}%` }"></div>
    <Content />
  </div>
</template>

<script>
export default {
  computed: {
    progress() {
      return this.$page.progress;
    },
  },
};
</script>

<style>
#progress {
  height: 2px;
  background-color: #42b983;
  position: fixed;
  top: 0;
  left: 0;
  transition: width 0.3s;
  z-index: 9999;
}
</style>
