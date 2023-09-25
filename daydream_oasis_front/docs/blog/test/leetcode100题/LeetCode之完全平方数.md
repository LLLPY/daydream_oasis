
<BlogInfo title="LeetCode之完全平方数" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=76 category="leetcode100题" tag_list="['leetcode', '动态规划']" create_time="2022.07.13 08:39:20.001563" update_time="2022.07.13 08:39:20" />

^^^^^^^^^
<h1><strong>题目</strong></h1>

<blockquote>
<p>&nbsp;</p>

<p><strong>给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。</strong></p>

<p><strong>完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。</strong></p>

<p><strong>&nbsp;</strong></p>

<p><strong>示例&nbsp;1：</strong></p>

<p><strong>输入：n = 12<br />
输出：3&nbsp;<br />
解释：12 = 4 + 4 + 4<br />
示例 2：</strong></p>

<p><strong>输入：n = 13<br />
输出：2<br />
解释：13 = 4 + 9<br />
&nbsp;<br />
提示：</strong></p>

<p><strong>1 &lt;= n &lt;= 104</strong></p>

<p><strong>来源：力扣（LeetCode）<br />
链接：https://leetcode.cn/problems/perfect-squares<br />
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。</strong></p>
</blockquote>

<h1><strong>思路</strong></h1>

<blockquote>
<p><strong>核心思想还是动态规划，空间换区时间。</strong></p>

<p>所以，确定好是动态规划后，我们第一步就先找出动态规划的方程（如下图解）。</p>

<p><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/5b30386778d64805b311a7fdd3d40933.png" style="height:755px; width:1162px" /></p>

<p>&nbsp;根据如上图解，我们可以进一步细化解题步骤：</p>

<ol>
	<li>求出n以内的所有完全平方数</li>
	<li>初始化一个dp数组</li>
	<li>根据状态转移方程，动态求解每一步的结果</li>
</ol>

<h2><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/98d1374dba5d4e83ae40822bc57edbab.gif" style="height:43px; width:43px" />1.求出n以内的所有完全平方数</h2>

<pre data-widget="codeSnippet">
<code class="language-python hljs"><span class="hljs-comment"># 求出n之内的所有完全平方数</span>
        pow_li = []
        <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> <span class="hljs-built_in">range</span>(<span class="hljs-number">1</span>, n // <span class="hljs-number">2</span> + <span class="hljs-number">1</span>):
            cur = i ** <span class="hljs-number">2</span>
            <span class="hljs-keyword">if</span> cur &lt;= n:
                pow_li.append(cur)
            <span class="hljs-keyword">else</span>:
                <span class="hljs-keyword">break</span></code></pre>

<p>&nbsp;由n&ge;1/2时，n&sup2;&ge;n/2,所以只需要遍历到n/2即可。</p>

<h2><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/0d55f4829e4f4da29b02f6e607d384b9.gif" style="height:47px; width:47px" />2.初始化一个dp数组</h2>

<p>&nbsp;</p>

<pre data-widget="codeSnippet">
<code class="language-python hljs">dp = [i <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> <span class="hljs-built_in">range</span>(n + <span class="hljs-number">1</span>)]  <span class="hljs-comment"># dp[1]=1</span></code></pre>

<p>&nbsp;因为1是最小的完全平方数，所以最坏情况就是都是由1这一个完全平方数组成的。</p>

<h2><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/539e319695974b6f9eafa72c129c3ef5.gif" style="height:48px; width:48px" />3.根据状态转移方程，动态求解每一步的结果</h2>

<p>&nbsp;</p>

<pre data-widget="codeSnippet">
<code class="language-python hljs"> <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> <span class="hljs-built_in">range</span>(<span class="hljs-number">2</span>, n + <span class="hljs-number">1</span>):  <span class="hljs-comment"># 从dp[2]开始</span>
            <span class="hljs-keyword">for</span> tmp <span class="hljs-keyword">in</span> pow_li:
                <span class="hljs-keyword">if</span> i &gt;= tmp:
                    dp[i] = <span class="hljs-built_in">min</span>(dp[i - tmp] + <span class="hljs-number">1</span>, dp[i])
                <span class="hljs-keyword">else</span>:
                    <span class="hljs-keyword">break</span></code></pre>

<p>&nbsp;dp[1]=1,所以直接从dp[2]开始，求解dp[i]时，依次遍历完全平方数列表直到找出最小值即可。</p>

<p>&nbsp;</p>
</blockquote>

<h1>源码</h1>

<pre data-widget="codeSnippet">
<code class="language-python hljs">class Solution:
    def numSquares(self, n: int) -&gt; int:

        # 动态规划求解
        &#39;&#39;&#39;

        &#39;&#39;&#39;

        # 求出n之内的所有完全平方数
        pow_li = []
        for i in range(1, n // 2 + 1):
            cur = i ** 2
            if cur &lt;= n:
                pow_li.append(cur)
            else:
                break
        dp = [i for i in range(n + 1)]  # dp[1]=1
        for i in range(2, n + 1):  # 从dp[2]开始
            for tmp in pow_li:
                if i &gt;= tmp:
                    dp[i] = min(dp[i - tmp] + 1, dp[i])
                else:
                    break
        return dp[n]</code></pre>

<h1>通过截图</h1>

<p><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/4f398da809fb4e7892fedc3cf80bbb9f.png" style="height:559px; width:927px" /></p>

<p>&nbsp;</p>

