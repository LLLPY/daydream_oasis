
<BlogInfo title="python并发编程之协程" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=195 category="并发编程" tag_list="[]" create_time="2022.09.30 17:45:49.055381" update_time="2022.09.30 17:45:49" />

^^^^^^^^^
<blockquote>
<p>摸鱼之余，跟着官方文档把协程这块过了一下。</p>
</blockquote>

<p><strong>目录</strong></p>

<p>&nbsp;</p>

<p><a href="#%E4%BD%93%E9%AA%8C%E5%8D%8F%E7%A8%8B" target="_self">体验协程</a></p>

<p><a href="#create_task%E5%B9%B6%E5%8F%91%E6%89%A7%E8%A1%8C" target="_self">create_task并发执行</a></p>

<p><a href="#%E5%8F%AF%E7%AD%89%E5%BE%85%E5%AF%B9%E8%B1%A1" target="_self">可等待对象</a></p>

<p><a href="#%E8%BF%90%E8%A1%8Casyncio%E7%A8%8B%E5%BA%8F" target="_self">运行asyncio程序</a></p>

<p><a href="#%E2%80%8B%E7%BC%96%E8%BE%91" target="_self">​编辑</a></p>

<p><a href="#%E5%88%9B%E5%BB%BA%E4%BB%BB%E5%8A%A1" target="_self">创建任务</a></p>

<p><a href="#sleep%E4%BC%91%E7%9C%A0" target="_self">sleep休眠</a></p>

<hr />
<p>&nbsp;</p>

<h1>体验协程</h1>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-keyword">import</span> asyncio
<span class="hljs-keyword">import</span> time
    

<span class="hljs-keyword">async</span> <span class="hljs-keyword">def</span> <span class="function_ hljs-title">say_afeter</span>(<span class="hljs-params">delay,msg</span>):
    <span class="hljs-keyword">await</span> asyncio.sleep(delay)
    <span class="hljs-built_in">print</span>(msg)



