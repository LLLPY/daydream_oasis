<script setup>
// 1.1 引入Vditor 构造函数
import Vditor from "vditor";
import { onMounted } from "vue";
import { Warning } from "../assets/js/MessageBox";
import { upload_api } from "../assets/js/axios";

// const CDN = "https://cdn.jsdelivr.net/npm/vditor@3.9.8"
const CDN = "https://cdn.staticfile.net/vditor/3.9.8";

// 3. 在组件初始化时，就创建Vditor对象，并引用
onMounted(() => {
  window.vditor = new Vditor("vditor", {
    // 获取焦点方法
    focus(md) {
      document.onkeydown = function () {
        // 判断 Ctrl+S
        if (event.ctrlKey == true && event.keyCode == 83) {
          alert("触发ctrl+s");
          // 或者 return false;
          event.preventDefault();
        }
      };
    },
    // 这个是自定义导航栏
    toolbar: [
      "emoji",
      "headings",
      "bold",
      "italic",
      "strike",
      "link",
      "|",
      "list",
      "ordered-list",
      "check",
      "|",
      "quote",
      "line",
      "code",
      "inline-code",
      "|",
      "upload",
      "record",
      "table",
      "|",
      "export",
      "fullscreen",
      "preview",
      "edit-mode",
      //新增自定义按钮
      {
        hotkey: "⌘-⇧-S",
        name: "sponsor",
        tipPosition: "s",
        tip: "点我有惊喜！",
        className: "right",
        icon: '<svg t="1589994565028" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2808" width="32" height="32"><path d="M506.6 423.6m-29.8 0a29.8 29.8 0 1 0 59.6 0 29.8 29.8 0 1 0-59.6 0Z" fill="#0F0F0F" p-id="2809"></path><path d="M717.8 114.5c-83.5 0-158.4 65.4-211.2 122-52.7-56.6-127.7-122-211.2-122-159.5 0-273.9 129.3-273.9 288.9C21.5 562.9 429.3 913 506.6 913s485.1-350.1 485.1-509.7c0.1-159.5-114.4-288.8-273.9-288.8z" fill="#FAFCFB" p-id="2810"></path><path d="M506.6 926c-22 0-61-20.1-116-59.6-51.5-37-109.9-86.4-164.6-139-65.4-63-217.5-220.6-217.5-324 0-81.4 28.6-157.1 80.6-213.1 53.2-57.2 126.4-88.8 206.3-88.8 40 0 81.8 14.1 124.2 41.9 28.1 18.4 56.6 42.8 86.9 74.2 30.3-31.5 58.9-55.8 86.9-74.2 42.5-27.8 84.3-41.9 124.2-41.9 79.9 0 153.2 31.5 206.3 88.8 52 56 80.6 131.7 80.6 213.1 0 103.4-152.1 261-217.5 324-54.6 52.6-113.1 102-164.6 139-54.8 39.5-93.8 59.6-115.8 59.6zM295.4 127.5c-72.6 0-139.1 28.6-187.3 80.4-47.5 51.2-73.7 120.6-73.7 195.4 0 64.8 78.3 178.9 209.6 305.3 53.8 51.8 111.2 100.3 161.7 136.6 56.1 40.4 88.9 54.8 100.9 54.8s44.7-14.4 100.9-54.8c50.5-36.3 108-84.9 161.7-136.6 131.2-126.4 209.6-240.5 209.6-305.3 0-74.9-26.2-144.2-73.7-195.4-48.2-51.9-114.7-80.4-187.3-80.4-61.8 0-127.8 38.5-201.7 117.9-2.5 2.6-5.9 4.1-9.5 4.1s-7.1-1.5-9.5-4.1C423.2 166 357.2 127.5 295.4 127.5z" fill="#141414" p-id="2811"></path><path d="M353.9 415.6m-33.8 0a33.8 33.8 0 1 0 67.6 0 33.8 33.8 0 1 0-67.6 0Z" fill="#0F0F0F" p-id="2812"></path><path d="M659.3 415.6m-33.8 0a33.8 33.8 0 1 0 67.6 0 33.8 33.8 0 1 0-67.6 0Z" fill="#0F0F0F" p-id="2813"></path><path d="M411.6 538.5c0 52.3 42.8 95 95 95 52.3 0 95-42.8 95-95v-31.7h-190v31.7z" fill="#5B5143" p-id="2814"></path><path d="M506.6 646.5c-59.6 0-108-48.5-108-108v-31.7c0-7.2 5.8-13 13-13h190.1c7.2 0 13 5.8 13 13v31.7c0 59.5-48.5 108-108.1 108z m-82-126.7v18.7c0 45.2 36.8 82 82 82s82-36.8 82-82v-18.7h-164z" fill="#141414" p-id="2815"></path><path d="M450.4 578.9a54.7 27.5 0 1 0 109.4 0 54.7 27.5 0 1 0-109.4 0Z" fill="#EA64F9" p-id="2816"></path><path d="M256 502.7a32.1 27.5 0 1 0 64.2 0 32.1 27.5 0 1 0-64.2 0Z" fill="#EFAFF9" p-id="2817"></path><path d="M703.3 502.7a32.1 27.5 0 1 0 64.2 0 32.1 27.5 0 1 0-64.2 0Z" fill="#EFAFF9" p-id="2818"></path></svg>',
        click() {
          alert("hello！");
        },
      },
    ],
    //编辑模式---wysiwyg:所见即所得 ir:及时渲染 sv:分屏预览
    mode: "sv",
    preview: {
      theme: {
        current: "light",
        // path: `${CDN}/dist/css/content-theme`,
      },
      mode: "both",
      markdown: {
        toc: true, //目录
      },
      //代码高亮
      hljs: {
        lineNumber: true,
        // style: "vs", //主题样式
      },
      //数学公式的渲染
      math: {
        engine: "KaTeX", // KaTeX MathJax
      },
    },
    //图标配置
    icon: "ant", // ant material

    //编辑器高度 不配置就是自适应 支持数字和百分比  "minHeight": 500
    // height: window.innerHeight,
    // height: screen.height,
    minHeight: 600,
    // height: '100%',
    //语言 中文：zh_CN 英文：en_US 韩文：ko_KR 日文；ja_JP
    lang: "zh_CN",

    //实用小特性 按下tab新增四个空格 placeholder内容为空的提示 全屏层级
    tab: "    ",
    placeholder: "开始你的创作吧！(tips:草稿会自动保存哦...)🐛🐛🐛",
    fullscreen: {
      index: 9999,
    },

    //文件上传
    upload: {
      accept: "image/*,.mp3, .wav, .rar",
      url: upload_api,
      linkToImgUrl: upload_api,
      filename(name) {
        return name
          .replace(/[^(a-zA-Z0-9\u4e00-\u9fa5\.)]/g, "")
          .replace(/[\?\\/:|<>\*\[\]\(\)\$%\{\}@~]/g, "")
          .replace("/\\s/g", "");
      },
      withCredentials: true,
      format(files, responseText) {
        // 转换为指定的格式
        let data = JSON.parse(responseText);
        if (data["code"] === "0") {
          data = data["data"];
          let succMap = {};
          succMap[data.filename] = data.url;
          let res = { data: { errFiles: [], succMap: succMap } };
          return JSON.stringify(res);
        } else {
          Warning(data["message"]);
        }
      },
    },

    hint: {
      //@，#话题等关键字扩展
      extend: [
        {
          key: "@",
          hint: (key) => {
            if ("vanessa".indexOf(key.toLocaleLowerCase()) > -1) {
              return [
                {
                  value: "@Kim",
                  html: '<img src="https://emoji.emojipic.cn/pic/72/apple/grinning-face_1f600.png"/> 开心的Kim',
                },
                {
                  value: "@Kim",
                  html: '<img src="https://emoji.emojipic.cn/pic/72/apple/smiling-face-with-open-mouth-and-cold-sweat_1f605.png"/> 流汗的Kim',
                },
                {
                  value: "@Kim",
                  html: '<img src="https://emoji.emojipic.cn/pic/72/apple/face-throwing-a-kiss_1f618.png"/> 好色的Kim',
                },
              ];
            }
            return [];
          },
        },
      ],

      //自定义表情
      emoji: {
        嘿嘿: "😀",
        哈哈: "😃",
        大笑: "😄",
        嘻嘻: "😁",
        斜眼笑: "😆",
        苦笑: "😅",
        笑哭了: "😂",
        笑得满地打滚: "🤣",
        微笑: "☺",
        羞涩微笑: "😊",
        微笑天使: "😇",
        呵呵: "🙂",
        倒脸: "🙃",
        眨眼: "😉",
        松了口气: "😌",
        花痴: "😍",
        喜笑颜开: "🥰",
        飞吻: "😘",
        亲亲: "😗",
        微笑亲亲: "😙",
        羞涩亲亲: "😚",
        好吃: "😋",
        吐舌: "😛",
        眯眼吐舌: "😝",
        单眼吐舌: "😜",
        滑稽: "🤪",
        挑眉: "🤨",
        带单片眼镜的脸: "🧐",
        书呆子脸: "🤓",
        墨镜笑脸: "😎",
        好崇拜哦: "🤩",
        聚会笑脸: "🥳",
        得意: "😏",
        不高兴: "😒",
        失望: "😞",
        沉思: "😔",
        担心: "😟",
        困扰: "😕",
        微微不满: "🙁",
        不满: "☹",
        痛苦: "😣",
        困惑: "😖",
        累: "😫",
        累死了: "😩",
        恳求的脸: "🥺",
        哭: "😢",
        放声大哭: "😭",
        傲慢: "😤",
        生气: "😠",
        怒火中烧: "😡",
        嘴上有符号的脸: "🤬",
        爆炸头: "🤯",
        脸红: "😳",
        脸发烧: "🥵",
        冷脸: "🥶",
        吓死了: "😱",
        害怕: "😨",
        冷汗: "😰",
        失望但如释重负: "😥",
        汗: "😓",
        抱抱: "🤗",
        想一想: "🤔",
        不说: "🤭",
        安静的脸: "🤫",
        说谎: "🤥",
        沉默: "😶",
        冷漠: "😐",
        无语: "😑",
        龇牙咧嘴: "😬",
        翻白眼: "🙄",
        缄默: "😯",
        啊: "😦",
        极度痛苦: "😧",
        吃惊: "😮",
        震惊: "😲",
        睡着了: "😴",
        流口水: "🤤",
        困: "😪",
        晕头转向: "😵",
        闭嘴: "🤐",
        头昏眼花: "🥴",
        恶心: "🤢",
        呕吐: "🤮",
        打喷嚏: "🤧",
        感冒: "😷",
        发烧: "🤒",
        受伤: "🤕",
        发财: "🤑",
        牛仔帽脸: "🤠",
        恶魔微笑: "😈",
        生气的恶魔: "👿",
        食人魔: "👹",
        小妖精: "👺",
        小丑脸: "🤡",
        大便: "💩",
        鬼: "👻",
        头骨: "💀",
        骷髅: "☠",
        外星人: "👽",
        外星怪物: "👾",
        机器人: "🤖",
        南瓜灯: "🎃",
        大笑的猫: "😺",
        微笑的猫: "😸",
        笑出眼泪的猫: "😹",
        花痴的猫: "😻",
        奸笑的猫: "😼",
        亲亲猫: "😽",
        疲倦的猫: "🙀",
        哭泣的猫: "😿",
        生气的猫: "😾",
        掌心向上托起: "🤲",
        张开双手: "👐",
        举双手: "🙌",
        鼓掌: "👏",
        握手: "🤝",
        拇指向上: "👍",
        拇指向下: "👎",
        出拳: "👊",
        举起拳头: "✊",
        朝左的拳头: "🤛",
        朝右的拳头: "🤜",
        交叉的手指: "🤞",
        胜利手势: "✌",
        爱你的手势: "🤟",
        摇滚: "🤘",
        ok: "👌",
        反手食指向左指: "👈",
        反手食指向右指: "👉",
        反手食指向上指: "👆",
        反手食指向下指: "👇",
        食指向上指: "☝",
        举起手: "✋",
        立起的手背: "🤚",
        手掌: "🖐",
        瓦肯举手礼: "🖖",
        挥手: "👋",
        给我打电话: "🤙",
        肌肉: "💪",
        竖中指: "🖕",
        写字: "✍",
        双手合十: "🙏",
        脚: "🦶",
        腿: "🦵",
        唇膏: "💄",
        唇印: "💋",
        嘴: "👄",
        牙齿: "🦷",
        舌头: "👅",
        耳朵: "👂",
        鼻子: "👃",
        脚印: "👣",
        眼睛: "👁",
        双眼: "👀",
        脑: "🧠",
        说话: "🗣",
        人像: "👤",
        双人像: "👥",
        小宝贝: "👶",
        女孩: "👧",
        儿童: "🧒",
        男孩: "👦",
        女人: "👩",
        成人: "🧑",
        男人: "👨",
        "女人: 卷发": "👩\u200d🦱",
        "男人: 卷发": "👨\u200d🦱",
        "女人: 红发": "👩\u200d🦰",
        "男人: 红发": "👨\u200d🦰",
        "女人：金色的头发": "👱\u200d♀️",
        金色头发的人: "👱",
        "女人: 白发": "👩\u200d🦳",
        "男人: 白发": "👨\u200d🦳",
        "女人: 秃顶": "👩\u200d🦲",
        "男人: 秃顶": "👨\u200d🦲",
        有胡子的人: "🧔",
        老奶奶: "👵",
        老年人: "🧓",
        老爷爷: "👴",
        戴瓜皮帽的人: "👲",
        戴头巾的人: "👳",
        女人戴着头巾: "👳\u200d♀️",
        带头饰的女人: "🧕",
        警察: "👮",
        女警官: "👮\u200d♀️",
        建筑工人: "👷",
        女建筑工人: "👷\u200d♀️",
        卫兵: "💂",
        女警卫: "💂\u200d♀️",
        侦探: "🕵",
        女侦探: "🕵️\u200d♀️",
        女卫生工作者: "👩\u200d⚕️",
        男子健康工作者: "👨\u200d⚕️",
        农妇: "👩\u200d🌾",
        农夫: "👨\u200d🌾",
        女厨师: "👩\u200d🍳",
        男厨师: "👨\u200d🍳",
        女学生: "👩\u200d🎓",
        男学生: "👨\u200d🎓",
        女歌手: "👩\u200d🎤",
        男歌手: "👨\u200d🎤",
        女老师: "👩\u200d🏫",
        男老师: "👨\u200d🏫",
        女工人: "👩\u200d🏭",
        男工人: "👨\u200d🏭",
        女程序员: "👩\u200d💻",
        男程序员: "👨\u200d💻",
        女白领: "👩\u200d💼",
        男白领: "👨\u200d💼",
        女技工: "👩\u200d🔧",
        男技工: "👨\u200d🔧",
        女科学家: "👩\u200d🔬",
      },
      emojiPath: `${CDN}/dist/images/emoji`,
    },
    //字数统计
    counter: {
      enable: false,
      //回调
      after(count) {
        console.log("字数为" + count);
      },
    },
    //重定义大小
    resize: {
      // enable: true, //打开
      position: "bottom", //位置
    },
    //缓存
    cache: {
      enable: false,
    },

    //是否展示大纲,手机端自动隐藏就行了
    outline: {
      enable: true,
    },
    // 工具栏配置是否隐藏和固定
    toolbarConfig: {
      // 是否固定工具栏
      pin: true,
    },
    // cdn:CDN
  });
});
</script>

<template>
  <!-- 指定一个容器 -->
  <div id="vditor"></div>
</template>

<style>
.vditor-emojis {
  max-height: 100px;
  overflow: auto;
}
</style>
