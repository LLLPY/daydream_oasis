import {axios_ins} from "../.vitepress/theme/assets/js/axios";

export default {
  async paths() {
    let posts = await (await axios_ins(`/api/blog/?is_all=True`)).data.data.results
    return posts.map((post) => {
      console.log(post.title)
      return {
        params: {
          id: post.id,
          title: post.title,
          author_username: post.author.username,
          pv: post.pv,
          read_times: post.read_times,
          read_time: post.read_time,
          category: post.category,
          tag_list: post.tag_list,
          create_time: post.create_time,
          update_time: post.update_time
        },
        content: post.content // raw Markdown or HTML
      }
    })
  }
}
