import { defineConfig } from 'vitepress'
export default defineConfig({
    lang: 'en-US', //zh-CN|en-US
    title: "白日梦想园",
    description: "Daydream Oasis是一个致力于启发和创造的博客系统，为您提供了一个欣赏、分享和沉浸在各种幻想和梦想中的机会。Daydream Oasis将成为您的梦想之家。",
    base: '/',
    // 忽略死链
    ignoreDeadLinks: true,
    head: [
        ['link', { rel: 'icon', href: 'http://www.lll.plus/media/image/favorite.ico' }],

        // element-plus
        ['link', { rel: 'stylesheet', href: 'https://cdn.jsdelivr.net/npm/element-plus/dist/index.css' }],
        // ['script', { src:'//cdn.jsdelivr.net/npm/vue@3' }],
        ['script', { src:'https://cdn.jsdelivr.net/npm/element-plus' }],

        // vditor
        ['link', { rel: 'stylesheet', href: 'https://unpkg.com/vditor@3.9.6/dist/index.css' }],
        ['script', { src:'https://unpkg.com/vditor@3.9.6/dist/index.min.js' }],
    ],
    themeConfig: {
        i18nRouting: true,
        // site title
        siteTitle: '🌈白日梦想园',
        // https://vitepress.dev/reference/default-theme-config
        nav: [
            { text: 'Home🏡', link: '/' },
            { text: '首页🐽', link: '/blog/' },
            { text: '前端💻', link: '/blog/167', activeMatch: '/167' },
            { text: '后端🛸', link: '/blog/408', activeMatch: '/408' },
            { text: 'AI🤖', link: '/blog/2', activeMatch: '/2' },
            { text: '标签🍒', link: '/blog/1389', activeMatch: '/1389' },
            { text: '分类🍰', link: '/blog/1390', activeMatch: '/1390' },
            { text: '关于🦴', link: '/blog/1053', activeMatch: '/1053' },
            { text: '写博客✍️', link: '/write' },
            { text: '登录/注册🚪', link: '/login' },
            // { text: '个人中心🍴', link: '/home' },
            // {
            //     text: '归档🗂️',
            //     items: [
            //         { text: '归档1', link: '/file' },
            //         { text: '归档2', link: '/file' },
            //         { text: '归档3', link: '/file' },
            //     ]
            // },
        ],
        // 侧边栏
        // sidebar: [],
        // 显示h2到h6的标题
        outline: 'deep',
        outlineTitle: '目录',

        // 社交连接
        socialLinks: [
            {
                icon:
                {
                    svg: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 261.76 226.69"><path d="M161.096.001l-30.225 52.351L100.647.001H-.005l130.877 226.688L261.749.001z" fill="#41b883"/><path d="M161.096.001l-30.225 52.351L100.647.001H52.346l78.526 136.01L209.398.001z" fill="#34495e"/></svg>',
                },
                link: 'https://gitee.com/max-LLL',
            },
            { icon: 'github', link: 'https://github.com/LLLPY' },

        ],
        //   网站logo
        // logo: 'http://www.lll.plus/static/image/favorite.ico',

        //底部
        footer: {
            message: 'Released under the MIT License.',
            copyright: '鄂ICP备20013301号-copyrights©2021 0318-SPACE All Rights Reserved.'
        },

        // 广告
        // carbonAds: {
        //     code: 'your-carbon-code',
        //     placement: 'your-carbon-placement11111',
        // },

        //"回到顶部"的按钮，只会在移动端显示
        returnToTopLabel: '回到顶部',
        //切换语言的按钮
        langMenuLabel: '语言切换',

        // externalLinkIcon: true,

        // 搜索
        search: {
            provider: 'local',
            options: {}
        },
    },
    markdown: {
        theme: 'github-dark-dimmed',
        lineNumbers: true,
    },

}
)




