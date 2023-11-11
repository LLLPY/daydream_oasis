
<BlogInfo id="1350" title="python求解迷宫问题，配js实现的走迷宫动画，动起来才有意思~" author="白日梦想猿" pv=0 read_times=0 pre_cost_time="171" category="算法" tag_list="['算法', '              栈', '              迷宫求解']" create_time="2022.05.12 17:10:59.820927" update_time="2022.05.12 20:23:54" />

# 前言

继昨天手动实现了走迷宫问题，虽然是实现了，但是看到被我画成乱七八糟的草稿纸，总是觉得不爽，不仔细看，又得把自己给走迷糊了，于是自己使用js实现了一下，效果还不错！先看一下展示效果吧！（文末配有js实现的代码）

不同的小方块代表不同的颜色，白色代表未走过的路，灰色代表墙，绿色代表走过的路，红色代表这条路走不通，即"死路"一条~

最后的截图：![](https://img-blog.csdnimg.cn/a97537d1d1184a13a0772b66acf42753.png)



# 言归正传说说具体的思路吧~

核心思想就是： **我头铁，我就要一步一步的试！**![](https://img-blog.csdnimg.cn/a292489f74414c85a2cb3ca9647c227c.jpeg)
直到杀出一条血路出来，不，不，是试出一条汗路来![](https://img-blog.csdnimg.cn/c38b2b1d780a460493ddf7d4dbe429ce.png)![](https://img-blog.csdnimg.cn/c38b2b1d780a460493ddf7d4dbe429ce.png)![](https://img-blog.csdnimg.cn/c38b2b1d780a460493ddf7d4dbe429ce.png)，（所以悄悄告诉你，这个方法的效率有点低哦![](https://img-blog.csdnimg.cn/6dd111f135f34238b3f730d66e3abceb.gif)）



# 归纳总结一下，其实也就分两步走！

### 第一步----"四面楚歌"

![](https://img-blog.csdnimg.cn/3a978fc48489458a94847719b8d3d284.png)

 为什么叫四面楚歌呢？就拿现在的这个局面给你说，你看上有吕布，下有阿珂，前有虞姬，后有个啥（我也看不清了![](https://img-blog.csdnimg.cn/c38b2b1d780a460493ddf7d4dbe429ce.png)），要想杀出个血路，你会怎么办？那不得先拿菜鸡开刀嘛，你看这个吕布（**上** ），别看它块头大，实际行动起来憨头憨老的，所以必须先拿他开刀，再看这个阿珂，虽然看她是满血，但是我就是头铁，我就是要拿她开刀，所以第二我会选她（
**下** ），其他的就留给你们自己挑吧！

![](https://img-blog.csdnimg.cn/2fbcdd3f29574defbbd14487f9afdc17.png)

###  杀不出去怎么办？![](https://img-blog.csdnimg.cn/c38b2b1d780a460493ddf7d4dbe429ce.png)

---------------------------------------等死嘛？

不，你要相信，你就是光，上帝会伸出援助之手的！

你看！上帝让你重生了！考虑到你比较菜，上帝没有让你在原地复活，而是让你回到了上一步，并且为了不让你再走回头路，给你标记了你死亡的地点，希望你不要再误入迷途了，阿弥陀佛~

![](https://img-blog.csdnimg.cn/8466088f8e734a748f61e069c0d4b99a.png)

###  第二步----"经历99八十一难，终得正果！"

不管你挂了多少次，不管上帝又让你复活了多少次，你从不觉疲倦，依旧任劳任怨，直到取得真经，修成正果的那一天！！！阿弥陀佛~

![](http://www.lll.plus/media/image/2022/05/12/image-20220512171049-1.png)

直到有一天，上帝也看不下去了。。。

他说：阿空，我看你为取得真经，虽历经千幸万苦，但你始终不忘初心，砥砺前行，实数让我感动，现在我给你两条路，一条路是通往真经的路，一条路是通往地狱的，能不能取得真经，就看你自己的造化了。

![](https://img-blog.csdnimg.cn/eff710e92e9d4330be318595aeb01d73.png)

阿空会不会取得真经呢？


----预知后事如何，还得等您亲自操刀！源码如下：

![](https://img-blog.csdnimg.cn/5898b7fb4bb04b4b8aee0834b9b55cf3.png)


### 求解迷宫的源码

```python
# -*- coding: UTF-8 -*-
'''
   *****************LLL*********************
   * @Project ：leetcode                       
   * @File    ：lll84_迷宫求解.py                  
   * @IDE     ：PyCharm             
   * @Author  ：LLL                         
   * @Date    ：2022/5/11 19:45             
   *****************************************
'''

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
            maze[cur_pos[0]][cur_pos[1]] = 'x'  # 标记此处不可走
            steps_li.append([*cur_pos, maze[cur_pos[0]][cur_pos[1]]])

    return stack


if __name__ == '__main__':
    steps_li = []
    path = maze_path(1, 1, 8, 8)
    print(path)  # 走出迷宫的路
    print(steps_li)  # 走过的所有的路
```

### js实现动画的源码

```html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>迷宫</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        $(function () {
            //总路线
            let steps_li = [[1, 1, 0], [1, 1, 2], [2, 1, 0], [2, 1, 2], [2, 2, 0], [2, 2, 2], [2, 3, 0], [2, 3, 2], [2, 4, 0], [2, 4, 2], [2, 5, 0], [2, 5, 2], [3, 5, 0], [3, 5, 2], [4, 5, 0], [4, 5, 2], [5, 5, 0], [5, 5, 2], [5, 4, 0], [5, 4, 'x'], [5, 5, 2], [5, 5, 2], [6, 5, 0], [6, 5, 2], [7, 5, 0], [7, 5, 2], [7, 4, 0], [7, 4, 2], [7, 3, 0], [7, 3, 2], [7, 2, 0], [7, 2, 2], [7, 1, 0], [7, 1, 2], [6, 1, 0], [6, 1, 2], [6, 2, 0], [6, 2, 2], [5, 2, 0], [5, 2, 2], [5, 1, 0], [5, 1, 'x'], [5, 2, 2], [5, 2, 2], [4, 2, 0], [4, 2, 2], [3, 2, 0], [3, 2, 2], [3, 1, 0], [3, 1, 'x'], [3, 2, 2], [3, 2, 'x'], [4, 2, 2], [4, 2, 'x'], [5, 2, 2], [5, 2, 'x'], [6, 2, 2], [6, 2, 'x'], [6, 1, 2], [6, 1, 'x'], [7, 1, 2], [7, 1, 2], [8, 1, 0], [8, 1, 2], [8, 2, 0], [8, 2, 'x'], [8, 1, 2], [8, 1, 'x'], [7, 1, 2], [7, 1, 'x'], [7, 2, 2], [7, 2, 'x'], [7, 3, 2], [7, 3, 'x'], [7, 4, 2], [7, 4, 2], [8, 4, 0], [8, 4, 'x'], [7, 4, 2], [7, 4, 'x'], [7, 5, 2], [7, 5, 2], [7, 6, 0], [7, 6, 2], [7, 7, 0], [7, 7, 2], [7, 8, 0], [7, 8, 2], [6, 8, 0], [6, 8, 2], [6, 7, 0], [6, 7, 2], [5, 7, 0], [5, 7, 2], [5, 8, 0], [5, 8, 'x'], [5, 7, 2], [5, 7, 2], [4, 7, 0], [4, 7, 2], [3, 7, 0], [3, 7, 2], [2, 7, 0], [2, 7, 2], [2, 8, 0], [2, 8, 'x'], [2, 7, 2], [2, 7, 2], [1, 7, 0], [1, 7, 'x'], [2, 7, 2], [2, 7, 'x'], [3, 7, 2], [3, 7, 'x'], [4, 7, 2], [4, 7, 'x'], [5, 7, 2], [5, 7, 'x'], [6, 7, 2], [6, 7, 'x'], [6, 8, 2], [6, 8, 'x'], [7, 8, 2], [7, 8, 2], [8, 8, 0], [8, 8, 2]];
            let maze_box = $('#maze');
            let maze = [
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

            ];

            function get_span(flag) {
                var cur_class;
                if (flag === 0) {
                    cur_class = 'path';
                } else if (flag === 1) {
                    cur_class = 'block';
                } else if (flag === 2) {
                    cur_class = 'walked';
                } else {
                    cur_class = 'no_way'
                }

                return `<span class="${cur_class}"></span>`;

            }

            //构建迷宫
            function make_maze() {
                maze_box.empty();//构建之前先清空原有的
                let cur_span = ``;
                for (let i = 0; i < maze.length; i++) {
                    for (let j = 0; j < maze[0].length; j++) {
                        cur_span += get_span(maze[i][j]);
                    }
                }
                maze_box.append(cur_span);

            }

            //探寻 假设每隔300ms探寻依次
            let n = 0;
            setInterval(function () {
                let pos = steps_li[n];
                maze[pos[0]][pos[1]] = pos[2];
                make_maze();
                n += 1;

            }, 300);
        })

    </script>

    <style>
        * {
            padding: 0 !important;
            margin: 0;
        }

        #maze {
            border: 1px solid black;
            width: 500px;
            height: 500px;
            margin: 50px auto;
            line-height: 0;

        }

        span {
            width: 50px;
            height: 50px;
            display: inline-block;
            box-sizing: border-box;
            line-height: 50px;
            text-align: center;
            cursor: pointer;
            border: 1px solid black;


        }

        .block {
            background-color: grey;
            border: 1px solid black;

        }

        .path {

        }

        .walked {
            background-color: green;
        }

        .no_way {
            background-color: red;
        }

        #example {
            width: 250px;
            margin: 50px auto;
        }


    </style>
</head>
<body>

<div id="example">
    <span class="path">未走</span>
    <span class="block">墙</span>
    <span class="walked">已走</span>
    <span class="no_way">死路</span>
</div>

<div id="maze"></div>

</body>
</html>
```

