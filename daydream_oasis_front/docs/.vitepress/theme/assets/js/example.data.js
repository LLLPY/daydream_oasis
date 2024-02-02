// example.example.data.js
import {createMarkdownRenderer, useData} from 'vitepress'
import {axios_ins} from "./axios.js";

const config = globalThis.VITEPRESS_CONFIG
const markdownRenderer =  createMarkdownRenderer(config.srcDir, config.markdown, config.site.base, config.logger)
let {params} = useData()
const blog = params.value
export default {
  async load() {
    const md = await markdownRenderer
    const response = await axios_ins.get(`/api/blog/2/`)
    console.log(blog)
    return response.data.data

  }
}
