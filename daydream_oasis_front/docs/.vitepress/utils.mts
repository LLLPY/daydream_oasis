import axios from 'axios'


export async function getSidebarData() {
    const res = await axios.get('http://127.0.0.1:8000/api/frontconfig/get_sidebar_config/?format=json')
    let code = res.data['code']
    if (code !== '0') {
        return {}
    }

    //配置文件
    let data = res.data['data']
    console.log(data)

    return data
}

export async function getNavData() {
    // 获取所有文件名和目录名
}

