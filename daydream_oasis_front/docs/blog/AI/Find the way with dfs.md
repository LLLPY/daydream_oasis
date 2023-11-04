---
prev:
  text: '体验css'
  link: '/blog/前端/css学习/1.体验css'
next:
  text: 'django web开发技术清单'
  link: '/blog/后端/Django/Django web开发技术清单'
---


<BlogInfo id="1" title="Find the way with dfs" author="白日梦想猿" pv=0 read_times=0 pre_cost_time="117" category="人工智能" tag_list="['数据结构', '                   dfs']" create_time="2023.08.27 00:05:46.036973" update_time="2023.08.29 23:05:29.746130" />

>
> 前言：最近在新的工作环境也慢慢适应了，又可以快乐的学习啦！因为工作的原因，很多地方都涉及到人工智能这一块的内容，以前对这一块有过一点点的涉略，但是对于大部分东西还是不明白的，加上之前有学这一块的打算，但是之前想着“学历”不够就算了，但是现在看来，在某种程度上，这是在给我自己设限，工作到现在，加上几段实习经历，遇到过很高学历的同学，但是他们也会觉得AI这一块水很深，不好学，也面临找工作难的问题.....所以大环境就是这样！学历不能代表一切，有实力才是硬道理！
>
>
> 思来想去，我觉得我之前所谓的“学历”不够而终止学习的根本原因就是：害怕找不到工作！害怕自己付出了努力，但是得不到相应的回报。而产生这些“害怕”的无非就是看到，听到网上的，别人那里的，短视频上的等等其他地方说的“本科生”不适合学习这一块的内容...
>
>
> 回到现在，我虽然不能以过来人的角度来说，但是我有底气说：我不会说因为这个学不好而怕找不到工作了，因为我本身就是后端开发，在开发这一块，我是有底气的！因此，我可以无忧无虑的去学，当作兴趣也好，或者当作自己将来的另一个赛道也罢，干它，就对了！
>
>
> 然后至于学习的路线的话，我是这样规划的，首先还是从基础开始，目前是跟着MIT的一个人工智能的[公开基础课](https://www.bilibili.com/video/BV1dM411U7qK?p=4&vd_source=95ef87e61d1c37fc15117824ffba69f5)开始的，学完这一块之后，会跟着李飞飞的计算机视觉的课程：[cs231n](https://www.bilibili.com/video/BV1mN4y1A7J1/?spm_id_from=333.999.0.0&vd_source=95ef87e61d1c37fc15117824ffba69f5)继续学习，同时我也买了一本关于相关的书：《深度学习》，跟着视频学习的过程，我也会刷一下书本的内容，两者都会跟进。

下面这段代码是基础课的一部分，是关于depth first search的一个实现方式（通过队列实现的），因为是国外的课程，所以笔记我也就一同用英文进行记录啦，一举双得，顺便也可以学一下英语，这也算是第一篇笔记，加油喽！

```python
# -*- coding: UTF-8 -*-  
# @Author  ：LLL   
# @Date    ：2023/8/26 15:04  
from collections import deque

# what is depth first search ?
# It's a way that you burrow ahead in a single minded way.(一路向前)

'''
 Q: how can i find a way from S to G with dfs ? 
  
            C --- E
            |
            |
       ---- B
      |     |
      |     |
      S --- A --- D --- G
 
 A:
    1. initialize a Queue
        put the S on the Queue
    2. extend first path on the Queue and check to see if that first path is a winner
        2.1 take the first path off and extend it(and check,if win then over,or continue...)
        2.2 put the new paths on front of the Queue
            Q: why should i put the new path on the front of the Queue?
            A: because i want to keep going down in the step that i just generated,i have to put
               it on the first so that i can deal with it first.(i think that is the core of dfs:
               find the new way and deal with it at the first time)  
   
 Process of dfs with a Queue:
    1.initialize a Queue and put the S on the Queue.
    Q = () 
    (S)    2.put S on the Queue
                     3.take off the S     check
    (S-A),(S-B)      4.put (S-A),(S-B) on the front
                     5.take off the (S-A) check 
    (S-A-B),(S-A-D),(S-B)  6.put (S-A-B),(S-A-D) on the first,and (S-B) is still there
                     7.take off the (S-A-B) check
    (S-A-B-C),(S-A-D),(S-B) 8.put (S-A-B-C) on the first
    ......
'''

def find_path_in_dfs(start, target, graph):
    # 1.define the Q
    queue = deque()
    if target not in graph:
        return
    queue.append([start])

    while queue:
        # 1.take off the first path
        cur_path = queue.popleft()
        end = cur_path[-1]
        # check if we get to the target
        if end == target:
            return cur_path

        # 2.find the new paths we can get to and extend
        neighbor_nodes = graph[end]
        for new_node in neighbor_nodes:
            if new_node not in cur_path:
                new_path = list(cur_path)
                new_path.append(new_node)

                # 3.put on the new path
                queue.appendleft(new_path)


if __name__ == '__main__':
    # 邻接表法来表示
    graph = {
        'A': {'B', 'D', 'S'},
        'B': {'A', 'C', 'S'},
        'C': {'B', 'E'},
        'D': {'A', 'G'},
        'E': {'C'},
        'G': {'D'},
        'S': {'A', 'B'},
        'W':{}
    }

    start = 'S'
    target = 'W'

    path = find_path_in_dfs(start, target, graph)
    print(f'the way S to G is :{path}')

```



