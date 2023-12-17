import axios from "axios";

const axios_ins = axios.create({
    withCredentials: true,
    baseURL: 'http://localhost:80',
    // baseURL: 'http://www.lll.plus'

})
axios_ins.defaults.withCredentials = true;
export default axios_ins
