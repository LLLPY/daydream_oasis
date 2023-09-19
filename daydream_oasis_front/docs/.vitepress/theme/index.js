import {default as DefaultTheme} from "vitepress/theme";
import GlobalComponent from "../../../src/components/GolbalComponent.vue";
import HelloWorld from "../../../src/components/HelloWorld.vue";
import MyLayout from "./MyLayout.vue";
import Login from "../../../src/components/Login.vue";

// 扩展默认的主题
export default {
    ...DefaultTheme,
    Layout:MyLayout,
    enhanceApp({app}) {
        app.component('GlobalComponent', GlobalComponent) //注册一个自定义的组件
        app.component('HelloWorld', HelloWorld)
        app.component('Login', Login)
        // app.component('rAsideOutlineAfter', AsideOutlineAfter)
    }
}