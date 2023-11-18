import {default as DefaultTheme} from "vitepress/theme";
import MyLayout from "./MyLayout.vue";
import Login from "../../../src/components/Login.vue";
import Register from "../../../src/components/Register.vue";
import ForgetPassword from "../../../src/components/ForgetPassword.vue";
import TagList from "../../../src/components/TagList.vue";
import TopList from "../../../src/components/TopList.vue";
import Logo from "../../../src/components/Logo.vue";
import ActionBox from "../../../src/components/ActionBox.vue";
import BlogInfo from "../../../src/components/BlogInfo.vue";
import BlogList from "../../../src/components/BlogList.vue";
import Vditor from "../../../src/components/Vditor.vue";
// import Live2dWidget from "../../../src/components/Live2dWidget.vue";
// import {h} from 'vue'
// import Documate from '@documate/vue'
// import '@documate/vue/dist/style.css'
import { ElPagination } from "element-plus";
import 'element-plus/dist/index.css'


// 扩展默认的主题
export default {
    ...DefaultTheme,
    Layout:MyLayout,
    // Layout: h(MyLayout, null, {
    //     'nav-bar-content-before': () => h(Documate, {
    //         endpoint: 'https://rm6pzfp19v.us.aircode.run/ask',
    //     }),
    // }),
    enhanceApp({app}) {
        app.component('Login', Login);
        app.component('Register', Register);
        app.component('ForgetPassword', ForgetPassword);
        app.component('TagList', TagList);
        app.component('TopList', TopList);
        app.component('Logo', Logo);
        app.component('ActionBox', ActionBox);
        app.component('BlogInfo', BlogInfo);
        app.component('BlogList', BlogList);
        app.component('el-pagination', ElPagination);
        app.component('Vditor', Vditor);
        // app.component('Live2dWidget', Live2dWidget);
    }
}

// module.exports = {
    // isCustomElement: tag => tag.startsWith('el-')
// }