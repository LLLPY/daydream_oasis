import {default as DefaultTheme} from "vitepress/theme";
import MyLayout from "./MyLayout.vue";
import Login from "../../../src/components/Login.vue";
import TagList from "../../../src/components/TagList.vue";
import TopList from "../../../src/components/TopList.vue";
import Logo from "../../../src/components/Logo.vue";
import ActionBox from "../../../src/components/ActionBox.vue";
import BlogInfo from "../../../src/components/BlogInfo.vue";
import MessageBox from "../../../src/components/MessageBox.vue";
import {h} from 'vue'
import Documate from '@documate/vue'
import '@documate/vue/dist/style.css'

// 扩展默认的主题
export default {
    ...DefaultTheme,
    // Layout:MyLayout,
    Layout: h(MyLayout, null, {
        'nav-bar-content-before': () => h(Documate, {
            endpoint: 'https://rm6pzfp19v.us.aircode.run/ask',
        }),
    }),
    enhanceApp({app}) {
        app.component('Login', Login);
        app.component('TagList', TagList);
        app.component('TopList', TopList);
        app.component('Logo', Logo);
        app.component('ActionBox', ActionBox);
        app.component('BlogInfo', BlogInfo);
        app.component('MessageBox', MessageBox);
    }
}