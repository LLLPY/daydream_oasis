
<BlogInfo title="使用__slots__和__dict__来节省空间（简直就是质的飞越，LeetCode亲测有效）" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=77 category="《流畅的python》" tag_list="['笔记']" create_time="2022.07.15 18:03:39.509285" update_time="2022.07.15 18:03:39" />

^^^^^^^^^
<h1>&nbsp;定义</h1>

<blockquote>
<p>&nbsp; &nbsp; &nbsp; &nbsp; __slots__和__dict__都是两个特殊的类属性。</p>
</blockquote>

<h2>1.__slots__</h2>

<blockquote>
<p>&nbsp; &nbsp; &nbsp; &nbsp; __slots__类属性的作用是指定当前类的实例所有包含的<strong>所有</strong>属性，注意是所有，就是只能是__slots__所指定的属性，不能包含其他以外的属性，也不能新建属性。在运行的时候，它存在的意义就在于告诉解释器：这个类中的所有实例属性都在这儿了！<img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/1714412ad5e94fab99d1b8099aeab493.png" style="height:781px; width:1295px" /></p>

<p>&nbsp;</p>
</blockquote>

<h2>2.__dict__</h2>

<blockquote>
<p>&nbsp; &nbsp; &nbsp; &nbsp; __dict__是用来存在实例属性的。就是说，当前实例有什么属性都会存储在这个字典中。__dict__存在提升了属性的访问速度，但是同时也带来了额外的空间消耗，因为__dict__它本质上就是一个字典，而字典是非常消耗空间的。<img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/8da37668c81f4f4bbd044f977aa02e45.png" style="height:781px; width:1385px" /></p>

<p>&nbsp;</p>
</blockquote>

<h1>测试</h1>

<blockquote>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;使用__slots__指定仅仅需要用到的几个属性，如果没有需要用到ed属性，则直接置空，这样在每次创建对象就不会创建额外的属性(包括__dict__属性)，从而大大节省了空间。</p>

<p><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/5aa3f39820174ff4aa5b4e2c9299a211.png" style="height:861px; width:1542px" /></p>

<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;这题是：<a contenteditable="true" data-link-icon="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666" data-link-title="LCS 01. 下载插件" data-widget="csdnlink" href="https://leetcode.cn/problems/Ju9Xwi/" title="LCS 01. 下载插件">LCS 01. 下载插件</a></p>

<p>&nbsp; &nbsp; &nbsp; &nbsp; 解题源码：</p>

<pre data-widget="codeSnippet">
<code class="hljs language-python">from collections import deque
class Node:
    __slots__=(&#39;l&#39;,&#39;r&#39;,&#39;speed&#39;,&#39;val&#39;)
    def __init__(self, l=None, r=None, speed=None, val=None):
        self.l = l
        self.r = r
        self.speed = speed
        self.val = val
class Solution:
    __slots__=()
    def leastMinutes(self, n: int) -&gt; int:
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
            while len(que) &gt; 0:
                cur_node = que.popleft()
                node_tmp.append(cur_node)
                new_l_val = cur_node.val
                if new_l_val &gt;= n:
                    flag = 1
                    N+=1
                    break
                else:
                    new_l_speed = cur_node.speed * 2
                    cur_node.l = Node(None, None, new_l_speed, new_l_val)

                new_r_val = cur_node.val + cur_node.speed
                if new_r_val &gt;= n:
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
        return N</code></pre>

<p>&nbsp;</p>
</blockquote>

<p>&nbsp;</p>

<p>&nbsp;</p>

