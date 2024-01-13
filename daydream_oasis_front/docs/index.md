---
# https://vitepress.dev/reference/default-theme-home-page
layout: home


hero:
  name: "🏝️白日梦想园🏡"
  text: "欢迎来到Daydream Oasis！"
  tagline: 白日梦想猿🦍的梦想圣地！
  actions:
    - theme: brand
      text: 开始探索
      link: /blog/
    - theme: alt
      text: source code
      link: https://gitee.com/max-LLL/daydream_oasis/tree/dev/
  
features:
  - icon: 💻
    title: 前端
    details: 从html,css和js，到jQuery和bootstrap，再到vue，一步步探索ing...
    link: /blog/前端/
    linkText: 了解更多
  - icon: 🛸️
    title: 后端
    details: 以python后端为主，包含了web，爬虫，图像处理等多个模块，同时也包含例如golang，c++等其他编程语言。
    link: /blog/后端/
    linkText: 了解更多
  - icon: 🤖
    title: AI
    details: 从了解人工智能开始，到渐入机器学习的佳境，探索的道路还很遥远...
    link: /blog/AI/
    linkText: 了解更多

---

<script setup>
  localStorage.removeItem('page')
</script>

