import { defineConfig } from "vitepress";
import { API_URL } from "./theme/assets/js/axios";
export default defineConfig({
  lang: "en-US", //zh-CN|en-US
  title: "白日梦想园",
  description:
    "Daydream Oasis是一个致力于启发和创造的个人博客系统，主要用于编程知识包括但不限于前端，后端和AI领域的分享。希望Daydream Oasis能够给您带来一定的启发和成才。",
  base: "/",
  // 忽略死链
  ignoreDeadLinks: true,
  head: [
    [
      "link",
      { rel: "icon", href: "http://www.lll.plus/media/image/favorite.ico" },
    ],

    // element-plus
    [
      "link",
      {
        rel: "stylesheet",
        href: "https://cdn.staticfile.net/element-plus/2.5.1/index.css",
      },
    ],
    // ['script', { src:'//cdn.jsdelivr.net/npm/vue@3' }],
    // ['script', { src:'https://cdn.jsdelivr.net/npm/element-plus' }],
    // vditor
    [
      "link",
      {
        rel: "stylesheet",
        href: "https://cdn.staticfile.net/vditor/3.9.8/index.css",
      },
    ],
  ],
  themeConfig: {
    i18nRouting: true,
    // site title
    siteTitle: "🌈白日梦想园",
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: "Home", link: "/" },
      { text: "首页", link: "/blog/" },
      { text: "关于", link: "/blog/content?id=1053", activeMatch: "/1053" },
      { text: "写博客", link: "/write" },
      { text: "订阅", link: `${API_URL}/api/rss` },
    ],
    // 侧边栏
    // sidebar: [],
    // 显示h2到h6的标题
    outline: "deep",
    outlineTitle: "目录",

    // 社交连接
    socialLinks: [
      {
        icon: {
          svg: '<svg t="1705112206458" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1489" width="200" height="200"><path d="M512 1024C229.222 1024 0 794.778 0 512S229.222 0 512 0s512 229.222 512 512-229.222 512-512 512z m259.149-568.883h-290.74a25.293 25.293 0 0 0-25.292 25.293l-0.026 63.206c0 13.952 11.315 25.293 25.267 25.293h177.024c13.978 0 25.293 11.315 25.293 25.267v12.646a75.853 75.853 0 0 1-75.853 75.853h-240.23a25.293 25.293 0 0 1-25.267-25.293V417.203a75.853 75.853 0 0 1 75.827-75.853h353.946a25.293 25.293 0 0 0 25.267-25.292l0.077-63.207a25.293 25.293 0 0 0-25.268-25.293H417.152a189.62 189.62 0 0 0-189.62 189.645V771.15c0 13.977 11.316 25.293 25.294 25.293h372.94a170.65 170.65 0 0 0 170.65-170.65V480.384a25.293 25.293 0 0 0-25.293-25.267z" fill="#C71D23" p-id="1490"></path></svg>',
        },
        link: "https://gitee.com/max-LLL",
      },
      { icon: "github", link: "https://github.com/LLLPY" },
    ],
    //   网站logo
    // logo: 'http://www.lll.plus/static/image/favorite.ico',

    //底部
    footer: {
      message: "Released under the MIT License.",
      copyright:
        "鄂ICP备20013301号-copyrights©2021 0318-SPACE All Rights Reserved.",
    },

    // 广告
    // carbonAds: {
    //     code: 'your-carbon-code',
    //     placement: 'your-carbon-placement11111',
    // },

    //"回到顶部"的按钮，只会在移动端显示
    returnToTopLabel: "回到顶部",
    //切换语言的按钮
    langMenuLabel: "语言切换",

    // externalLinkIcon: true,

    // 搜索
    search: {
      provider: "local",
      options: {},
    },
  },
  markdown: {
    theme: "github-dark-dimmed",
    lineNumbers: true,
  },
  cleanUrls: true,
});
