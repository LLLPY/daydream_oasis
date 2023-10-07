
<BlogInfo title="python求解迷宫问题，配js实现的走迷宫动画，动起来才有意思~" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=171 category="算法" tag_list="['算法', '栈', '迷宫求解']" create_time="2022.05.12 17:10:59.820927" update_time="2022.05.12 20:23:54" />

^^^^^^^^^
<h1>前言</h1>

<p>继昨天手动实现了走迷宫问题，虽然是实现了，但是看到被我画成乱七八糟的草稿纸，总是觉得不爽，不仔细看，又得把自己给走迷糊了，于是自己使用js实现了一下，效果还不错！先看一下展示效果吧！（文末配有js实现的代码）</p>

<p>不同的小方块代表不同的颜色，白色代表未走过的路，灰色代表墙，绿色代表走过的路，红色代表这条路走不通，即&ldquo;死路&rdquo;一条~</p>

<p>最后的截图：<img alt="" src="https://img-blog.csdnimg.cn/a97537d1d1184a13a0772b66acf42753.png" style="height:946px; width:900px" /></p>

<p>&nbsp;</p>

<h1>言归正传说说具体的思路吧~</h1>

<p>核心思想就是：<strong>我头铁，我就要一步一步的试！</strong><img alt="" src="https://img-blog.csdnimg.cn/a292489f74414c85a2cb3ca9647c227c.jpeg" style="height:81px; width:81px" />直到杀出一条血路出来，不，不，是试出一条汗路来<img alt="" src="https://img-blog.csdnimg.cn/c38b2b1d780a460493ddf7d4dbe429ce.png" style="height:32px; width:32px" /><img alt="" src="https://img-blog.csdnimg.cn/c38b2b1d780a460493ddf7d4dbe429ce.png" style="height:32px; width:32px" /><img alt="" src="https://img-blog.csdnimg.cn/c38b2b1d780a460493ddf7d4dbe429ce.png" style="height:32px; width:32px" />，（所以悄悄告诉你，这个方法的效率有点低哦<img alt="" src="https://img-blog.csdnimg.cn/6dd111f135f34238b3f730d66e3abceb.gif" style="height:82px; width:82px" />）</p>

<p>&nbsp;</p>

<h1>归纳总结一下，其实也就分两步走！</h1>

<h2>第一步&mdash;&mdash;&ldquo;四面楚歌&rdquo;</h2>

<p><img alt="" src="https://img-blog.csdnimg.cn/3a978fc48489458a94847719b8d3d284.png" style="height:561px; width:900px" /></p>

<p>&nbsp;为什么叫四面楚歌呢？就拿现在的这个局面给你说，你看上有吕布，下有阿珂，前有虞姬，后有个啥（我也看不清了<img alt="" src="https://img-blog.csdnimg.cn/c38b2b1d780a460493ddf7d4dbe429ce.png" style="height:32px; width:32px" />），要想杀出个血路，你会怎么办？那不得先拿菜鸡开刀嘛，你看这个吕布（<strong>上</strong>），别看它块头大，实际行动起来憨头憨老的，所以必须先拿他开刀，再看这个阿珂，虽然看她是满血，但是我就是头铁，我就是要拿她开刀，所以第二我会选她（<strong>下</strong>），其他的就留给你们自己挑吧！</p>

<p><img alt="" src="https://img-blog.csdnimg.cn/2fbcdd3f29574defbbd14487f9afdc17.png" style="height:284px; width:900px" /></p>

<h2>&nbsp;杀不出去怎么办？<img alt="" src="https://img-blog.csdnimg.cn/c38b2b1d780a460493ddf7d4dbe429ce.png" style="height:32px; width:32px" /></h2>

<h3>---------------------------------------等死嘛？</h3>

<p>不，你要相信，你就是光，上帝会伸出援助之手的！</p>

