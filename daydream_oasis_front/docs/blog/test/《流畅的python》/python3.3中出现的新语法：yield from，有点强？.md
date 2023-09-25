
<BlogInfo title="python3.3中出现的新语法：yield from，有点强？" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=40 category="《流畅的python》" tag_list="['yield from']" create_time="2022.04.18 10:07:11.395021" update_time="2022.04.18 10:07:11" />

^^^^^^^^^
<h1>&nbsp;前言</h1>

<p>我们知道，一个函数中，如果出现了yield关键字，那么它一定是一个生成器函数！那yield from又是个啥？</p>

<p>&nbsp;</p>

<p>不知道小伙伴有没有看过我上一篇的：<a class="link-info" contenteditable="true" data-link-icon="https://csdnimg.cn/release/blog_editor_html/release2.0.9/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3C8" data-link-title="标准库中的生成器函数" data-widget="csdnlink" href="https://blog.csdn.net/max_LLL/article/details/124241937" title="标准库中的生成器函数">标准库中的生成器函数</a>，其中就讲到过一个生成器函数：itertools.chain()，它的功能就是将多个可迭代对象无缝连接在一起！</p>

<p><img src="../media/image/2022/04/18/image-20220418100701-1.png" style="height:248px; width:900px" /></p>

<p>&nbsp;</p>

<p>功能看上去不是很复杂，要不我们自己实现一下试试？</p>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-comment"># 例：自己实现chain</span>
<span class="hljs-keyword">def</span> <span class="function_ hljs-title">my_chain</span>(<span class="hljs-params">*iterable</span>):
    <span class="hljs-keyword">for</span> it <span class="hljs-keyword">in</span> iterable:
        <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> it:
            <span class="hljs-keyword">yield</span> i</code></pre>

<p><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/4c2cb5a2d199440c9cd833be46b7f0cc.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16" style="height:488px; width:756px" /></p>

<p>&nbsp;可以看到，实现非常简单，只需要使用一个嵌套循环就可以了！</p>

<p>不过还有更高效的实现方法，那就是yield from的功能了！</p>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-comment"># 使用yield from实现</span>
<span class="hljs-keyword">def</span> <span class="function_ hljs-title">chain</span>(<span class="hljs-params">*iterable</span>):
    <span class="hljs-keyword">for</span> it <span class="hljs-keyword">in</span> iterable:
        <span class="hljs-keyword">yield</span> <span class="hljs-keyword">from</span> it</code></pre>

<p><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/fbbdad07e60b4914b504a6d3493fa339.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16" style="height:414px; width:838px" /></p>

<p>可以看到，结果还是一样的，但是使用yield from直接代替了内层的for循环！&nbsp;这样代码读起来更顺畅，其实除了代替循环之外，yield from还会创建通道，把内层生成器直接与外层生成器的客户端联系起来。把生成器当成协程使用时，这个通道特别重要，不仅能为客户端代码生成值，还能使用客户端代码提供值！协程就留着以后再讲吧~</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

