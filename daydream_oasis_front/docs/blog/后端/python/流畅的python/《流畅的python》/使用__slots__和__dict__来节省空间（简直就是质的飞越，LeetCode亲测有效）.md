
<BlogInfo id="781" title="使用__slots__和__dict__来节省空间（简直就是质的飞越，LeetCode亲测有效）" author="白日梦想猿" pv=0 read_times=0 pre_cost_time="77" category="《流畅的python》" tag_list="['笔记']" create_time="2022.07.15 18:03:39.509285" update_time="2022.07.15 18:03:39" />

###  定义

>         __slots__和__dict__都是两个特殊的类属性。

#### 1.__slots__

>         __slots__类属性的作用是指定当前类的实例所有包含的 **所有**
> 属性，注意是所有，就是只能是__slots__所指定的属性，不能包含其他以外的属性，也不能新建属性。在运行的时候，它存在的意义就在于告诉解释器：这个类中的所有实例属性都在这儿了！![](https://img-blog.csdnimg.cn/1714412ad5e94fab99d1b8099aeab493.png)
>
>  

#### 2.__dict__

>
> __dict__是用来存在实例属性的。就是说，当前实例有什么属性都会存储在这个字典中。__dict__存在提升了属性的访问速度，但是同时也带来了额外的空间消耗，因为__dict__它本质上就是一个字典，而字典是非常消耗空间的。![](https://img-blog.csdnimg.cn/8da37668c81f4f4bbd044f977aa02e45.png)
>
>  

### 测试

>
> 使用__slots__指定仅仅需要用到的几个属性，如果没有需要用到ed属性，则直接置空，这样在每次创建对象就不会创建额外的属性(包括__dict__属性)，从而大大节省了空间。
>
> ![](https://img-blog.csdnimg.cn/5aa3f39820174ff4aa5b4e2c9299a211.png)
>

这题是：[LCS 01. 下载插件](https://leetcode.cn/problems/Ju9Xwi/ "LCS 01.下载插件")
解题源码：

```python
from collections import deque
class Node:
    __slots__=('l','r','speed','val')
    def __init__(self, l=None, r=None, speed=None, val=None):
        self.l = l
        self.r = r
        self.speed = speed
        self.val = val
class Solution:
    __slots__=()
    def leastMinutes(self, n: int) -> int:
        if n==1:return 1
        root = Node()
        root.l = Node(None, None, 2, 0)  # 左孩子选择宽带加倍
        root.r = Node(None, None, 1, 1)  # 右孩子选择直接下载
        que = deque()
        que.append(root.l)
        que.append(root.r)
        N = 1
        while True:
            node_tmp = []
            flag = 0
            while len(que) > 0:
                cur_node = que.popleft()
                node_tmp.append(cur_node)
                new_l_val = cur_node.val
                if new_l_val >= n:
                    flag = 1
                    N+=1
                    break
                else:
                    new_l_speed = cur_node.speed * 2
                    cur_node.l = Node(None, None, new_l_speed, new_l_val)

                new_r_val = cur_node.val + cur_node.speed
                if new_r_val >= n:
                    flag = 1
                    N+=1
                    break
                else:
                    new_r_speed = cur_node.speed
                    cur_node.r = Node(None, None, new_r_speed, new_r_val)
            if flag:
                break
            else:
                N += 1
            while node_tmp:
                node = node_tmp.pop()
                if node.l: que.append(node.l)
                if node.r: que.append(node.r)
        return N
```






