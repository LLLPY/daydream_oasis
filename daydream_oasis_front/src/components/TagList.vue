<template>
    <div class="card">
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
        </div>
        <div class="card__content">
            <span class="tag">xxx</span>
            <span class="tag">xxx</span>
            <span class="tag">xxx</span>
            <span class="tag">xxx</span>
            <span class="tag">xxx</span>
            <span class="tag">xxx</span>
            <span class="tag">xxx</span>
            <span class="tag">xxx</span>
        </div>
    </div>


</template>

<script lang="ts" setup>
</script>

<style>
    .card {
        width: 100%;
        height: 254px;
        margin: 10px auto;
        background-color: #F8FBFE;
        border-radius: 8px;
        z-index: 1;
        border: 1px solid silver;
    }

    .tools {
        display: flex;
        align-items: center;
        padding: 9px;
    }

    .circle {
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

    .card__content .tag{
        border: 1px solid red;
        margin: 2px;
        display: inline-block;
        border-radius: 5px;
    }

</style>
  