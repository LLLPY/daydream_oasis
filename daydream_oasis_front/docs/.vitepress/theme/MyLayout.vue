<!-- .vitepress/theme/Layout.vue -->
<script setup lang="ts">
    import {useData} from 'vitepress'
    import DefaultTheme from 'vitepress/theme'
    import {nextTick, provide} from 'vue'
    import TagList from '../../../src/components/TagList.vue'
    import TopList from '../../../src/components/TopList.vue'
    import Logo from '../../../src/components/Logo.vue'
    import ActionBox from "../../../src/components/ActionBox.vue";

    // export default {components :{TagList} }

    // import {L2Dwidget} from 'live2d-widget'r

    // import AsideOutlineAfter from "./AsideOutlineAfter.vue";

    const {Layout} = DefaultTheme


    const {isDark} = useData()

    const enableTransitions = () =>
        'startViewTransition' in document &&
        window.matchMedia('(prefers-reduced-motion: no-preference)').matches

    provide('toggle-appearance', async ({clientX: x, clientY: y}: MouseEvent) => {
        if (!enableTransitions()) {
            isDark.value = !isDark.value
            return
        }

        const clipPath = [
            `circle(0px at ${x}px ${y}px)`,
            `circle(${Math.hypot(
                Math.max(x, innerWidth - x),
                Math.max(y, innerHeight - y)
            )}px at ${x}px ${y}px)`
        ]

        await document.startViewTransition(async () => {
            isDark.value = !isDark.value
            await nextTick()
        }).ready

        document.documentElement.animate(
            {clipPath: isDark.value ? clipPath.reverse() : clipPath},
            {
                duration: 300,
                easing: 'ease-in',
                pseudoElement: `::view-transition-${isDark.value ? 'old' : 'new'}(root)`
            }
        )
    })

    // setTimeout(function () {
    //   L2Dwidget.init({
    //     //黑猫
    //     "model": {
    //       "jsonPath": "https://unpkg.com/live2d-widget-model-hijiki@1.0.5/assets/hijiki.model.json",
    //       "scale": 1,
    //       "hHeadPos": 0.5,
    //       "vHeadPos": 0.618
    //     },
    //     "display": {"position": "right", "width": 100, "height": 100, "hOffset": 10, "vOffset": -10},
    //
    //     "mobile": {"show": true, "scale": 0.5},
    //     "react": {"opacityDefault": 0.9, "opacityOnHover": 0.2}
    //   });
    // }, 1000);

</script>

<template>
    <Layout>
        <template #home-hero-image><Logo/></template>
        <template #aside-outline-after>
            <TopList/>
            <TagList/>
        </template>
        <template #doc-after><ActionBox/></template>
    </Layout>

    <!--    <L2Dwidget/>-->


</template>


<style>
    ::view-transition-old(root),
    ::view-transition-new(root) {
        animation: none;
        mix-blend-mode: normal;
    }

    ::view-transition-old(root),
    .dark::view-transition-new(root) {
        z-index: 1;
    }

    ::view-transition-new(root),
    .dark::view-transition-old(root) {
        z-index: 9999;
    }

    .VPSwitchAppearance {
        width: 22px !important;
    }

    .VPSwitchAppearance .check {
        transform: none !important;
    }


</style>

