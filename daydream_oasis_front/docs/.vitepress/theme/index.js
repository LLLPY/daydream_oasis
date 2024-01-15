import {default as DefaultTheme} from "vitepress/theme";
import MyLayout from "./MyLayout.vue";
import Login from "./components/Login.vue";
import Register from "./components/Register.vue";
import ForgetPassword from "./components/ForgetPassword.vue";
import TagList from "./components/TagList.vue";
import TopList from "./components/TopList.vue";
import Logo from "./components/Logo.vue";
import ActionBox from "./components/ActionBox.vue";
import BlogInfo from "./components/BlogInfo.vue";
import BlogList from "./components/BlogList.vue";
import Vditor from "./components/Vditor.vue";
import Write from "./components/Write.vue";
import Nav from "./components/Nav.vue";
import Home from "./components/Home.vue";
import { ElPagination,ElCol,ElAutocomplete,ElRow,ElCascader,ElInput,ElUpload,ElIcon,ElDialog,ElTag,ElButton,ElAvatar } from "element-plus";
import { Plus,Delete, ZoomIn } from '@element-plus/icons-vue'
import './assets/css/index.css'



// 扩展默认的主题
export default {
    ...DefaultTheme,
    Layout:MyLayout,
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
        app.component('el-col', ElCol);
        app.component('el-row', ElRow);
        app.component('el-autocomplete', ElAutocomplete);
        app.component('el-cascader', ElCascader);
        app.component('el-input', ElInput);
        app.component('el-upload', ElUpload);
        app.component('el-icon', ElIcon);
        app.component('el-avatar', ElAvatar);
        app.component('Plus', Plus);
        app.component('Delete', Delete);
        app.component('ZoomIn', ZoomIn);
        app.component('el-dialog', ElDialog);
        app.component('el-tag', ElTag);
        app.component('el-button', ElButton);
        app.component('Vditor', Vditor);
        app.component('Write', Write);
        app.component('Nav', Nav);
        app.component('Home', Home);
    }
}