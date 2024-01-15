import axios from "axios";
import {Warning} from "./MessageBox";

// const API_URL = 'http://www.lll.plus'
const API_URL = 'http://localhost:8000'
const axios_ins = axios.create({
    withCredentials: true,
    baseURL: API_URL,
})

// 添加请求拦截器
axios_ins.interceptors.request.use(function (config) {
    // 在发送请求之前做些什么
    return config;
}, function (error) {
    // 对请求错误做些什么
    return Promise.reject(error);
});

// 添加响应拦截器
axios_ins.interceptors.response.use(function (response) {
    // 对响应数据做点什么
    let data = response.data
    if (data['code'] !== '0') {
        Warning(data['message'])
        // 结果异常，直接结束
        return Promise.reject(new Error('Response code is not 0'));

    }
    return response;
}, function (error) {
    // 对响应错误做点什么
    return Promise.reject(error.message);
});
// axios_ins.defaults.withCredentials = true;

const upload_api = `${API_URL}/api/file/upload/`


export {axios_ins, API_URL, upload_api}

