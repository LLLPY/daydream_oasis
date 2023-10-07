
<BlogInfo title="python中可迭代的归约函数，功能这么强，你能不爱？ ？ ？" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=49 category="《流畅的python》" tag_list="['归约函数']" create_time="2022.04.18 10:14:45.177403" update_time="2022.04.18 10:14:45" />

^^^^^^^^^
<p>&nbsp;相信学习python的小伙伴都用过这些函数，但是它们的功能真的太强了，还是忍不住把它们总结记录一下！！！</p>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-keyword">import</span> functools
<span class="hljs-keyword">import</span> itertools

<span class="hljs-comment"># 归约函数:接受一个可迭代对象，然后返回单个结果的函数。</span>

<span class="hljs-comment"># all(it)</span>
<span class="hljs-comment"># it中的所有元素都为真时返回True，否者返回False</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">all</span>(<span class="hljs-built_in">range</span>(<span class="hljs-number">10</span>)))  <span class="hljs-comment"># 因为出现了0，所以返回False</span>

<span class="hljs-comment"># any(it)</span>
<span class="hljs-comment"># 只有有一个元素是True就返回True，否者返回False</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">any</span>(<span class="hljs-built_in">range</span>(<span class="hljs-number">10</span>)))

<span class="hljs-comment"># max(it,[key=],[default=])</span>
<span class="hljs-comment"># 返回it中的最大值，key指定排序规则，如果it为空，返回default的值</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">max</span>([<span class="hljs-string">&#39;apple&#39;</span>, <span class="hljs-string">&#39;banana&#39;</span>, <span class="hljs-string">&#39;orange&#39;</span>, <span class="hljs-string">&#39;peach&#39;</span>], key=<span class="hljs-built_in">len</span>, default=<span class="hljs-string">&#39;apple&#39;</span>))  <span class="hljs-comment"># 按照长度进行比较</span>

<span class="hljs-comment"># min(it,[key=],[default=])</span>
<span class="hljs-comment"># 返回it中的最小值，key指定排序规则，如果it为空，返回default的值</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">min</span>([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, -<span class="hljs-number">4</span>, -<span class="hljs-number">9</span>, <span class="hljs-number">6</span>], key=<span class="hljs-built_in">abs</span>, default=<span class="hljs-number">0</span>))  <span class="hljs-comment"># 按照绝对值进行比较</span>

<span class="hljs-comment"># itertools.reduce(func,it,[initial])</span>
<span class="hljs-comment"># 把前两个元素传给func，然后把计算结果和第三个元素传给func，以此类推，返回最后的结果，如果提供了initial</span>
<span class="hljs-comment"># 就会把它当做第一个元素传入</span>
<span class="hljs-built_in">print</span>(functools.reduce(<span class="hljs-keyword">lambda</span> a, b: a * b, <span class="hljs-built_in">range</span>(<span class="hljs-number">1</span>, <span class="hljs-number">11</span>)))  <span class="hljs-comment"># 计算10！</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">list</span>(itertools.accumulate(<span class="hljs-built_in">range</span>(<span class="hljs-number">1</span>, <span class="hljs-number">11</span>), <span class="hljs-keyword">lambda</span> a, b: a * b)))  <span class="hljs-comment"># 依次计算1! 2! 3!...10!</span>

<span class="hljs-comment"># sum(it,start=0)</span>
<span class="hljs-comment"># it中所有元素的总和，如果提供可选的start，会把它加上</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">sum</span>(<span class="hljs-built_in">range</span>(<span class="hljs-number">3</span>), start=<span class="hljs-number">10</span>))  <span class="hljs-comment"># 0+1+2+10=13</span>
</code></pre>

<p><img src="../media/image/2022/04/18/image-20220418101439-1.png" style="height:319px; width:900px" /></p>

<p>请告诉我，这些函数中哪个你没有用到手软？？？如果有的话，那么证明你对python的爱还是不够哈哈哈哈哈哈</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

