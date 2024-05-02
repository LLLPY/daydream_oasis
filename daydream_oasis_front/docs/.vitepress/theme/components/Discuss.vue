<template>
  <div id="Discuss-Comments"></div>
</template>
<script setup>
import { onMounted } from "vue";
import { get_url_params } from "../assets/js/tools";
import { API_URL } from "../assets/js/axios";
onMounted(() => {
  let script = document.createElement("script");
  script.type = "text/javascript";
  script.src = "https://cdn.staticfile.net/discuss/1.2.5/dist/discuss.js";
  script.onload = function () {
    // 初始化
    discuss.init({
      el: "#Discuss-Comments",
      serverURLs: `${API_URL}/api/comment/`,
      color: "red",
      path: `content?id=${get_url_params()["id"]}`,
      visitStat: true,
    });
  };
  document.head.appendChild(script);
});
</script>