<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 你看！上帝让你重生了！考虑到你比较菜，上帝没有让你在原地复活，而是让你回到了上一步，并且为了不让你再走回头路，给你标记了你死亡的地点，希望你不要再误入迷途了，阿弥陀佛~</p>

<p><img alt="" src="https://img-blog.csdnimg.cn/8466088f8e734a748f61e069c0d4b99a.png" style="height:295px; width:900px" /></p>

<h1>&nbsp;第二步&mdash;&mdash;&ldquo;经历99八十一难，终得正果！&rdquo;</h1>

<p>不管你挂了多少次，不管上帝又让你复活了多少次，你从不觉疲倦，依旧任劳任怨，直到取得真经，修成正果的那一天！！！阿弥陀佛~</p>

<p><img src="../media/image/2022/05/12/image-20220512171049-1.png" style="height:697px; width:900px" /></p>

<p>直到有一天，上帝也看不下去了。。。</p>

<p>他说：阿空，我看你为取得真经，虽历经千幸万苦，但你始终不忘初心，砥砺前行，实数让我感动，现在我给你两条路，一条路是通往真经的路，一条路是通往地狱的，能不能取得真经，就看你自己的造化了。</p>

<p><img alt="" src="https://img-blog.csdnimg.cn/eff710e92e9d4330be318595aeb01d73.png" style="height:579px; width:900px" /></p>

<p>阿空会不会取得真经呢？</p>

<p>&nbsp;</p>

<p>&mdash;&mdash;预知后事如何，还得等您亲自操刀！源码如下：</p>

<p><img alt="" src="https://img-blog.csdnimg.cn/5898b7fb4bb04b4b8aee0834b9b55cf3.png" style="height:456px; width:900px" /></p>

<p>&nbsp;</p>

<h1>求解迷宫的源码：</h1>

<pre>
<code># -*- coding: UTF-8 -*-
&#39;&#39;&#39;
   *****************LLL*********************
   * @Project ：leetcode                       
   * @File    ：lll84_迷宫求解.py                  
   * @IDE     ：PyCharm             
   * @Author  ：LLL                         
   * @Date    ：2022/5/11 19:45             
   *****************************************
&#39;&#39;&#39;

# 迷宫
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

]

# 定义移动规则
steps = {
    0: lambda x, y: (x, y - 1),  # 上
    1: lambda x, y: (x, y + 1),  # 下
    2: lambda x, y: (x - 1, y),  # 左
    3: lambda x, y: (x + 1, y)  # 右
}


def maze_path(x1, y1, x2, y2):
    stack = [(x1, y1)]  # 起始点放入栈中
    while stack:
        # 取出栈顶元素
        cur_pos = stack[-1]
        steps_li.append([*cur_pos, maze[cur_pos[0]][cur_pos[1]]])
        if cur_pos == (x2, y2):
            steps_li.append([*cur_pos, 2])
            return stack

        # 试探下一步
        for i in range(4):
            next_x, next_y = steps[i](*cur_pos)
            if maze[next_x][next_y] == 0:
                maze[cur_pos[0]][cur_pos[1]] = 2  # 将走过的路标记为2
                steps_li.append([*cur_pos, maze[cur_pos[0]][cur_pos[1]]])

                cur_pos = (next_x, next_y)
                stack.append(cur_pos)
                break
        else:
            # 回退
            stack.pop()
            maze[cur_pos[0]][cur_pos[1]] = &#39;x&#39;  # 标记此处不可走
            steps_li.append([*cur_pos, maze[cur_pos[0]][cur_pos[1]]])

    return stack


if __name__ == &#39;__main__&#39;:
    steps_li = []
    path = maze_path(1, 1, 8, 8)
    print(path)  # 走出迷宫的路
    print(steps_li)  # 走过的所有的路
</code></pre>

<h1>js实现动画的源码：</h1>

<p>&nbsp;</p>

<pre>
<code>html&gt;
</code></pre>

<p>迷宫<!--<span class="hljs-name"-->title&gt;</p>

