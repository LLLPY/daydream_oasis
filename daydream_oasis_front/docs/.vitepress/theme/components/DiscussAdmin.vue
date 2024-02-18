<template>
  <div id="Discuss-Comments-Admin"></div>
</template>
<script setup>
import {onMounted} from "vue";
onMounted(() => {
  let script = document.createElement('script');
  script.type = 'text/javascript';
  script.src = 'https://cdn.staticfile.net/discuss/1.2.5/dist/discuss.admin.js';
  script.onload = function () {
    // 初始化
    discuss.init({
      el: '#Discuss-Comments-Admin',
      serverURLs: 'http://127.0.0.1:6870/'
    })
  }
  document.head.appendChild(script);

})

</script>
