
<BlogInfo title="python中iter()的高阶用法" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=35 category="《流畅的python》" tag_list="['iter()']" create_time="2022.04.18 10:33:19.910392" update_time="2022.04.18 10:33:19" />

^^^^^^^^^
<h1>&nbsp;前言</h1>

<p>众所周知，在python中，iter()函数的功能是：接受一个可迭代对象，将其转换成一个迭代器。</p>

<p>举个栗子：</p>

<pre data-widget="codeSnippet">
<code class="hljs language-python">
a=[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>]
a_iter=<span class="hljs-built_in">iter</span>(a)
<span class="hljs-built_in">print</span>(a_iter)
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">next</span>(a_iter))
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">next</span>(a_iter))</code></pre>

<p><img src="../media/image/2022/04/18/image-20220418103318-1.png" style="height:219px; width:703px" /></p>

<p>上面就是iter()的一般用法。</p>

<h1>iter()的高阶用法</h1>

<p>但是，iter()还有一个更好玩的用法！</p>

<p>简单做一下描述：传入两个参数：使用常规的函数或者任何可调用的对象创建迭代器。这样使用时，<strong>第一个参数必须是可调用的对象（无参数调用）</strong>，用于不断调用产出值，<strong>第二个是哨符，这个是标记值</strong>，当可调用的对象返回这个值时，触发迭代器抛出StopIteration异常，程序结束！</p>

<p>一句话概括一下：<strong>第一个参数中的对象不断产出值，如果产出的值和第二个参数是一样的，就停止产出！</strong></p>

<p>举个栗子：</p>

<p>随机产生1到10的数字，如果产出数字是5就停止。</p>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-keyword">from</span> random <span class="hljs-keyword">import</span> randint

<span class="hljs-keyword">def</span> <span class="function_ hljs-title">d10</span>():
    <span class="hljs-keyword">return</span> randint(<span class="hljs-number">1</span>, <span class="hljs-number">10</span>)


<span class="hljs-comment"># 随机产生1~10之间的数，遇到5就停止</span>
<span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> <span class="hljs-built_in">iter</span>(d10, <span class="hljs-number">5</span>):
    <span class="hljs-built_in">print</span>(i)</code></pre>

<p><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/acc578d29a674c2f9a419d1a69905425.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_16,color_FFFFFF,t_70,g_se,x_16" style="height:345px; width:501px" /></p>

<p>&nbsp;是不是感jio很新鲜，快去亲手试一试吧！</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

