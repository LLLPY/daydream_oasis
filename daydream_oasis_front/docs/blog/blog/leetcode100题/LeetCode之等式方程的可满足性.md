
<BlogInfo title="LeetCode之等式方程的可满足性" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=128 category="leetcode100题" tag_list="['leetcode', '并查集']" create_time="2022.07.21 16:52:09.842470" update_time="2022.07.21 16:52:09" />

^^^^^^^^^
<h1>&nbsp;题目</h1>

<blockquote>
<p>给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，并采用两种不同的形式之一：&quot;a==b&quot; 或&nbsp;&quot;a!=b&quot;。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。</p>

<p>只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回&nbsp;true，否则返回 false。&nbsp;</p>

<p>&nbsp;</p>

<p>示例 1：</p>

<p>输入：[&quot;a==b&quot;,&quot;b!=a&quot;]<br />
输出：false<br />
解释：如果我们指定，a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程。<br />
示例 2：</p>

<p>输入：[&quot;b==a&quot;,&quot;a==b&quot;]<br />
输出：true<br />
解释：我们可以指定 a = 1 且 b = 1 以满足满足这两个方程。<br />
示例 3：</p>

<p>输入：[&quot;a==b&quot;,&quot;b==c&quot;,&quot;a==c&quot;]<br />
输出：true<br />
示例 4：</p>

<p>输入：[&quot;a==b&quot;,&quot;b!=c&quot;,&quot;c==a&quot;]<br />
输出：false<br />
示例 5：</p>

<p>输入：[&quot;c==c&quot;,&quot;b==d&quot;,&quot;x!=z&quot;]<br />
输出：true<br />
&nbsp;</p>

<p>提示：</p>

<p>1 &lt;= equations.length &lt;= 500<br />
equations[i].length == 4<br />
equations[i][0] 和&nbsp;equations[i][3]&nbsp;是小写字母<br />
equations[i][1] 要么是&nbsp;&#39;=&#39;，要么是&nbsp;&#39;!&#39;<br />
equations[i][2]&nbsp;是&nbsp;&#39;=&#39;<br />
通过次数43,917提交次数83,897</p>

<p>来源：力扣（LeetCode）<br />
链接：https://leetcode.cn/problems/satisfiability-of-equality-equations<br />
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。</p>
</blockquote>

<h1>思路</h1>

<blockquote>
<p>一开始没有什么思路，然后查看了题解，基本上都是用并查集求解的。于是也试着用并查集写了下。</p>

<p>核心思想就是：</p>

<ul>
	<li>将相等的元素放在同一个集合中</li>
	<li>查询不相等的顶点是否属于同一个集合，如果是，直接返回False，如果所有的都不是，才返回True</li>
</ul>

<p>所以我这里定义了两个基本的方法，分别用于查找和合并：</p>

<p>查找：</p>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-comment"># 找到当前元素属于哪个集合，并返回那个集合的索引位置</span>
    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">find</span>(<span class="hljs-params">self, k: <span class="hljs-built_in">str</span>, set_li</span>):

        <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> <span class="hljs-built_in">range</span>(<span class="hljs-built_in">len</span>(set_li)):
            <span class="hljs-keyword">if</span> k <span class="hljs-keyword">in</span> set_li[i]:
                <span class="hljs-keyword">return</span> i
        <span class="hljs-keyword">else</span>:
            <span class="hljs-keyword">return</span> <span class="hljs-literal">None</span>  <span class="hljs-comment"># 不属于任何集合</span></code></pre>

<p>合并：</p>

<pre data-widget="codeSnippet">
<code class="hljs language-python"> <span class="hljs-comment"># 如果两个集合有交集就将它们合并</span>
    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">union</span>(<span class="hljs-params">self, k1, k2, li: <span class="hljs-built_in">list</span></span>):
        <span class="hljs-keyword">if</span> li[k1] &amp; li[k2]:
            li[k1] = li[k1] | li[k2]
            li.remove(li[k2])
            <span class="hljs-keyword">return</span> <span class="hljs-literal">True</span>
        <span class="hljs-keyword">return</span> <span class="hljs-literal">False</span></code></pre>

<p>整个思想就是：</p>

<p>1.先遍历整个equations列表，如果是等式，就将等式两边的变量添加(新建)到对应的集合；如果是不等式，就添加到一个不等式集合；</p>

<p>2.遍历不等式集合，查找不等式两边的变量是否在同一个等式集合中，如果在，直接返回False，如果都不在才返回True。</p>

<p><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/88cf4a0cb84846fc93133c6a61345869.png" style="height:498px; width:900px" /></p>

<p><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/ec8e10e619844af2b0a08dc16c4611f2.png" style="height:329px; width:900px" /></p>

<p>&nbsp;</p>

<p>&nbsp;</p>
</blockquote>

<h1>源码</h1>

<pre data-widget="codeSnippet">
<code class="hljs language-python">from typing import List

class Solution:
    def equationsPossible(self, equations: List[str]) -&gt; bool:
        # 把相等的顶点合并到同一个集合中
        # 查询两个顶点是否属于同一个集合
        equal_set_li = [set()]  # 用于存储相同的元素的集合
        tmp_not_equal_set = set()  # 用于存储不等式
        for equation in equations:
            if equation[1] == &#39;=&#39;:
                i = self.find(equation[0], equal_set_li) or self.find(equation[-1], equal_set_li)  # 查询当前元素所在集合的位置
                if i != None:  # 找到了
                    equal_set_li[i].add(equation[0])
                    equal_set_li[i].add(equation[-1])
                    # 合并
                    for k in range(len(equal_set_li)):
                        if k != i:
                            union_flag = self.union(k, i, equal_set_li)
                            if union_flag:
                                break
                else:
                    equal_set_li.append({equation[0], equation[-1]})

            else:
                if equation[0] == equation[-1]: return False
                tmp_not_equal_set.add(equation)

        # 判断两个字母是否在同一个集合中
        for tmp in tmp_not_equal_set:
            tmp_k1 = self.find(tmp[0], equal_set_li)
            tmp_k2 = self.find(tmp[-1], equal_set_li)
            # print(tmp_k1, tmp_k2)
            if tmp_k1 and tmp_k2 and tmp_k1 == tmp_k2: return False
        else:
            return True

    # 找到当前元素属于哪个集合，并返回那个集合的索引位置
    def find(self, k: str, set_li):

        for i in range(len(set_li)):
            if k in set_li[i]:
                return i
        else:
            return None  # 不属于任何集合

    # 如果两个集合有交集就将它们合并
    def union(self, k1, k2, li: list):
        if li[k1] &amp; li[k2]:
            li[k1] = li[k1] | li[k2]
            li.remove(li[k2])
            return True
        return False</code></pre>

<h1>通过截图</h1>

<p><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/a7685a72491946458577bd2b336ea592.png" style="height:361px; width:900px" /></p>

<p>&nbsp;</p>