<span class="hljs-keyword">async</span> <span class="hljs-keyword">def</span> <span class="function_ hljs-title">test</span>():
    start=time.time()    
    <span class="hljs-keyword">await</span> say_afeter(<span class="hljs-number">1</span>,<span class="hljs-string">&#39;hello world&#39;</span>)
    <span class="hljs-keyword">await</span> say_afeter(<span class="hljs-number">2</span>,<span class="hljs-string">&#39;hello python&#39;</span>)
    end =time.time()
    <span class="hljs-built_in">print</span>(<span class="hljs-string">&#39;execute cost %f&#39;</span>%(end- start))


<span class="hljs-keyword">if</span> __name__==<span class="hljs-string">&quot;__main__&quot;</span>:
    asyncio.run(test()) </code></pre>

<p><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/61b96ef8afaf4288a1ec1929b51e9481.png" style="height:215px; width:625px" /></p>

<p>&nbsp;</p>

<h1>create_task并发执行</h1>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-keyword">import</span> asyncio
<span class="hljs-keyword">from</span> time <span class="hljs-keyword">import</span> sleep,time
<span class="hljs-keyword">from</span> turtle <span class="hljs-keyword">import</span> st

<span class="hljs-keyword">async</span> <span class="hljs-keyword">def</span> <span class="function_ hljs-title">say_after</span>(<span class="hljs-params">delay,words</span>):
    <span class="hljs-keyword">await</span> asyncio.sleep(delay)
    <span class="hljs-built_in">print</span>(words)



<span class="hljs-keyword">async</span> <span class="hljs-keyword">def</span> <span class="function_ hljs-title">test</span>():
    
    start=time()
    task1=asyncio.create_task(say_after(<span class="hljs-number">1</span>,<span class="hljs-string">&#39;hello world&#39;</span>))
    task2=asyncio.create_task(say_after(<span class="hljs-number">2</span>,<span class="hljs-string">&#39;hello python&#39;</span>))    
    mid=time()
    <span class="hljs-keyword">await</span> task1
    <span class="hljs-keyword">await</span> task2
    end=time()
    <span class="hljs-comment">#使用create_task后，task1和task2并发运行，从耗时结果也可以看到，task1和task2总共耗时2s左右</span>
    <span class="hljs-built_in">print</span>(<span class="hljs-string">&#39;execute cost %f --- %f&#39;</span>%(mid-start,end-start)) 
    



<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">&#39;__main__&#39;</span>:
    asyncio.run(test())

</code></pre>

<p><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/0ea645b466854337af64eabfc1cf5524.png" style="height:234px; width:598px" /></p>

<p>&nbsp;</p>

<h1>可等待对象</h1>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-keyword">import</span> asyncio
<span class="hljs-keyword">from</span> operator <span class="hljs-keyword">import</span> ne



<span class="hljs-comment">#可等待对象</span>
<span class="hljs-string">&#39;&#39;&#39;
如果一个对象可以在await语句中使用，那么它就是可等待对象。
可等待的对象有三种类型：
    1.协程
    2.任务
    3.Future


#协程
    1.协程函数：使用async定义的函数被称为协程函数
    2.协程对象：协程函数返回的对象就是协程对象

#任务
    通过asyncio.create_task(async fun)可以将一个协程函数func转成一个任务，任务会被自动调度执行

#Future
    1.Future是一种特殊的低层级可等待对象，表示一个异步操作的最终结果。
    2.当一个Future对象被等待，这意味着协程将保持等待直到该Future对象在其他地方的操作完毕。
    3.通常情况下，没有必要在应用层面创建Future对象



&#39;&#39;&#39;</span>



<span class="hljs-comment">#协程</span>
<span class="hljs-keyword">async</span> <span class="hljs-keyword">def</span> <span class="function_ hljs-title">nested</span>():
    <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span>  <span class="hljs-built_in">range</span>(<span class="hljs-number">10</span>):
        <span class="hljs-built_in">print</span>(<span class="hljs-string">&#39;hello python!&#39;</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-number">200</span>



<span class="hljs-keyword">async</span> <span class="hljs-keyword">def</span> <span class="function_ hljs-title">test</span>():
    
    
    <span class="hljs-comment">#协程</span>
    <span class="hljs-comment"># Nothing happens if we just call &quot;nested()&quot;.</span>
    <span class="hljs-comment"># A coroutine object is created but not awaited,</span>
    <span class="hljs-comment"># so it *won&#39;t run at all*.</span>
    nested() <span class="hljs-comment">#仅仅调用协程函数，而不使用await关键字，它是不会被执行的</span>
    
    <span class="hljs-built_in">print</span>(<span class="hljs-keyword">await</span> nested())
    
    
    
    <span class="hljs-comment">#task</span>
    <span class="hljs-string">&#39;&#39;&#39;
    通过create_task将协程函数封装成任务后，它会被自动调度执行
    &#39;&#39;&#39;</span>
    task=asyncio.create_task(nested())
    <span class="hljs-built_in">print</span>(<span class="hljs-built_in">type</span>(task),task)
    <span class="hljs-comment">#在这里可以取消任务</span>
    <span class="hljs-comment"># task.cancel()</span>
    
    
    
    <span class="hljs-keyword">await</span> task <span class="hljs-comment">#可以使用await关键字等待任务被执行完成后再继后面的任务</span>
    
    <span class="hljs-built_in">print</span>(<span class="hljs-string">&#39;task之后的代码被执行了！！！！&#39;</span>)
    
    
    
    <span class="hljs-comment">#Future</span>
    
    
    
    
    

<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">&#39;__main__&#39;</span>:
    asyncio.run(test())</code></pre>

<p><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/536a2fb0b5ce4c818ab1ab5c90b1aa5d.png" style="height:394px; width:773px" /></p>

<h1>运行asyncio程序</h1>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-keyword">import</span> asyncio




<span class="hljs-keyword">async</span> <span class="hljs-keyword">def</span> <span class="function_ hljs-title">say_hello</span>():
    <span class="hljs-built_in">print</span>(<span class="hljs-string">&#39;hello python!&#39;</span>)
    


<span class="hljs-keyword">async</span> <span class="hljs-keyword">def</span> <span class="function_ hljs-title">test</span>():
    <span class="hljs-keyword">await</span> say_hello()
    
    <span class="hljs-comment">#下面这条语句会执行失败，因为在一个asyncio事件循环内部不能有其他的asyncio事件循环</span>
    <span class="hljs-comment"># asyncio.run(say_hello())</span>
    
    <span class="hljs-keyword">return</span> <span class="hljs-string">&#39;coroutine done!&#39;</span>

    
<span class="hljs-keyword">if</span>  __name__ == <span class="hljs-string">&#39;__main__&#39;</span>:


    <span class="hljs-comment">#asyncio.run(coro,*,debug=False)  </span>
    <span class="hljs-string">&#39;&#39;&#39;
        1.执行coroutine coro并返回结果
        2.run函数会执行传入的协程，负责管理asyncio事件循环，终结异步生成器，关闭线程池等。
        3.当有其他的asyncio事件循环在同一个线程中运行时，不能调用它。
        4.如果debug=True，将以调试模式运行
        5.run函数总是会创建一个新的事件循环并在结束的时候关闭它，它应当被当作asyncio程序的主入口点，理想情况下应当只被调用一次
    
    &#39;&#39;&#39;</span>

    
    res=asyncio.run(test())
    <span class="hljs-built_in">print</span>(res)






</code></pre>

<h1><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/1e4caa1c240e415f9276a24f8d5b73d1.png" style="height:89px; width:496px" /></h1>

<p>&nbsp;</p>

<h1>创建任务</h1>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-keyword">import</span> asyncio
<span class="hljs-keyword">from</span> secrets <span class="hljs-keyword">import</span> randbelow


<span class="hljs-keyword">async</span> <span class="hljs-keyword">def</span> <span class="function_ hljs-title">say_hello</span>():
    <span class="hljs-built_in">print</span>(<span class="hljs-string">&#39;hello world!&#39;</span>)


<span class="hljs-keyword">def</span> <span class="function_ hljs-title">done</span>(<span class="hljs-params">task</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-number">1111</span>,task)


<span class="hljs-keyword">async</span> <span class="hljs-keyword">def</span> <span class="function_ hljs-title">test</span>():
    task=asyncio.create_task(say_hello())
    <span class="hljs-keyword">await</span> task
    <span class="hljs-comment">#asyncio.create_task(coro,*,name=None)</span>
    <span class="hljs-string">&#39;&#39;&#39;
         将coro封装成一个Task并调度其执行。
         name：为Task设定名称，同时可以使用Task.set_name()来设定
    
    &#39;&#39;&#39;</span>    
    
    task.set_name(<span class="hljs-string">&#39;say hello!&#39;</span>)
    <span class="hljs-built_in">print</span>(task.get_name())
    
    
    
    
    background_tasks=<span class="hljs-built_in">set</span>()
    <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> <span class="hljs-built_in">range</span>(<span class="hljs-number">10</span>):
        task=asyncio.create_task(say_hello())
        
        background_tasks.add(task)  
        
        task.add_done_callback(background_tasks.discard)
        <span class="hljs-comment"># task.add_done_callback(done)</span>
        
        <span class="hljs-keyword">await</span> task <span class="hljs-comment">#等待task执行完成</span>
        
    
    <span class="hljs-built_in">print</span>(background_tasks)
        



<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">&#39;__main__&#39;</span>:
    asyncio.run(test())</code></pre>

<p><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/fea94cd985784f5aaf040a91e9d7ef78.png" style="height:249px; width:629px" /></p>

<p>&nbsp;</p>

<h1>sleep休眠</h1>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-keyword">import</span> asyncio
<span class="hljs-keyword">import</span> datetime

<span class="hljs-keyword">async</span> <span class="hljs-keyword">def</span> <span class="function_ hljs-title">say_delay</span>(<span class="hljs-params">delay,words</span>):
    
    <span class="hljs-comment">#阻塞一秒后返回一个打印函数</span>
    say=<span class="hljs-keyword">await</span> asyncio.sleep(delay,<span class="hljs-keyword">lambda</span> a:<span class="hljs-built_in">print</span>(a))
    
    say(words)
    <span class="hljs-comment">#asyncio.sleep(delay,result=None)</span>
    <span class="hljs-string">&#39;&#39;&#39;
        1.delay指定阻塞的秒数。
        2.如果指定了result，则当协程完成时将其返回给调用者
        3.sleep()总会挂起当前任务，以允许其他任务执行。
        4.将delay设为0将提供一个经优化的路径以允许其他任务运行。这可供长期间运行的函数以避免
          在函数调用的全程中阻塞事件循环。
    &#39;&#39;&#39;</span>
    
    
<span class="hljs-comment">#程序运行 n s，每秒打印当前日期</span>
<span class="hljs-keyword">async</span> <span class="hljs-keyword">def</span> <span class="function_ hljs-title">show_date_in_time</span>(<span class="hljs-params">n</span>):
    loop=asyncio.get_running_loop()
    end=loop.time()+n
    <span class="hljs-keyword">while</span> <span class="hljs-literal">True</span>:
        <span class="hljs-keyword">if</span> loop.time()&gt;end:<span class="hljs-keyword">break</span>
        
        <span class="hljs-built_in">print</span>(datetime.datetime.now())  

        <span class="hljs-keyword">await</span> asyncio.sleep(<span class="hljs-number">1</span>)
        
        
        
<span class="hljs-keyword">async</span> <span class="hljs-keyword">def</span> <span class="function_ hljs-title">test</span>():
    <span class="hljs-keyword">await</span> say_delay(<span class="hljs-number">1</span>,<span class="hljs-string">&#39;hello world!&#39;</span>)
    <span class="hljs-keyword">await</span> show_date_in_time(<span class="hljs-number">5</span>)
    
    
    

<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">&#39;__main__&#39;</span>:
    asyncio.run(test())
    
    
</code></pre>

<p><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/a0d0c4a26ddf450489146f00a55f48f0.png" style="height:231px; width:567px" /></p>

