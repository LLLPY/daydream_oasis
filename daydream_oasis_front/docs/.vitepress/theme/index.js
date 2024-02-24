import { default as DefaultTheme } from "vitepress/theme";
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
import Discuss from "./components/Discuss.vue";
import DiscussAdmin from "./components/DiscussAdmin.vue";
import {
  ElPagination,
  ElCol,
  ElAutocomplete,
  ElRow,
  ElInput,
  ElUpload,
  ElIcon,
  ElDialog,
  ElTag,
  ElButton,
  ElAvatar,
  ElSelect,
  ElOption,
} from "element-plus";
import { Plus } from "@element-plus/icons-vue";

// 扩展默认的主题
/** @type {import('vitepress').Theme} */
export default {
  ...DefaultTheme,
  Layout: MyLayout,
  async enhanceApp({ app }) {
    app.component("Login", Login);
    app.component("Register", Register);
    app.component("ForgetPassword", ForgetPassword);
    app.component("TagList", TagList);
    app.component("TopList", TopList);
    app.component("Logo", Logo);
    app.component("ActionBox", ActionBox);
    app.component("BlogInfo", BlogInfo);
    app.component("BlogList", BlogList);
    app.component("el-pagination", ElPagination);
    app.component("el-col", ElCol);
    app.component("el-row", ElRow);
    app.component("el-autocomplete", ElAutocomplete);
    app.component("el-input", ElInput);
    app.component("el-upload", ElUpload);
    app.component("el-icon", ElIcon);
    app.component("el-avatar", ElAvatar);
    app.component("el-dialog", ElDialog);
    app.component("el-tag", ElTag);
    app.component("el-button", ElButton);
    app.component("el-select", ElSelect);
    app.component("el-option", ElOption);
    app.component("Plus", Plus);
    app.component("Vditor", Vditor);
    app.component("Write", Write);
    app.component("Nav", Nav);
    app.component("Home", Home);
    app.component("Discuss", Discuss);
    app.component("DiscussAdmin", DiscussAdmin);
    if (!import.meta.env.SSR) {
      // 导入包含window的包
      let plugin = await import("./assets/font/iconfont.js");
      // app.use(plugin.default)
    }
  },
};
