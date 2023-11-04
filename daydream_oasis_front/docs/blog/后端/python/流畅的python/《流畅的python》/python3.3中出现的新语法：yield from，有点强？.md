
<BlogInfo id="764" title="python3.3中出现的新语法：yield from，有点强？" author="白日梦想猿" pv=0 read_times=0 pre_cost_time="40" category="《流畅的python》" tag_list="['yield from']" create_time="2022.04.18 10:07:11.395021" update_time="2022.04.18 10:07:11" />

#  前言

我们知道，一个函数中，如果出现了yield关键字，那么它一定是一个生成器函数！那yield from又是个啥？

不知道小伙伴有没有看过我上一篇的：[标准库中的生成器函数](https://blog.csdn.net/max_LLL/article/details/124241937
"标准库中的生成器函数")，其中就讲到过一个生成器函数：itertools.chain()，它的功能就是将多个可迭代对象无缝连接在一起！

![](../media/image/2022/04/18/image-20220418100701-1.png)

功能看上去不是很复杂，要不我们自己实现一下试试？


```python
# 例：自己实现chain
def my_chain(*iterable):
    for it in iterable:
        for i in it:
            yield i
```

![](https://img-blog.csdnimg.cn/4c2cb5a2d199440c9cd833be46b7f0cc.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16)

 可以看到，实现非常简单，只需要使用一个嵌套循环就可以了！

不过还有更高效的实现方法，那就是yield from的功能了！


```python
# 使用yield from实现
def chain(*iterable):
    for it in iterable:
        yield from it
```


![](https://img-blog.csdnimg.cn/fbbdad07e60b4914b504a6d3493fa339.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16)

可以看到，结果还是一样的，但是使用yield from直接代替了内层的for循环！ 这样代码读起来更顺畅，其实除了代替循环之外，yield
from还会创建通道，把内层生成器直接与外层生成器的客户端联系起来。把生成器当成协程使用时，这个通道特别重要，不仅能为客户端代码生成值，还能使用客户端代码提供值！协程就留着以后再讲吧~
