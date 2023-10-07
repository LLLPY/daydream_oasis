
<BlogInfo title="python实现线索二叉树（以先序线索化为例）" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=141 category="树与二叉树" tag_list="['二叉树', '线索化']" create_time="2022.05.16 12:25:26.783677" update_time="2022.05.16 12:25:26" />

^^^^^^^^^
<h1>&nbsp;背景</h1>

<p>给定一棵树中的某一个节点，让你找出这个节点的先序遍历的直接前驱，如果是一颗普通的树，因为指向的单向性，你只能建立两个指针pre,cur_node，pre紧接在cur_node的后面，从头遍历到尾，如果cur_node指向了要找的节点，那么pre就是要找的节点的直接前驱。</p>

<p>可以看到，无论给定的节点在哪里，都需要从根节点开始从头遍历，所以效率是非常低的。</p>

<p>&nbsp;</p>

<h1>节点的定义</h1>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-keyword">class</span> <span class="class_ hljs-title">TreeNode</span>:
    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">__init__</span>(<span class="hljs-params">self, val=<span class="hljs-literal">None</span>, left=<span class="hljs-literal">None</span>, right=<span class="hljs-literal">None</span>, ltag=<span class="hljs-number">0</span>, rtag=<span class="hljs-number">0</span></span>):
        self.val = val  <span class="hljs-comment"># 值</span>
        self.left = left  <span class="hljs-comment"># 左孩子</span>
        self.right = right  <span class="hljs-comment"># 右孩子</span>
        self.ltag = ltag  <span class="hljs-comment"># 初始值为0 为0说明指向左孩子，为1说明指向直接前驱</span>
        self.rtag = rtag  <span class="hljs-comment"># 初始值为0 为0说明指向右孩子，为1说明指向直接后继</span>
</code></pre>

<h1>构建一颗树</h1>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-comment"># 创建一颗二叉树(层次遍历)</span>
<span class="hljs-keyword">def</span> <span class="function_ hljs-title">create_tree</span>(<span class="hljs-params">li</span>):
    <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> li: <span class="hljs-keyword">return</span> TreeNode()
    root = TreeNode(li[<span class="hljs-number">0</span>])
    cur_que = deque()
    cur_que.append(root)
    li = li[<span class="hljs-number">1</span>:][::-<span class="hljs-number">1</span>]
    <span class="hljs-keyword">while</span> <span class="hljs-built_in">len</span>(cur_que):
        cur_node = cur_que.popleft()
        <span class="hljs-keyword">if</span> li:
            cur_node.left = TreeNode(li.pop())
            cur_que.append(cur_node.left)

        <span class="hljs-keyword">if</span> li:
            cur_node.right = TreeNode(li.pop())
            cur_que.append(cur_node.right)
    <span class="hljs-keyword">return</span> root</code></pre>

<h1>先序遍历线索化</h1>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-comment"># 先序遍历</span>
<span class="hljs-keyword">def</span> <span class="function_ hljs-title">travel</span>(<span class="hljs-params">root</span>):
    <span class="hljs-keyword">if</span> root:
        vist(root)
        <span class="hljs-keyword">global</span> pre
        pre = root  <span class="hljs-comment"># 更新前驱</span>
        <span class="hljs-keyword">if</span> root.ltag == <span class="hljs-number">0</span>:  <span class="hljs-comment"># 如果是左孩子就访问</span>
            travel(root.left)

        <span class="hljs-keyword">if</span> root.rtag == <span class="hljs-number">0</span>:  <span class="hljs-comment"># 如果是右孩子就访问</span>
            travel(root.right)</code></pre>

<h1>线索化的核心</h1>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-comment"># 访问当前节点</span>
<span class="hljs-keyword">def</span> <span class="function_ hljs-title">vist</span>(<span class="hljs-params">cur_node</span>):
    <span class="hljs-keyword">global</span> pre
    <span class="hljs-keyword">if</span> pre:
        <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> cur_node.left:  <span class="hljs-comment"># 当前节点没有左孩子，且前驱pre不为空</span>
            cur_node.left = pre  <span class="hljs-comment"># 指向它的直接前驱</span>
            cur_node.ltag = <span class="hljs-number">1</span>  <span class="hljs-comment"># 标记当前左指针指向的是直接前驱</span>
        <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> pre.right <span class="hljs-keyword">and</span> cur_node:  <span class="hljs-comment"># pre没有右孩子 且cur_node不为空</span>
            pre.right = cur_node  <span class="hljs-comment"># cur_node就是pre的直接后继</span>
            pre.rtag = <span class="hljs-number">1</span>  <span class="hljs-comment"># 标记当前右指针指向的是直接后继</span></code></pre>

<h1>测试</h1>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-comment"># 线索化</span>
<span class="hljs-keyword">def</span> <span class="function_ hljs-title">thread_tree</span>(<span class="hljs-params">root</span>):
    <span class="hljs-keyword">global</span> pre  <span class="hljs-comment"># 设为全局变量 一开始指向None</span>
    pre = <span class="hljs-literal">None</span>
    travel(root)
    <span class="hljs-keyword">return</span> root


