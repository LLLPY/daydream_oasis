<script setup>
import {L2Dwidget} from 'live2d-widget'

setTimeout(function () {
  L2Dwidget.init({
    //黑猫
    "model": {
      "jsonPath": "https://unpkg.com/live2d-widget-model-hijiki@1.0.5/assets/hijiki.model.json",
      "scale": 1,
      "hHeadPos": 0.5,
      "vHeadPos": 0.618
    },
    "display": {"position": "right", "width": 60, "height": 100, "hOffset": 0, "vOffset": -30},

    "mobile": {"show": true, "scale": 0.5},
    "react": {"opacityDefault": 0.9, "opacityOnHover": 0.2}
  });
}, 1000);


</script>

<template>

</template>

<style scoped>

</style>