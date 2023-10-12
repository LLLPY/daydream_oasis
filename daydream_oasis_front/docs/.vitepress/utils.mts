import axios_ins from '../../src/assets/axios'

export async function getSidebarData() {
    const res = await axios_ins.get('/api/frontconfig/get_sidebar_config/?format=json')
    let code = res.data['code']
    if (code !== '0') {
        return {}
    }

    //配置文件
    let data = res.data['data']
    return data
}

export async function getNavData() {
    // 获取所有文件名和目录名
}


