
<BlogInfo title="《流畅的python》学习笔记之我们常用的列表list和元组tuple还有这个秘密？" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=105 category="《流畅的python》" tag_list="['笔记', '序列', '巩固']" create_time="2022.02.13 22:07:51.199276" update_time="2022.07.11 10:41:44" />

^^^^^^^^^
<h2><strong>&nbsp;前言</strong></h2>

<p>不知道大家在学习python中数据类型的时候，在学到tuple和list的区别时，是不是想到的第一句话就是list是可变数据类型，tuple是不可变数据类型，我就猜到了，你想到的肯定是这个嘿嘿</p>

<p>&nbsp;</p>

<h2><strong>可变和不可变序列</strong></h2>

<p>其实这是分类python中序列的一种方法，即可变序列和不可变序列。</p>

<p><strong>python中的可变序列</strong></p>

<p>list，bytearray，array.array.collections.deque和memoryview</p>

<p><strong>python中的不可变序列</strong></p>

<p>tuple，str和bytes</p>

<p>&nbsp;</p>

<p>在说另一种分类方法之前，先来看一个神奇的问题???</p>

<pre>
<code>a = [[]]
b = a * 3
a[0].append(&#39;Python&#39;)
print(f&#39;添加Python之后的b:{b}&#39;)</code></pre>

<p>不知道大家有没有猜到答案，正确答案如下：</p>

<p><img src="../media/image/2022/02/13/image-20220213220738-1.png" style="height:305px; width:902px" /></p>

<p>不知道大家猜到的答案是不是[[], [], []]或者[[&#39;Python&#39;], [], []]或者其他答案？明明是列表a添加了&ldquo;python&rdquo;，关我列表b毛事哈哈哈???</p>

<p>但是为啥是上面这个答案呢？？？<img alt="" src="https://img-blog.csdnimg.cn/b8cbd1c95cc145bfb5b5a35eb94c80d8.gif" style="height:320px; width:320px" /></p>

<p>&nbsp;这就要谈到python中序列的另一种分类方式了！</p>

<p>&nbsp;</p>

<h2><strong>容器序列和扁平序列</strong></h2>

<p>python中的容器序列包含：list，tuple和collections.deque</p>

<p>python中的扁平序列包含：str，bytes，bytearray，memoryview，=和array.array</p>

<p>&nbsp;</p>

<p>按照这个分类来，你们有没有发现容器序列中，它们存放的元素的类型可以是不同的，比如在同一个list中，既可以存放str，tuple，也可以存放int；但是在扁平容序列中，存放的元素类型必须是一致的，str就就必须全是字符型，bytes就必须全是自字节型。</p>

<p>说到这里，不知道大家有没有想到答案？<strong>其实能容器序列之所以能够存储不同类型的元素，是因为它存储的不是元素本身，而是对元素的引用，存储的是元素的地址！</strong>说到这里，想必大家都云雾顿开了吧！！！（配个图也许更清楚一些）</p>

<p><img alt="" src="https://img-blog.csdnimg.cn/c02791ed7d054c25b0662c5001428e6e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16" style="height:373px; width:684px" /></p>

<p>&nbsp;</p>

<h2><strong>其他小知识点（可能是你的知识点盲区哦）</strong></h2>

<p><strong>1.你知道python中如何获取一个字符对应的unicode编码吗？</strong></p>

<p>答案就是ord()函数：</p>

<p><img alt="" src="https://img-blog.csdnimg.cn/435a1aa749f24803bd8006c8e2fac76a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_17,color_FFFFFF,t_70,g_se,x_16" style="height:102px; width:548px" /></p>

<p><img alt="" src="https://img-blog.csdnimg.cn/8bb245d4436c4c4a8a28e07a40c53f2b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_19,color_FFFFFF,t_70,g_se,x_16" style="height:130px; width:548px" />&nbsp;</p>

<p>2.你知道最简的生成器表达式吗？</p>

<p>答案就是小括号！</p>

<p><img alt="" src="https://img-blog.csdnimg.cn/9e3dddd3c6094227b79348ba49cc4b66.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16" style="height:370px; width:1024px" /></p>

<p>&nbsp;<strong>3.你知道*除了看作是乘法外，却不知道它还有拆包的作用吗？</strong></p>

<p><img alt="" src="https://img-blog.csdnimg.cn/176c9814402c4c39bf408e9719f8d2b7.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16" style="height:588px; width:1017px" /></p>

<p><strong>&nbsp;4.假设s是一个序列，对s进行的s[a:b:c]切片含义你知道吗？</strong></p>

<p>答：在a，b以间隔为c进行取值。</p>

<p><img alt="" src="https://img-blog.csdnimg.cn/f0f8089883824a3caadd94dc7e6b082b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16" style="height:603px; width:1017px" /></p>

<p>&nbsp;</p>

<p>以上就是今天学习的《流畅的python》第二章的前半部分的内容了，感觉收货不少！希望也对大家有所帮助！</p>

<p>加油！<img alt="" src="https://img-blog.csdnimg.cn/0dc483e5c13a4822a1989290dcb56a44.gif" style="height:48px; width:48px" /><img alt="" src="https://img-blog.csdnimg.cn/0dc483e5c13a4822a1989290dcb56a44.gif" style="height:48px; width:48px" /><img alt="" src="https://img-blog.csdnimg.cn/0dc483e5c13a4822a1989290dcb56a44.gif" style="height:48px; width:48px" /></p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

