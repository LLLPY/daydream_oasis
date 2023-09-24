import {default as DefaultTheme} from "vitepress/theme";
import MyLayout from "./MyLayout.vue";
import Login from "../../../src/components/Login.vue";
import TagList from "../../../src/components/TagList.vue";
import TopList from "../../../src/components/TopList.vue";
import Logo from "../../../src/components/Logo.vue";
import ActionBox from "../../../src/components/ActionBox.vue";
import BlogInfo from "../../../src/components/BlogInfo.vue";

// 扩展默认的主题
export default {
    ...DefaultTheme,
    Layout:MyLayout,
    enhanceApp({app}) {
        app.component('Login', Login);
        app.component('TagList', TagList);
        app.component('TopList', TopList);
        app.component('Logo', Logo);
        app.component('ActionBox', ActionBox);
        app.component('BlogInfo', BlogInfo);
    }
}