
<BlogInfo title="python实现二叉搜索树" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=151 category="树与二叉树" tag_list="['二叉树', '二叉排序树']" create_time="2022.06.04 19:48:37.607665" update_time="2022.06.04 19:48:37" />

^^^^^^^^^
<p>&nbsp;</p>

<h1>&nbsp;笔记</h1>

<p>python实现二叉搜索树</p>

<pre data-widget="codeSnippet">
<code class="language-python hljs"><span class="hljs-comment"># -*- coding: UTF-8 -*-</span>
<span class="hljs-string">&#39;&#39;&#39;
   *****************LLL*********************
   * @Project ：leetcode                       
   * @File    ：lll_110二叉搜索树.py                  
   * @IDE     ：PyCharm             
   * @Author  ：LLL                         
   * @Date    ：2022/6/3 17:41             
   *****************************************
&#39;&#39;&#39;</span>
<span class="hljs-keyword">from</span> random <span class="hljs-keyword">import</span> shuffle


<span class="hljs-comment"># binary search tree</span>
<span class="hljs-keyword">class</span> <span class="class_ hljs-title">BST</span>:
    <span class="hljs-comment"># 树节点</span>
    <span class="hljs-keyword">class</span> <span class="class_ hljs-title">TreeNode</span>:
        <span class="hljs-keyword">def</span> <span class="function_ hljs-title">__init__</span>(<span class="hljs-params">self, val, lchild=<span class="hljs-literal">None</span>, rchild=<span class="hljs-literal">None</span>, parent=<span class="hljs-literal">None</span></span>):
            self.val = val
            self.lchild = lchild
            self.rchild = rchild
            self.parent = parent

    <span class="hljs-comment"># 初始化根节点为空</span>
    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">__init__</span>(<span class="hljs-params">self, li</span>):
        self.root = <span class="hljs-literal">None</span>
        <span class="hljs-keyword">if</span> li:
            <span class="hljs-keyword">for</span> val <span class="hljs-keyword">in</span> li:
                self.insert_no_rec(val)

    <span class="hljs-comment"># 插入(递归写法) 从根节点开始，查找适合插入的位置</span>
    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">insert</span>(<span class="hljs-params">self, root, val</span>):
        <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> root:
            root = self.TreeNode(val)
        <span class="hljs-keyword">elif</span> val &lt; root.val:
            root.lchild = self.insert(root.lchild, val)
            root.lchild.parent = root
        <span class="hljs-keyword">elif</span> val &gt; root.val:
            root.rchild = self.insert(root.rchild, val)
            root.rchild.parent = root
        <span class="hljs-keyword">else</span>:
            <span class="hljs-keyword">pass</span>
        <span class="hljs-keyword">return</span> root

    <span class="hljs-comment"># 插入(非递归写法)</span>
    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">insert_no_rec</span>(<span class="hljs-params">self, val</span>):
        tmp_node = self.root
        <span class="hljs-comment"># 如果没有根节点</span>
        <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> tmp_node:
            self.root = self.TreeNode(val)
            <span class="hljs-keyword">return</span>

        <span class="hljs-keyword">while</span> tmp_node:
            <span class="hljs-keyword">if</span> val &lt; tmp_node.val:
                <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> tmp_node.lchild:  <span class="hljs-comment"># 为None说明已经到了叶子结点</span>
                    tmp_node.lchild = self.TreeNode(val)
                    tmp_node.lchild.parent = tmp_node
                    <span class="hljs-keyword">return</span>
                tmp_node = tmp_node.lchild
            <span class="hljs-keyword">elif</span> val &gt; tmp_node.val:
                <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> tmp_node.rchild:
                    tmp_node.rchild = self.TreeNode(val)
                    tmp_node.rchild.parent = tmp_node
                    <span class="hljs-keyword">return</span>
                tmp_node = tmp_node.rchild
            <span class="hljs-keyword">else</span>:
                <span class="hljs-keyword">return</span>

    <span class="hljs-comment"># 查询(递归写法)</span>
    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">query</span>(<span class="hljs-params">self, root, val</span>):
        <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> root: <span class="hljs-keyword">return</span>  <span class="hljs-comment"># 如果没有根 返回None</span>
        <span class="hljs-keyword">if</span> val &lt; root.val:  <span class="hljs-comment"># 小于 就在左子树上查找</span>
            <span class="hljs-keyword">return</span> self.query(root.lchild, val)
        <span class="hljs-keyword">if</span> val &gt; root.val:  <span class="hljs-comment"># 大于 就在右子树上查找</span>
            <span class="hljs-keyword">return</span> self.query(root.rchild, val)
        <span class="hljs-keyword">else</span>:  <span class="hljs-comment"># 等于就直接返回当前节点</span>
            <span class="hljs-keyword">return</span> root

    <span class="hljs-comment"># 查询(非递归写法)</span>
    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">query_no_rec</span>(<span class="hljs-params">self, val</span>):
        tmp_node = self.root
        <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> tmp_node: <span class="hljs-keyword">return</span>

        <span class="hljs-keyword">while</span> tmp_node:
            <span class="hljs-keyword">if</span> val &lt; tmp_node.val:  <span class="hljs-comment"># 小于就查找左子树</span>
                tmp_node = tmp_node.lchild
            <span class="hljs-keyword">elif</span> val &gt; tmp_node.val:  <span class="hljs-comment"># 大于就查找右子树</span>
                tmp_node = tmp_node.rchild
            <span class="hljs-keyword">else</span>:
                <span class="hljs-keyword">return</span> tmp_node

    <span class="hljs-comment"># 删除</span>
    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">delete</span>(<span class="hljs-params">self, val</span>):
        <span class="hljs-comment"># 三种情况</span>
        <span class="hljs-string">&#39;&#39;&#39;
        1.如果要删除的节点是叶子结点，直接删除
        2.如果要删除的节点只有一个孩子（不管是左孩子还是右孩子），将其孩子连向其父亲，然后删除该节点
        3.如果要删除的节点有两个孩子，寻找左子树的最大节点（或者右子树的最小节点）替换当前节点
        &#39;&#39;&#39;</span>

        tmp_node = self.query_no_rec(val)
        <span class="hljs-keyword">if</span> tmp_node:
            <span class="hljs-comment"># 情况1</span>
            <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> tmp_node.lchild <span class="hljs-keyword">and</span> <span class="hljs-keyword">not</span> tmp_node.rchild:  <span class="hljs-comment"># 如果是叶子节点</span>
                <span class="hljs-keyword">if</span> tmp_node.parent:
                    <span class="hljs-keyword">if</span> tmp_node.parent.lchild == tmp_node:
                        tmp_node.parent.lchild = <span class="hljs-literal">None</span>
                    <span class="hljs-keyword">else</span>:
                        tmp_node.parent.rchild = <span class="hljs-literal">None</span>
                <span class="hljs-keyword">else</span>:  <span class="hljs-comment"># 如果是根节点</span>
                    self.root = <span class="hljs-literal">None</span>
            <span class="hljs-comment"># 情况2</span>
            <span class="hljs-keyword">elif</span> tmp_node.lchild:
                tmp_node.parent.lchild = tmp_node.lchild
                tmp_node.lchild.parent = tmp_node.parent

            <span class="hljs-keyword">elif</span> tmp_node.rchild:
                tmp_node.parent.rchild = tmp_node.rchild
                tmp_node.rchild.parent = tmp_node.parent

            <span class="hljs-comment"># 情况3</span>
            <span class="hljs-keyword">else</span>:
                tmp_node2 = tmp_node.rchild  <span class="hljs-comment"># 右子树</span>
                <span class="hljs-keyword">while</span> tmp_node2.lchild:  <span class="hljs-comment"># 寻找右子树值最小的节点</span>
                    tmp_node2 = tmp_node2.lchild

                tmp_node3 = tmp_node2.parent
                <span class="hljs-keyword">while</span> tmp_node3.rchild:
                    tmp_node3 = tmp_node3.rchild

                tmp_node.val = tmp_node2.val
                tmp_node2.parent.lchild = <span class="hljs-literal">None</span>
                tmp_node3.rchild = tmp_node2.rchild
                tmp_node2.rchild.parent = tmp_node3
        <span class="hljs-keyword">else</span>:
            <span class="hljs-built_in">print</span>(<span class="hljs-string">&#39;要删除的节点不存在！&#39;</span>)

    <span class="hljs-comment"># 前序遍历</span>
    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">pre_order</span>(<span class="hljs-params">self, root</span>):
        <span class="hljs-keyword">if</span> root:
            <span class="hljs-built_in">print</span>(root.val, end=<span class="hljs-string">&#39; &#39;</span>)
            self.in_order(root.lchild)
            self.in_order(root.rchild)

    <span class="hljs-comment"># 中序遍历</span>
    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">in_order</span>(<span class="hljs-params">self, root</span>):
        <span class="hljs-keyword">if</span> root:
            self.in_order(root.lchild)
            <span class="hljs-built_in">print</span>(root.val, end=<span class="hljs-string">&#39; &#39;</span>)
            self.in_order(root.rchild)

    <span class="hljs-comment"># 后序遍历</span>
    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">post_order</span>(<span class="hljs-params">self, root</span>):
        <span class="hljs-keyword">if</span> root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            <span class="hljs-built_in">print</span>(root.val, end=<span class="hljs-string">&#39; &#39;</span>)


<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">&#39;__main__&#39;</span>:
    li = <span class="hljs-built_in">list</span>(<span class="hljs-built_in">range</span>(<span class="hljs-number">1</span>, <span class="hljs-number">20</span>))
    shuffle(li)
    bst = BST(li)
    <span class="hljs-built_in">print</span>()
    <span class="hljs-comment"># bst.pre_order(bst.root)</span>
    <span class="hljs-built_in">print</span>()
    bst.in_order(bst.root)
    bst.delete(<span class="hljs-number">1</span>)
    <span class="hljs-comment"># bst.delete(2)</span>
    <span class="hljs-comment"># bst.delete(16)</span>
    <span class="hljs-comment"># bst.delete(19)</span>
    <span class="hljs-built_in">print</span>()
    bst.in_order(bst.root)
</code></pre>

