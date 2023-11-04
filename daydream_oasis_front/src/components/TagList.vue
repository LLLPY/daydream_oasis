<template>
    <div class="card" id="tag-box">
        <div class="tools">
            <div class="circle">
                <span class="red box"></span>
            </div>
            <div class="circle">
                <span class="yellow box"></span>
            </div>
            <div class="circle">
                <span class="green box"></span>
            </div>
            <div class="more">
                <span class=""><a href="/tag.html">更多</a></span>
            </div>
        </div>
        <div class="card__content">

      <span class="tag" v-for="(tag, index) in tag_list" :key="index"
            :style="{ backgroundColor:randomColor(),fontSize: randomSize() }">{{ tag.title }}</span>

        </div>
    </div>


</template>

<script>
    import axios_ins from '../assets/axios'

    export default {
        data() {
            return {
                tag_list: []
            };
        },
        methods: {
            randomColor() {
                // 生成随机颜色
                let hue = Math.floor(Math.random() * 360); // 随机色相值（0-359）
                let saturation = Math.floor(Math.random() * 50) + 50; // 随机饱和度（50-100）
                let lightness = Math.floor(Math.random() * 20) + 50; // 随机亮度（50-70）

                return 'hsl(' + hue + ', ' + saturation + '%, ' + lightness + '%)';
            },
            randomSize() {
                // 生成随机字体大小
                return Math.floor(Math.random() * 10 + 7) + 'px';
            },
            fetchTags() {
                axios_ins.get('/api/tag/?format=json').then(response => {
                    this.tag_list = response.data.data

                }).catch(error => {
                    console.log('error')
                })
            }
        },
        mounted() {
            this.fetchTags();
        }
    };
</script>

<style>
    .card {
        width: 100%;
        margin: 0.5em auto;
        border-radius: 3px;
        border: 1px solid silver;
        padding-bottom: 0.1em;
        padding-left: 0.1em;
        padding-right: 0.1em;
        margin-bottom: 0;
    }

    .tools {
        align-items: center;
        padding: 9px;
    }

    .circle {
        display: inline-block;
        padding: 0 4px;
    }

    .box {
        display: inline-block;
        align-items: center;
        width: 10px;
        height: 10px;
        padding: 1px;
        border-radius: 50%;
    }

    .red {
        background-color: #ff605c;
    }

    .yellow {
        background-color: #ffbd44;
    }

    .green {
        background-color: #00ca4e;
    }

    .card__content .tag {
        margin: 2px;
        display: inline-block;
        border-radius: 5px;
        padding: 0.2em;
        transition: background-color .3s linear;
        font-weight: 600;
        color: white;
    }

    .card__content .tag:hover {
        cursor: pointer;
        background-color: skyblue !important;
    }

    .card .tools .more {
        float: right;
        font-size: 0.6em;
    }

    .card .tools .more:hover {
        color: gray;
    }

    .VPDocAside #tag-box {
        max-height: 321px;
        overflow: hidden;
    }


</style>

