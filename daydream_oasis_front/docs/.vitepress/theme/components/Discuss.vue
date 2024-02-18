<template>
  <div id="Discuss-Comments"></div>
</template>
<script setup>
import {onMounted} from "vue";
import {get_url_params} from '../assets/js/tools'
onMounted(() => {
  let script = document.createElement('script');
  script.type = 'text/javascript';
  script.src = 'https://cdn.staticfile.net/discuss/1.2.5/dist/discuss.js';
  script.onload = function () {
    // 初始化
    discuss.init({
      el: '#Discuss-Comments',
      serverURLs: 'http://127.0.0.1:6870/',
      color:'red',
      path:get_url_params()['id'],
      visitStat:true,
    })
  }
  document.head.appendChild(script);

})

</script>
