import {ElMessage} from "element-plus";

export function Error(msg) {
    ElMessage({
        showClose: true,
        message: msg,
        center: true,
        type: 'error'
    })
}


export function Warning(msg) {
    ElMessage({
        showClose: true,
        message: msg,
        center: true,
        type: 'warning'
    })
}

export function Info(msg) {
    ElMessage({
        showClose: true,
        message: msg,
        center: true,
        type: 'info'
    })
}


