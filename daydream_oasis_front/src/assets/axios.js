import axios from "axios";

const axios_ins = axios.create({
    withCredentials: true,
    baseURL: 'http://127.0.0.1:8000'

})
axios_ins.defaults.withCredentials = true;
export default axios_ins