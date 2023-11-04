<BlogInfo id="26" title="" author="白日梦想猿" pv=0 read_times=0 pre_cost_time="0" category="其他" tag_list="['']" create_time="2023.11.04 17:23:12" update_time="2023.11.04 17:23:12" /><script setup>
import { VPTeamMembers } from 'vitepress/theme'

const members = [
  {
    avatar: 'https://www.github.com/yyx990803.png',
    name: 'Evan You',
    title: 'Creator',
    links: [
      { icon: 'github', link: 'https://github.com/yyx990803' },
      { icon: 'twitter', link: 'https://twitter.com/youyuxi' }
    ]
  },
 {
    avatar: 'https://www.github.com/yyx990803.png',
    name: 'Evan You',
    title: 'Creator',
    links: [
      { icon: 'github', link: 'https://github.com/yyx990803' },
      { icon: 'twitter', link: 'https://twitter.com/youyuxi' }
    ]
  },
  
]
</script>

# Our Team

Say hello to our awesome team.

<VPTeamMembers size="small" :members="members" />