<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">&#39;__main__&#39;</span>:
    root = create_tree([<span class="hljs-string">&#39;A&#39;</span>, <span class="hljs-string">&#39;B&#39;</span>, <span class="hljs-string">&#39;C&#39;</span>, <span class="hljs-string">&#39;D&#39;</span>, <span class="hljs-string">&#39;E&#39;</span>, <span class="hljs-string">&#39;F&#39;</span>, <span class="hljs-string">&#39;G&#39;</span>])
    thread_tree(root)</code></pre>

<p>这里使用Tutor进行了运行过程的可视化，最终结果如下（符合预期）：</p>

<p><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/ec0705c50e4b4c8fa1edb22c88e2f597.png" style="height:729px; width:900px" /><img src="../media/image/2022/05/16/image-20220516122517-1.png" style="height:245px; width:900px" /></p>

<h1>源码</h1>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-comment"># -*- coding: UTF-8 -*-</span>
<span class="hljs-string">&#39;&#39;&#39;
   *****************LLL*********************
   * @Project ：leetcode                       
   * @File    ：lll97_二叉树的线索化.py                  
   * @IDE     ：PyCharm             
   * @Author  ：LLL                         
   * @Date    ：2022/5/16 10:30             
   *****************************************
&#39;&#39;&#39;</span>
<span class="hljs-keyword">from</span> collections <span class="hljs-keyword">import</span> deque


<span class="hljs-keyword">class</span> <span class="class_ hljs-title">TreeNode</span>:
    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">__init__</span>(<span class="hljs-params">self, val=<span class="hljs-literal">None</span>, left=<span class="hljs-literal">None</span>, right=<span class="hljs-literal">None</span>, ltag=<span class="hljs-number">0</span>, rtag=<span class="hljs-number">0</span></span>):
        self.val = val  <span class="hljs-comment"># 值</span>
        self.left = left  <span class="hljs-comment"># 左孩子</span>
        self.right = right  <span class="hljs-comment"># 右孩子</span>
        self.ltag = ltag  <span class="hljs-comment"># 初始值为0 为0说明指向左孩子，为1说明指向直接前驱</span>
        self.rtag = rtag  <span class="hljs-comment"># 初始值为0 为0说明指向右孩子，为1说明指向直接后继</span>


<span class="hljs-comment"># 创建一颗二叉树(层次遍历)</span>
<span class="hljs-keyword">def</span> <span class="function_ hljs-title">create_tree</span>(<span class="hljs-params">li</span>):
    <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> li: <span class="hljs-keyword">return</span> TreeNode()
    root = TreeNode(li[<span class="hljs-number">0</span>])
    cur_que = deque()
    cur_que.append(root)
    li = li[<span class="hljs-number">1</span>:][::-<span class="hljs-number">1</span>]
    <span class="hljs-keyword">while</span> <span class="hljs-built_in">len</span>(cur_que):
        cur_node = cur_que.popleft()
        <span class="hljs-keyword">if</span> li:
            cur_node.left = TreeNode(li.pop())
            cur_que.append(cur_node.left)

        <span class="hljs-keyword">if</span> li:
            cur_node.right = TreeNode(li.pop())
            cur_que.append(cur_node.right)
    <span class="hljs-keyword">return</span> root


<span class="hljs-comment"># 访问当前节点</span>
<span class="hljs-keyword">def</span> <span class="function_ hljs-title">vist</span>(<span class="hljs-params">cur_node</span>):
    <span class="hljs-keyword">global</span> pre
    <span class="hljs-keyword">if</span> pre:
        <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> cur_node.left:  <span class="hljs-comment"># 当前节点没有左孩子，且前驱pre不为空</span>
            cur_node.left = pre  <span class="hljs-comment"># 指向它的直接前驱</span>
            cur_node.ltag = <span class="hljs-number">1</span>  <span class="hljs-comment"># 标记当前左指针指向的是直接前驱</span>
        <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> pre.right <span class="hljs-keyword">and</span> cur_node:  <span class="hljs-comment"># pre没有右孩子 且cur_node不为空</span>
            pre.right = cur_node  <span class="hljs-comment"># cur_node就是pre的直接后继</span>
            pre.rtag = <span class="hljs-number">1</span>  <span class="hljs-comment"># 标记当前右指针指向的是直接后继</span>


<span class="hljs-comment"># 先序遍历</span>
<span class="hljs-keyword">def</span> <span class="function_ hljs-title">travel</span>(<span class="hljs-params">root</span>):
    <span class="hljs-keyword">if</span> root:
        vist(root)
        <span class="hljs-keyword">global</span> pre
        pre = root  <span class="hljs-comment"># 更新前驱 pre总是等于上一轮的root</span>
        <span class="hljs-keyword">if</span> root.ltag == <span class="hljs-number">0</span>:  <span class="hljs-comment"># 如果是左孩子就访问</span>
            travel(root.left)

        <span class="hljs-keyword">if</span> root.rtag == <span class="hljs-number">0</span>:  <span class="hljs-comment"># 如果是右孩子就访问</span>
            travel(root.right)


<span class="hljs-comment"># 线索化</span>
<span class="hljs-keyword">def</span> <span class="function_ hljs-title">thread_tree</span>(<span class="hljs-params">root</span>):
    <span class="hljs-keyword">global</span> pre  <span class="hljs-comment"># 设为全局变量 一开始指向None</span>
    pre = <span class="hljs-literal">None</span>
    travel(root)
    <span class="hljs-keyword">return</span> root


<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">&#39;__main__&#39;</span>:
    root = create_tree([<span class="hljs-string">&#39;A&#39;</span>, <span class="hljs-string">&#39;B&#39;</span>, <span class="hljs-string">&#39;C&#39;</span>, <span class="hljs-string">&#39;D&#39;</span>, <span class="hljs-string">&#39;E&#39;</span>, <span class="hljs-string">&#39;F&#39;</span>, <span class="hljs-string">&#39;G&#39;</span>])
    thread_tree(root)
</code></pre>

<p>&nbsp;</p>

