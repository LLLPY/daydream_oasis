
<BlogInfo title="python中__init__真的会在__new__完成后执行吗？" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=30 category="《流畅的python》" tag_list="['笔记']" create_time="2022.07.15 14:48:46.107470" update_time="2022.09.03 10:16:24" />

^^^^^^^^^
<h1>前言</h1>

<blockquote>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在看书的过程中又发现了这个知识点盲区。有些东西不自己亲手去尝试，真的不会知道：居然是这样子的？</p>
</blockquote>

<h1>常规思路</h1>

<blockquote>
<p>&nbsp; &nbsp; &nbsp; &nbsp; 大家可能都知道，在python中创建一个对象的流程是：首先调用__new__方法创建一个实例，然后再调用__init__方法初始化这个实例对象。这个是常规的思路，也没有什么问题。</p>
</blockquote>

<h1>蹊跷的事情发生了！</h1>

<blockquote>
<p>&nbsp; &nbsp; &nbsp; &nbsp; 直接说结果吧：如果__new__方法返回的对象不是当前的类的实例，它就不会调用__init__方法。</p>

<p>&nbsp; &nbsp; &nbsp; &nbsp; 直接看下面的栗子吧(talk is cheap，show me your&nbsp; code.)：</p>

<pre>
<code># __new__方法执行完成后不一定会调用__init__方法
# 只有当__new__方法返回的对象是当前类的实例时才会调用__init__方法
class A:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)
        # return &#39;hello world！&#39;

    def __init__(self):
        print(&#39;调用了__init__方法！&#39;)
a = A()</code></pre>

<p><img alt="" src="https://img-blog.csdnimg.cn/219a8f245c4544e58fae72ef2da89d3c.png" style="height:429px; width:900px" /></p>

<p>&nbsp;</p>
</blockquote>

<h1>总结</h1>

<blockquote>
<p>&nbsp; &nbsp; &nbsp; &nbsp; __init__方法只有在__new__方法返回的实例是当前类(祖先类)的实例的情况下才会被自动调用。</p>
</blockquote>

