import {defineConfig} from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
    title: "白日梦想园",
    description: "Daydream Oasis是一个致力于启发和创造的博客系统，为您提供了一个欣赏、分享和沉浸在各种幻想和梦想中的机会。Daydream Oasis将成为您的梦想之家。",
    base: '/',
    head: [],
    themeConfig: {
        // https://vitepress.dev/reference/default-theme-config
        nav: [
            {text: 'Home', link: '/'},
            {text: 'Examples', link: '/markdown-examples'},
            {text: '前段', link: 'http://www.lll.plus'},
            {text: '后端', link: 'http://www.lll.plus'},
            {
                text: '归档',
                items: [
                    {text: '归档1', link: '/'},
                    {text: '归档2', link: '/'},
                    {text: '归档3', link: '/'},
                ]
            },
        ],

        sidebar: [
            {
                text: 'Examples',
                items: [
                    {text: 'Markdown Examples', link: '/markdown-examples'},
                    {text: 'Runtime API Examples', link: '/api-examples'},
                    {text: 'Runtime API Examples2', link: '/api-examples'}
                ]
            }
        ],
        // 社交连接
        socialLinks: [
            {icon: 'github', link: 'https://github.com/vuejs/vitepress'},
            {icon: 'linkedin', link: 'https://www.lll.plus'},
        ],
        //   网站logo
        logo: 'http://www.lll.plus/static/image/favorite.ico',

        // site title
        // siteTitle : '66666',

        //底部
        footer: {
            message: 'Released under the MIT License.',
            copyright: 'Copyright © 2019-present Evan You'
        },

        // editLink
        editLink: {
            pattern: 'https://github.com/vuejs/vitepress/edit/main/docs/:path',
            text: 'Edit this page on GitHub'
        },


        // lastUpdated
        lastUpdated: {
            text: 'updated at',
            formatOptions: {
                dateStyle: 'full',
                timeStyle: 'media'
            }
        },

        // 广告
        carbonAds: {
            code: 'your-carbon-code',
            placement: 'your-carbon-placement'
        },




    }


})
