import {defineConfig} from 'vitepress'
import vue from "@vitejs/plugin-vue";
import AutoImport from "unplugin-auto-import/vite";
import Components from "unplugin-vue-components/vite";
import {ElementPlusResolver} from "unplugin-vue-components/resolvers";

export default defineConfig({
        // plugins: [vue(),AutoImport({resolvers: [ElementPlusResolver()],}),Components({resolvers: [ElementPlusResolver()],}),],
        lang: 'en-US', //zh-CN|en-US
        title: "白日梦想园",
        description: "Daydream Oasis是一个致力于启发和创造的博客系统，为您提供了一个欣赏、分享和沉浸在各种幻想和梦想中的机会。Daydream Oasis将成为您的梦想之家。",
        base: '/',
        // 忽略死链
        ignoreDeadLinks: true,
        head: [
            ['link', {rel: 'icon', href: 'http://www.lll.plus/media/image/favorite.ico'}],

            // element-plus
            ['link', { rel: 'stylesheet', href: 'https://cdn.jsdelivr.net/npm/element-plus/dist/index.css' }],
            // ['script', { src:'//cdn.jsdelivr.net/npm/vue@3' }],
            // ['script', { src:'https://cdn.jsdelivr.net/npm/element-plus' }],

            // vditor
            // ['link', {rel: 'stylesheet', href: 'http://www.lll.plus/media/vditor/dist/js/icons/ant.js'}],
            // ['link', {rel: 'stylesheet', href: 'http://www.lll.plus/media/vditor/dist/css/content-theme/light.css'}],
            // ['script', { src:'https://unpkg.com/vditor@3.9.6/dist/index.min.js' }],
        ],
        themeConfig: {
            i18nRouting: true,
            // site title
            siteTitle: '🌈白日梦想园',
            // https://vitepress.dev/reference/default-theme-config
            nav: [
                {text: 'Home🏡', link: '/'},
                {text: '首页🐽', link: '/blog/'},
                {text: '前端💻', link: '/blog/167', activeMatch: '/167'},
                {text: '后端🛸', link: '/blog/408', activeMatch: '/408'},
                {text: 'AI🤖', link: '/blog/2', activeMatch: '/2'},
                {text: '标签🍒', link: '/blog/1389', activeMatch: '/1389'},
                {text: '分类🍰', link: '/blog/1390', activeMatch: '/1390'},
                {text: '关于🦴', link: '/blog/1053', activeMatch: '/1053'},
                {text: '写博客✍️', link: '/write'},
                {text: '登录/注册🚪', link: '/login'},
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
                            svg: '<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="100px" height="100px" viewBox="0 0 88 88" enable-background="new 0 0 88 88" xml:space="preserve">  <image id="image0" width="88" height="88" x="0" y="0"\n' +
                                '    href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFgAAABYCAMAAABGS8AGAAAABGdBTUEAALGPC/xhBQAAACBjSFJN\n' +
                                'AAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAA7VBMVEUAAAD/gIDIHiPIHyTH\n' +
                                'HiPIHiTIHSPIHiPIHSTIHiTOHSfJHiPIHiPfIEDKHyTIHiTIHSPVKyvIHyPIHiP/QEDHHSTIHibH\n' +
                                'HSPVKyvHHiXIHSPLHibIHiPJHyfIHiPJHiTHHiPHHiXIHiT/VVXHHSPLLTPbcXTstLb01db67Oz+\n' +
                                '/v7////78PHcc3fMMzjopaf++/vdeXz89vbHICbnoaP77/Dccnb44+TQQ0jHHyXstrjJKC7QQkfH\n' +
                                'HiT78fLcdHjKKzDpqKrKKi/89PT23d7uvsDee3/+/PzNNTvppqj88/PMNDn+/f3YYmbffoEJwGXi\n' +
                                'AAAAJHRSTlMAAjNiibDR3+z5Gm3vCFu5/Qx05wRyPNIGkv4izELwVWVusQMCq8UIAAAAAWJLR0Qr\n' +
                                'JLnkCAAAAAd0SU1FB+gBCg4sG93UddMAAAK7SURBVFjD7Zn5V9swDMfTpGmT3vddjs5cSzLGLjpY\n' +
                                'Ydwwtv3/f85a1rDKsmO51Htvb/3+iJTPcy1bloRlrbXW/6GU7aTdTNbzfS+bcdOOnVoFNZd3C4xT\n' +
                                'wc3nXkYtlsoVJlSlXCouja3W6ixB9Vp1KWyj6TGFvGZDn9tqq7AztVua2E63R+Ey1ut2dLj9AQ07\n' +
                                '06BP5w436FzGNoZU7qavw2XM36Rxtyp63Omh3iKtV5s7JRPWPNTch/luKPe5rxW3hQgqzkZH45xB\n' +
                                'DZLPc3dZLmPdJG4L37ed3b39g9eBRGH07NhLuN0NlB/eHL4NEhX+8W3LM1KT5x69C1Ra8G7KuFUu\n' +
                                'T77/oMQCsCfLzzVuvRTuIpjVxNwi914cUbgAXBe/ViUubur9neoj+KYkBJch+JDCDT+Bb8oibg4m\n' +
                                'n53nc3YcjT8TL0lFVBVsQ5/dmHtySqTOlBeAR9BlL16vDpe5mJvi6p39OTjS4bICrr5szuVgDv6i\n' +
                                'BWY2AjucR5x3JnpgB4HTnIfoAhCURmB3NWAcvYwCHIXCC8LHNoPAWQVYyAX5+ElZBPYUYEoSmspD\n' +
                                'YH81YP/vgY1thSp4ZzQwDp7quJ2fkcD4uOldkK8XEju+IGktMLuU2PGVdvTAE4kdJyFbDzyW2HHa\n' +
                                '5BO9AhzNzVfwz4JEzz9NyeDT47n5WhU79JjG4Esh9yQ230CD6DHlnv/4ywtEnoyjeL1BcAtMwuef\n' +
                                'K1gCku7uwUfCgoUrsWjgB/hjxCUWLApJ3G+PgCspCmEZS+F+/wEXLCljYeFN4f6EXGnhDVoFwj5w\n' +
                                '65W3CqC5CRXYu4dHjpvQ3Cy2Y1EC+er65vaewya2Y+YaSHMtr7Em3dxYwdwgxNzoxtywydx4zNxA\n' +
                                'z9wI0jI2NLXMjXktY4PpmQyN0p+U2x7h4f/opcP/33pl5N8Va631D+gX+FNZtIGr8cIAAAAldEVY\n' +
                                'dGRhdGU6Y3JlYXRlADIwMjQtMDEtMTBUMTQ6NDQ6MjcrMDA6MDBjf98CAAAAJXRFWHRkYXRlOm1v\n' +
                                'ZGlmeQAyMDI0LTAxLTEwVDE0OjQ0OjI3KzAwOjAwEiJnvgAAACh0RVh0ZGF0ZTp0aW1lc3RhbXAA\n' +
                                'MjAyNC0wMS0xMFQxNDo0NDoyNyswMDowMEU3RmEAAAAASUVORK5CYII=" />\n' + '</svg>',
                        },
                    link: 'https://gitee.com/max-LLL',
                },
                {icon: 'github', link: 'https://github.com/LLLPY'},


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




