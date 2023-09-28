<template>
  <el-button plain @click="openCenter('error')">Centered text</el-button>
</template>

<script>
import 'element-plus/es/components/message/style/css'
import {ElMessage} from 'element-plus'

export const Error = (msg) => {
  ElMessage({
    showClose: true,
    message: msg,
    center: true,
    type: 'error'
  })
}
</script>
