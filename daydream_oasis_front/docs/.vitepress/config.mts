import {defineConfig} from 'vitepress'
import {getSidebarData, getNavData} from './utils.mjs'
// https://vitepress.dev/reference/site-config
export default defineConfig(
    {
        vite:{

        },

        lang: 'en-US', //zh-CN|en-US
        title: "白日梦想园",
        description: "Daydream Oasis是一个致力于启发和创造的博客系统，为您提供了一个欣赏、分享和沉浸在各种幻想和梦想中的机会。Daydream Oasis将成为您的梦想之家。",
        base: '/',
        // 忽略死链
        ignoreDeadLinks: true,
        lastUpdated: true,
        head: [[
            'link',
            {
                rel: 'icon',
                href: '/favicon.ico'
            }
        ]],
        themeConfig: {
            i18nRouting: true,
            // site title
            siteTitle: '白日梦想园',
            // https://vitepress.dev/reference/default-theme-config
            nav: [
                {text: 'Home', link: '/'},
                {text: '前端', link: '/blog/sider_a/', activeMatch: '/sider_a/'},
                {text: '后端', link: '/blog/sider_b/', activeMatch: '/sider_b/'},
                {text: 'AI', link: 'http://www.lll.plus'},
                {text: '标签', link: 'http://www.lll.plus'},
                {text: '分类', link: 'http://www.lll.plus'},
                {text: '关于', link: 'http://www.lll.plus'},
                {text: '登录/注册', link: '/login/'},
                {
                    text: '归档',
                    items: [
                        {text: '归档1', link: '/'},
                        {text: '归档2', link: '/'},
                        {text: '归档3', link: '/'},
                    ]
                },
            ],
            // 侧边栏
            sidebar: {
                '/blog/sider_a/': [
                    {
                        text: 'section A',
                        //是否支持折叠
                        collapsible: true,
                        //默认展开
                        collapsed: false,
                        items:
                            [
                                {text: 'Markdown Examples', link: '/blog/sider_a/markdown-examples'},
                                {text: 'Runtime API Examples', link: '/blog/sider_a/api-examples'},
                                {text: '初识机器学习', link: '/blog/sider_a/初识机器学习'},
                                {text: 'b', link: '/blog/sider_a/b'},
                                {text: 'team_members', link: '/blog/sider_a/team_members'},
                                // {
                                //     '/blog/sider_a/section_a/': [
                                //         {
                                //             text: 'section A',
                                //             //是否支持折叠
                                //             collapsible: true,
                                //             //默认展开
                                //             collapsed: false,
                                //             items:[ {text: 'demo', link: '/blog/sider_a/section_a/demo'},]
                                //
                                //         }
                                //     ]
                                // }
                            ],
                    },
                    {
                        text: 'section B',
                        //是否支持折叠
                        collapsible: true,
                        //默认展开
                        collapsed: false,
                        items:
                            [
                                {text: 'Markdown Examples', link: '/blog/sider_a/markdown-examples'},
                                {text: 'Runtime API Examples', link: '/blog/sider_a/api-examples'},
                                {text: 'a', link: '/blog/sider_a/a'},
                                {text: 'b', link: '/blog/sider_a/b'},
                            ],
                    },
                ]
                ,
                '/blog/sider_b/': [{
                    text: 'sider B',
                    items:
                        [
                            {text: 'a', link: '/blog/sider_b/a'},
                            {text: 'demo', link: '/blog/sider_b/demo'},
                        ]
                }]
            },

            // sidebar: getSidebarData(),

            // 显示h2到h6的标题
            outline: 'deep',
            outlineTitle: '文章目录',

            // 社交连接
            socialLinks: [
                {icon: 'github', link: 'https://github.com/vuejs/vitepress'},
                {icon: 'linkedin', link: 'https://www.lll.plus'},
                // You can also add custom icons by passing SVG as string:
                // {
                //     icon: {
                //         svg: '<svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><title>Dribbble</title><path d="M12...6.38z"/></svg>'
                //     },
                //     link: '.6666..',
                //     You can include a custom label for accessibility too (optional but recommended):
                // ariaLabel: 'cool link'
                // }
            ],
            //   网站logo
            logo: 'http://www.lll.plus/static/image/favorite.ico',


            //底部
            footer: {
                message: 'Released under the MIT License.',
                copyright: '鄂ICP备20013301号-copyrights©2021 0318-SPACE All Rights Reserved.'
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
                    // dateStyle: 'full',
                    // timeStyle: 'media'
                }
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

            externalLinkIcon: true,

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
        // 标题的后缀
        // titleTemplate:'',
        //     toc:{
        //
        //     },
        // config:(md)=>{
        //     md.use(require())
        // }

        // }

    })

