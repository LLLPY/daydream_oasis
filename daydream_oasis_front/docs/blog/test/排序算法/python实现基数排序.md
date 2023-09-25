
<BlogInfo title="python实现基数排序" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=67 category="排序算法" tag_list="['排序算法', '基数排序']" create_time="2022.05.09 11:49:25.993005" update_time="2022.05.09 11:49:25" />

^^^^^^^^^
<h1>&nbsp;思路</h1>

<blockquote>
<pre>
先比较个位数，得到一个新的序列；再按照十位数排序，在上一个新序列的基础上又得到
一个新的序列；然后再按照百位数排序，在上一个新序列的基础上又得到一新的序列；
只到排到所有数中的最高位，依次输出列表，排序结束。</pre>
</blockquote>

<h1>栗子</h1>

<blockquote>
<pre>
例：li=[12,90,4,894,66]

可以看到，最高位有百位，因此我们可以将li看成是[012,090,004,894,066]

######################################################################################
[012,090,004,894,066]按照个位排序：

                                 894
                 090     012     004     066                
                  0   1   2   3   4   5   6   7   8   9   ---&gt;li=[090,012,004,894,066]
######################################################################################
 
 
######################################################################################
 [090,012,004,894,066]按照十位排序：
                                                     894
                 004 012                 066         090
                  0   1   2   3   4   5   6   7   8   9   ---&gt;li=[004,012,066,090,894]

######################################################################################

######################################################################################
li=[004,012,066,090,894]按照百位排序：
                 
                 090 
                 066
                 012
                 004                             894
                  0   1   2   3   4   5   6   7   8   9   ---&gt;li=[004,012,066,090,894]
######################################################################################

排序完成，得到li=[004,012,066,090,894]</pre>
</blockquote>

<h1>源码</h1>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-comment"># 基数排序</span>
<span class="hljs-meta">@clocked</span>
<span class="hljs-keyword">def</span> <span class="function_ hljs-title">radix_sort</span>(<span class="hljs-params">li</span>):
    n = <span class="hljs-number">1</span>
    <span class="hljs-keyword">while</span> <span class="hljs-literal">True</span>:
        buckets = [[] <span class="hljs-keyword">for</span> _ <span class="hljs-keyword">in</span> <span class="hljs-built_in">range</span>(<span class="hljs-number">10</span>)]
        flag = <span class="hljs-number">0</span>
        <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> <span class="hljs-built_in">range</span>(<span class="hljs-built_in">len</span>(li)):
            digit = li[i] // n % <span class="hljs-number">10</span>  <span class="hljs-comment"># 依次取出个位，十位，百位的数字...</span>
            buckets[digit].append(li[i])
            <span class="hljs-keyword">if</span> digit != <span class="hljs-number">0</span>: flag = <span class="hljs-number">1</span>  <span class="hljs-comment"># 只要有所有的数中，有一个数它的最高位不为0，说明循环就没有结束</span>
        n *= <span class="hljs-number">10</span>

        li.clear()
        <span class="hljs-keyword">for</span> bucket <span class="hljs-keyword">in</span> buckets: li.extend(bucket)
        <span class="hljs-built_in">print</span>(li)
        <span class="hljs-keyword">if</span> flag == <span class="hljs-number">0</span>:
            <span class="hljs-keyword">break</span></code></pre>

<h1>测试</h1>

<p>&nbsp;</p>

<p><img src="../media/image/2022/05/09/image-20220509114915-2.png" style="height:754px; width:900px" /></p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

