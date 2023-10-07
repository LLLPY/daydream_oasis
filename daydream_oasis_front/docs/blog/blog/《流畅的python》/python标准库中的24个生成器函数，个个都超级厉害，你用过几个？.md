
<BlogInfo title="python标准库中的24个生成器函数，个个都超级厉害，你用过几个？" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=209 category="《流畅的python》" tag_list="['生成器函数']" create_time="2022.04.18 09:44:17.133579" update_time="2022.04.18 09:44:17" />

^^^^^^^^^
<h1>前言</h1>

<p>标准库提供了很多生成器，有些是内置的，有些在itertools和functools模块中，下面我们就按照它们的功能进行分组来看看它们吧！</p>

<p>&nbsp;</p>

<h1>用于过滤的生成器函数</h1>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-keyword">import</span> itertools

<span class="hljs-comment"># itertools.compress(it,selector_it)</span>
<span class="hljs-comment"># 并行处理两个可迭代对象，如果selector_it中的元素是真值，产出it中对应的元素</span>
<span class="hljs-built_in">print</span>([i <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> itertools.compress(<span class="hljs-built_in">range</span>(<span class="hljs-number">10</span>), [<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">1</span>])])

<span class="hljs-comment"># itertools.takewhile(predicate,it)</span>
<span class="hljs-comment"># 使用传入的生成器生成另一个生成器，predicate指定终止条件</span>
<span class="hljs-built_in">print</span>([i <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> itertools.takewhile(<span class="hljs-keyword">lambda</span> n: n &lt; <span class="hljs-number">5</span>, <span class="hljs-built_in">range</span>(<span class="hljs-number">10</span>))])

<span class="hljs-comment"># itertools.dropwhile(prdicate,it)</span>
<span class="hljs-comment"># 与itertools.takewhile的作用相反</span>
<span class="hljs-built_in">print</span>([i <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> itertools.dropwhile(<span class="hljs-keyword">lambda</span> n: n &lt; <span class="hljs-number">5</span>, <span class="hljs-built_in">range</span>(<span class="hljs-number">10</span>))])

<span class="hljs-comment"># filter(predicate,it)</span>
<span class="hljs-comment"># 将it中的各个元素传给predicate，如果为真，则产出it中对应的元素</span>
<span class="hljs-built_in">print</span>([i <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> <span class="hljs-built_in">filter</span>(<span class="hljs-keyword">lambda</span> a: a % <span class="hljs-number">2</span>, <span class="hljs-built_in">range</span>(<span class="hljs-number">10</span>))])  <span class="hljs-comment"># 保留奇数</span>

<span class="hljs-comment"># itertools.filterfalse(predicate,it)</span>
<span class="hljs-comment"># 与filter的作用相反</span>
<span class="hljs-built_in">print</span>([i <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> itertools.filterfalse(<span class="hljs-keyword">lambda</span> a: a % <span class="hljs-number">2</span>, <span class="hljs-built_in">range</span>(<span class="hljs-number">10</span>))])  <span class="hljs-comment"># 保留偶数</span>

<span class="hljs-comment"># itertools.islice(it,stop)或者itertools.islice(it,start,stop,step=1)</span>
<span class="hljs-comment"># 产出it的切片 实现的是惰性操作</span>
<span class="hljs-built_in">print</span>([i <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> itertools.islice(<span class="hljs-built_in">range</span>(<span class="hljs-number">10</span>), <span class="hljs-number">2</span>)])
<span class="hljs-built_in">print</span>([i <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> itertools.islice(<span class="hljs-built_in">range</span>(<span class="hljs-number">10</span>), <span class="hljs-number">2</span>, <span class="hljs-number">9</span>, <span class="hljs-number">3</span>)])

<span class="hljs-comment">#end</span>
</code></pre>

<p><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/70d7187e1a614c248be8deb291e0dd39.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_18,color_FFFFFF,t_70,g_se,x_16" style="height:303px; width:562px" /></p>

<p>&nbsp;</p>

<h1>用于映射的生成器函数</h1>

<p>&nbsp;</p>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-keyword">import</span> itertools
<span class="hljs-keyword">import</span> fractions
<span class="hljs-keyword">import</span> operator

<span class="hljs-comment"># itertools.accumulate(it,func)</span>
<span class="hljs-comment"># 产出累积的总和，如果提供了func，那么把前两个元素传给它，然后把计算的结果和下一个元素传给它，以此类推</span>
<span class="hljs-built_in">print</span>([i <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> itertools.accumulate(<span class="hljs-built_in">range</span>(<span class="hljs-number">10</span>), <span class="hljs-keyword">lambda</span> a, b: a + b)])  <span class="hljs-comment"># 计算前n项的和</span>

<span class="hljs-comment"># enunerate(it,start=0)</span>
<span class="hljs-comment"># 产出由两个元素构成的元组 结构是(index,item) index从start开始，每次加一 item的值中it中取</span>
<span class="hljs-built_in">print</span>([i <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> <span class="hljs-built_in">enumerate</span>(<span class="hljs-built_in">range</span>(<span class="hljs-number">10</span>), start=<span class="hljs-number">10</span>)])

<span class="hljs-comment"># map(func,iter,[it2,...itn])</span>
<span class="hljs-comment"># 把it中的各个元素传给func，产出结果，如果传入n个it，func的参数必须有n个</span>
<span class="hljs-built_in">print</span>([i <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> <span class="hljs-built_in">map</span>(<span class="hljs-keyword">lambda</span> a, b, c: a + b + c, <span class="hljs-built_in">range</span>(-<span class="hljs-number">10</span>, <span class="hljs-number">0</span>, <span class="hljs-number">1</span>), <span class="hljs-built_in">range</span>(<span class="hljs-number">10</span>), <span class="hljs-built_in">range</span>(<span class="hljs-number">10</span>, <span class="hljs-number">20</span>))])  <span class="hljs-comment"># 对it1，it2，it3对应位置的元素进行求和</span>
<span class="hljs-comment"># itertools.startmap(func,it)</span>
<span class="hljs-comment"># 把it中的各个元素传给func，产出结果</span>
<span class="hljs-built_in">print</span>([i <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> itertools.starmap(operator.mul, <span class="hljs-built_in">enumerate</span>(<span class="hljs-string">&#39;hello world&#39;</span>, <span class="hljs-number">1</span>))])  <span class="hljs-comment"># 从1开始，根据字母所在位置，把字母重复相应的次数</span>
</code></pre>

<p><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/bc54a45870f74b50a29dfd4fd34e6abe.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16" style="height:166px; width:900px" /></p>

<h1>&nbsp;合并多个可迭代对象的生成器函数</h1>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-keyword">import</span> itertools

<span class="hljs-comment"># itertools.chain(it1,[it2...it2])</span>
<span class="hljs-comment"># 先产出it1中的元素，然后产出it2中的元素，以此类推，无缝连接在一起</span>
<span class="hljs-built_in">print</span>([i <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> itertools.chain(<span class="hljs-built_in">range</span>(<span class="hljs-number">10</span>), <span class="hljs-built_in">range</span>(<span class="hljs-number">11</span>, <span class="hljs-number">20</span>), <span class="hljs-string">&#39;hello world&#39;</span>)])

<span class="hljs-comment"># itertools.chain.from_iterable(it)</span>
<span class="hljs-comment"># 功能同itertools.chain 不过传入的参数的结构有所变化   it的结构：it=[iter1,[iter2...itern]]</span>
<span class="hljs-built_in">print</span>([i <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> itertools.chain.from_iterable([<span class="hljs-built_in">range</span>(<span class="hljs-number">10</span>), <span class="hljs-string">&#39;hello&#39;</span>])])

<span class="hljs-comment"># itertools.product(it1,...itn,repeat=1)</span>
<span class="hljs-comment"># 计算笛卡尔积，从输入的各个可迭代对象中获取元素，合并成由N个元素组成的元组，与嵌套的for循环效果一样，repeat指明重复处理多少次输入的可迭代对象</span>
<span class="hljs-built_in">print</span>([i <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> itertools.product(<span class="hljs-built_in">range</span>(<span class="hljs-number">3</span>), <span class="hljs-string">&#39;hello&#39;</span>, <span class="hljs-string">&#39;world&#39;</span>, repeat=<span class="hljs-number">1</span>)])

<span class="hljs-comment"># zip(it1,...itn)</span>
<span class="hljs-comment"># 并行从输入的各个可迭代对象中获取元素，产出由N个元素组成的元组，只要有一个可迭代对象到了头，迭代就终止</span>
<span class="hljs-built_in">print</span>([i <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> <span class="hljs-built_in">zip</span>(<span class="hljs-built_in">range</span>(<span class="hljs-number">5</span>), <span class="hljs-string">&#39;hello&#39;</span>)])

<span class="hljs-comment"># zip_longest(it1,..itn,fillvalue=None)</span>
<span class="hljs-comment"># 与zip作用一样，但是终止条件是最长的可迭代对象到头了才终止，其他可迭代对象空缺的值用fillvalue进行补充</span>
<span class="hljs-built_in">print</span>([i <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> itertools.zip_longest(<span class="hljs-built_in">range</span>(<span class="hljs-number">10</span>), <span class="hljs-string">&#39;hello&#39;</span>, fillvalue=<span class="hljs-string">&#39;world&#39;</span>)])
</code></pre>

<p><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/3d3da097e55b4ef4aae5b07c27c5ebdb.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16" style="height:142px; width:900px" /></p>

<h1>&nbsp;把输入的各个元素扩展成多个输出元素的生成器函数</h1>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-keyword">import</span> itertools

<span class="hljs-comment"># itertools.combinations(it,out_len)  组合 和顺序无关</span>
<span class="hljs-comment"># 把it产出的out_len个元素组合在一起，然后产出</span>
<span class="hljs-built_in">print</span>([i <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> itertools.combinations(<span class="hljs-string">&#39;ABC&#39;</span>, <span class="hljs-number">2</span>)])  <span class="hljs-comment"># 产出两两组合的元素</span>

<span class="hljs-comment"># itertools.combinations_with_replacement 组合</span>
<span class="hljs-comment"># 功能同itertools.combinations，但是也包含自己和自己的组合</span>
<span class="hljs-built_in">print</span>([i <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> itertools.combinations_with_replacement(<span class="hljs-string">&#39;ABC&#39;</span>, <span class="hljs-number">2</span>)])

<span class="hljs-comment"># itertools.count(start=0,step=1)</span>
<span class="hljs-comment"># 从start开始，以step为步长，不断产出数字</span>
<span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> itertools.count(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>):
    <span class="hljs-built_in">print</span>(i, end=<span class="hljs-string">&#39; &#39;</span>)
    <span class="hljs-keyword">if</span> i &gt; <span class="hljs-number">10</span>: <span class="hljs-keyword">break</span>
<span class="hljs-built_in">print</span>()

<span class="hljs-comment"># itertools.permutations(it,out_len=len(list(it)))</span>
<span class="hljs-comment"># 把it产出的out_len个元素排列在一起  排列  和顺序有关</span>
<span class="hljs-built_in">print</span>([i <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> itertools.permutations(<span class="hljs-string">&#39;ABC&#39;</span>, <span class="hljs-number">2</span>)])

<span class="hljs-comment"># repeat(item,[times])</span>
<span class="hljs-comment"># 重复不断的产出指定的元素，除非提供times指定次数</span>
<span class="hljs-built_in">print</span>([i <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> itertools.repeat(<span class="hljs-string">&#39;hello&#39;</span>, <span class="hljs-number">10</span>)])

<span class="hljs-comment"># itertools.cycle(it)</span>
<span class="hljs-comment"># 从it中产出各个元素，存储各个元素的副本，然后按顺序重复不断地产出各个元素</span>
cy = itertools.cycle(<span class="hljs-string">&#39;ABC&#39;</span>)  <span class="hljs-comment"># 将it首位相连</span>
<span class="hljs-keyword">while</span> <span class="hljs-literal">True</span>:
    <span class="hljs-built_in">print</span>(<span class="hljs-built_in">next</span>(cy))
    <span class="hljs-keyword">break</span>
</code></pre>

<p><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/6bec6cbad9da43289c8b8473759bf358.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16" style="height:238px; width:900px" /></p>

<h1>&nbsp;用于重新排列元素的生成器函数</h1>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-keyword">import</span> itertools

<span class="hljs-comment"># itertools.groupby(it,key=None)</span>
<span class="hljs-comment"># 产出由练个元素组成的元素，形式为(key,group)，其中key是分组标准，group是生成器，用于产出分组里的元素</span>
strs_list = [<span class="hljs-string">&#39;hello&#39;</span>, <span class="hljs-string">&#39;world&#39;</span>, <span class="hljs-string">&#39;we&#39;</span>, <span class="hljs-string">&#39;price&#39;</span>, <span class="hljs-string">&#39;the&#39;</span>, <span class="hljs-string">&#39;things&#39;</span>, <span class="hljs-string">&#39;when&#39;</span>, <span class="hljs-string">&#39;we&#39;</span>, <span class="hljs-string">&#39;have&#39;</span>, <span class="hljs-string">&#39;lost&#39;</span>, <span class="hljs-string">&#39;them&#39;</span>, <span class="hljs-string">&#39;.&#39;</span>]
strs_list.sort(key=<span class="hljs-built_in">len</span>)  <span class="hljs-comment"># 先排序</span>
<span class="hljs-keyword">for</span> key, group <span class="hljs-keyword">in</span> itertools.groupby(strs_list, key=<span class="hljs-built_in">len</span>):  <span class="hljs-comment"># 根据元素的长度进行分组</span>
    <span class="hljs-built_in">print</span>(key, <span class="hljs-built_in">list</span>(group))

<span class="hljs-comment"># reversed(seq)</span>
<span class="hljs-comment"># 从后向前，倒序产出seq seq必须是序列，或者是实现了__reversed__的对象</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">list</span>(<span class="hljs-built_in">reversed</span>(strs_list)))

<span class="hljs-comment"># itertools.tee(it,n=2)</span>
<span class="hljs-comment"># 产出一个由n个生成器组成的元组，每个生成器用于单独产出输入的可迭代对象中的元素</span>
g1, g2 = itertools.tee(<span class="hljs-string">&#39;ABC&#39;</span>)
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">list</span>(g1))
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">list</span>(g2))
</code></pre>

<p><img src="../media/image/2022/04/18/image-20220418094344-1.png" style="height:458px; width:900px" /></p>

<p>&nbsp;</p>

<h1>总结</h1>

<p>python的大部分的内置功能都是用c实现的，这些生成器函数也不例外，它们不仅功能强大，性能也是相当不错的，因此，掌握它们对你的代码优化上会有不小的帮助哦！</p>

